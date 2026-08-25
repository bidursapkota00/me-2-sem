# 7. Database Scalability and Optimization

# 7.1 Database Partitioning (Horizontal vs. Vertical)

> **What is database partitioning? Explain different database partitioning techniques in detail with example. [7 marks] (2080)**
>
> **Compare horizontal and vertical database partitioning. Design a scenario for a large e-commerce system and explain which partitioning strategy you would use for the Orders table and why. [7 marks] (2082)**

Database partitioning is the technique of dividing a large database table into smaller, more manageable pieces called partitions. Each partition holds a subset of the data and can be stored, accessed, and managed independently. The primary goals are to improve query performance, enhance manageability, and increase availability. Partitioning can be done within a single database server (intra-node) or across multiple servers (inter-node, often called sharding).

**Horizontal Partitioning:**

Horizontal partitioning divides a table by rows. Each partition contains a subset of the rows but retains all the columns of the original table. Every row exists in exactly one partition. This is the most common form of partitioning for scaling large tables.

Example: An `Orders` table with millions of rows is split so that orders from 2023 go to Partition 1 and orders from 2024 go to Partition 2. Both partitions have the same schema (`order_id`, `customer_id`, `order_date`, `amount`), but each holds different rows.

**Horizontal Partitioning Techniques:**

1. **Range Partitioning:** Rows are assigned to partitions based on whether the partition key falls within a defined range of values. This is effective when queries frequently filter on continuous values like dates, IDs, or prices.

```sql
-- PostgreSQL example
CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2)
) PARTITION BY RANGE (order_date);

CREATE TABLE orders_2023 PARTITION OF orders
    FOR VALUES FROM ('2023-01-01') TO ('2024-01-01');
CREATE TABLE orders_2024 PARTITION OF orders
    FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');
```

Advantage: Efficient for range-based queries (e.g., "all orders in Q1 2024"). The optimizer can perform partition pruning, scanning only the relevant partition.

Disadvantage: Can cause data skew or hotspots if most activity is concentrated in the latest partition.

2. **Hash Partitioning:** A hash function is applied to the partition key, and the hash value determines the target partition. This distributes data uniformly across partitions, preventing hotspots.

```sql
CREATE TABLE users (
    user_id INT,
    username VARCHAR(50),
    email VARCHAR(100)
) PARTITION BY HASH (user_id);

CREATE TABLE users_p0 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 0);
CREATE TABLE users_p1 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 1);
CREATE TABLE users_p2 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 2);
CREATE TABLE users_p3 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 3);
```

Advantage: Even data distribution; avoids hotspots.

Disadvantage: Range queries are inefficient because related rows are scattered across all partitions. Adding or removing partitions requires rehashing and redistributing data.

3. **List Partitioning:** Rows are assigned to partitions based on membership in a predefined list of discrete values. This is suitable for categorical data.

```sql
CREATE TABLE customers (
    customer_id INT,
    name VARCHAR(100),
    country VARCHAR(50)
) PARTITION BY LIST (country);

CREATE TABLE customers_asia PARTITION OF customers
    FOR VALUES IN ('Nepal', 'India', 'China', 'Japan');
CREATE TABLE customers_europe PARTITION OF customers
    FOR VALUES IN ('UK', 'Germany', 'France');
```

Advantage: Ideal for regulatory compliance (keeping regional data on specific servers) and queries that filter by category.

Disadvantage: Requires manual maintenance of value lists; uneven distribution if some categories have far more data than others.

4. **Composite (Sub-) Partitioning:** Combines two partitioning strategies. For example, first partition by range on `order_date`, then sub-partition each range by hash on `customer_id`. This gives the range-query benefits of range partitioning with the even distribution of hash partitioning within each range.

**Vertical Partitioning:**

Vertical partitioning divides a table by columns. The original table is split into two or more tables, each containing a subset of columns. A common key column (usually the primary key) is included in all resulting tables so that the full row can be reconstructed via a join.

Example: A `Products` table with columns (`product_id`, `name`, `price`, `description`, `image_blob`) is split into:
- `Products_Core(product_id, name, price)` — frequently accessed, lightweight columns.
- `Products_Detail(product_id, description, image_blob)` — rarely accessed, large columns.

Advantage: Queries that access only frequently used columns read smaller rows, improving I/O efficiency and cache hit rates. Large BLOBs or rarely-used columns do not waste buffer pool space.

Disadvantage: Queries needing all columns require a join across the split tables, adding overhead.

**E-commerce Scenario — Partitioning the Orders Table:**

For a large e-commerce system, horizontal partitioning by range on `order_date` is typically the best strategy for the `Orders` table. Reasons:
- Most queries are time-bound (recent orders, monthly reports), benefiting from partition pruning.
- Old partitions can be archived or dropped without affecting active data.
- Each partition remains manageable in size.

If queries also frequently filter by `region`, composite partitioning (range on date, list on region) further optimizes access.

---

# 7.2 Caching Strategies (Redis, Memcached)

> **Differentiate between Redis and Memcached Caching Strategies. [8 marks] (2081)**

Caching is the practice of storing frequently accessed data in a fast, in-memory data store to reduce the load on the primary database and decrease response latency. A cache sits between the application and the database, serving repeated requests from memory instead of hitting disk.

**Why Caching Matters:**

Database queries involve disk I/O, query parsing, optimization, and execution — all of which take time. For data that is read far more often than it is written, caching can reduce query latency from milliseconds to microseconds and dramatically increase throughput.

**Common Caching Patterns:**

1. **Cache-Aside (Lazy Loading):** The application checks the cache first. On a cache miss, it fetches data from the database, stores it in the cache, and returns it to the caller. On a cache hit, data is served directly from the cache. This is the most widely used pattern.

```
Read Request:
1. App checks cache for key
2. If HIT → return cached data
3. If MISS → query database → store result in cache → return data
```

Advantage: Only requested data is cached, conserving memory. The cache naturally fills with the most-accessed data.

Disadvantage: The first request always has a cache miss (cold start). Stale data can be served if the database is updated without invalidating the cache.

2. **Write-Through:** Every write operation updates both the cache and the database simultaneously. This ensures the cache always holds the latest data.

Advantage: Cache is always consistent with the database.

Disadvantage: Higher write latency because every write must complete in both the cache and the database. Data that is written but never read still consumes cache space.

3. **Write-Behind (Write-Back):** The application writes data to the cache first, and the cache asynchronously flushes the data to the database after a delay or in batches.

Advantage: Very fast writes; reduced database load through batching.

Disadvantage: Risk of data loss if the cache fails before the data is flushed to the database.

4. **Read-Through:** Similar to cache-aside, but the cache itself is responsible for loading data from the database on a miss, rather than the application.

**Eviction Policies:**

When the cache reaches its memory limit, an eviction policy determines which entries to remove:
- **LRU (Least Recently Used):** Evicts the entry that has not been accessed for the longest time. Most commonly used.
- **LFU (Least Frequently Used):** Evicts the entry with the fewest access counts.
- **TTL (Time-To-Live):** Each entry has an expiration time. Expired entries are automatically removed.
- **Random:** Evicts a randomly chosen entry. Simple but unpredictable.

**Redis:**

Redis (Remote Dictionary Server) is an open-source, in-memory data structure store. It can function as a cache, a database, a message broker, and a streaming engine. Redis stores data as key-value pairs, but the values can be rich data structures.

Key Features:
- **Rich Data Types:** Supports strings, hashes, lists, sets, sorted sets, bitmaps, HyperLogLogs, and streams — not just simple strings.
- **Persistence:** Supports two persistence mechanisms: RDB (point-in-time snapshots) and AOF (Append-Only File that logs every write operation). This means cached data can survive restarts.
- **Single-Threaded Execution:** Uses a single-threaded event loop for command execution, which avoids locking overhead and ensures atomicity of individual commands.
- **Replication and Clustering:** Supports master-replica replication for high availability and Redis Cluster for horizontal partitioning of data across multiple nodes.
- **Pub/Sub and Lua Scripting:** Built-in publish/subscribe messaging and server-side Lua scripting for complex atomic operations.
- **Transactions:** Supports MULTI/EXEC transaction blocks for executing a group of commands atomically.

**Memcached:**

Memcached is an open-source, high-performance, distributed memory caching system designed for simplicity and speed. It stores data as simple key-value pairs where both keys and values are strings.

Key Features:
- **Simple Key-Value Store:** Supports only string data. All data manipulation must be done by the application.
- **Multi-Threaded Architecture:** Uses multiple threads to handle concurrent requests, scaling well across multiple CPU cores.
- **No Persistence:** Data exists only in memory. A restart or failure clears the entire cache.
- **Slab Allocation:** Uses a slab allocator for memory management, which reduces fragmentation and provides predictable performance.
- **Simple Protocol:** Easy to integrate with minimal configuration.

**Redis vs. Memcached:**

| Feature | Redis | Memcached |
|---|---|---|
| Data Types | Strings, hashes, lists, sets, sorted sets, streams | Strings only |
| Threading | Single-threaded (core) | Multi-threaded |
| Persistence | RDB snapshots + AOF | None |
| Max Value Size | 512 MB | 1 MB (default) |
| Eviction Policies | Multiple (LRU, LFU, TTL, etc.) | LRU only |
| Pub/Sub | Yes | No |
| Replication | Master-replica | None (client-side distribution) |
| Scripting | Lua scripting | No |
| Use Case | Complex caching, sessions, queues, leaderboards | Simple, high-throughput key-value caching |

**When to Use Redis:** When the application requires rich data structures, persistence, pub/sub messaging, or atomic operations beyond simple get/set.

**When to Use Memcached:** When the application needs a simple, ephemeral cache with maximum throughput for basic key-value lookups and can benefit from multi-threaded scaling.

---

# 7.3 Load Balancing and High Availability

> **Write short notes on: Load Balancing and High Availability [5 marks] (2082)**

## 7.3.1 Load Balancing

Load balancing is the process of distributing incoming database requests (queries, transactions) across multiple database servers to prevent any single server from becoming a bottleneck. A load balancer sits between the application tier and the database tier, presenting a single endpoint to the application while routing requests to one of several backend servers.

**Load Balancing Algorithms:**

1. **Round Robin:** Requests are distributed to servers in a circular order (Server 1, Server 2, Server 3, Server 1, ...). Simple but does not account for differing server loads or capacities.
2. **Least Connections:** The request is routed to the server with the fewest active connections. Effective when request processing times vary.
3. **Weighted Round Robin:** Each server is assigned a weight based on its capacity. Servers with higher weights receive proportionally more requests.
4. **IP Hash:** A hash of the client's IP address determines which server handles the request, ensuring session affinity (the same client always reaches the same server).

**Read-Write Splitting:**

In a replicated database setup, the load balancer can route read queries to replicas and write queries to the primary server. This is a common strategy because read operations typically outnumber writes by a large factor. The primary handles all writes and propagates changes to replicas via replication.

```
Application → Load Balancer
                ├── Write queries → Primary DB
                └── Read queries  → Replica 1, Replica 2, Replica 3
```

## 7.3.2 High Availability (HA)

High availability refers to the design of systems that remain operational and accessible for a very high percentage of time, typically measured in "nines" (e.g., 99.99% uptime means at most ~52 minutes of downtime per year). The goal is to eliminate single points of failure.

**Replication for HA:**

Database replication maintains identical copies of data on multiple servers. If the primary server fails, a replica can be promoted to take over.

1. **Synchronous Replication:** The primary waits for at least one replica to acknowledge the write before confirming it to the client. Guarantees zero data loss during failover but increases write latency.
2. **Asynchronous Replication:** The primary confirms the write to the client immediately and propagates the change to replicas in the background. Lower write latency but risks losing the most recent writes if the primary fails before replication completes.

**Failover Mechanisms:**

Failover is the process of automatically switching to a standby server when the primary fails.

1. **Active-Passive (Primary-Standby):** One server actively handles all traffic. One or more standby servers remain idle, continuously receiving replicated data. When the primary fails, the standby is promoted. Simple to manage but the standby resources are underutilized during normal operation.
2. **Active-Active (Multi-Master):** Multiple servers simultaneously handle read and write traffic. If one server fails, the remaining servers absorb its load. Provides higher resource utilization and near-instant failover but introduces complexity in handling write conflicts and maintaining data consistency.

**Health Checks and Heartbeats:**

Load balancers and cluster managers continuously monitor database servers by sending periodic heartbeat signals (small health-check queries). If a server fails to respond within a timeout period, it is marked as unhealthy and removed from the pool. Once it recovers, it is automatically added back.

**Achieving HA in Practice:**

- Deploy database replicas across different physical machines and ideally across different data centers or availability zones.
- Use automatic failover tools (e.g., PostgreSQL Patroni, MySQL Group Replication, Redis Sentinel).
- Combine replication with load balancing so that if one replica fails, traffic is automatically redistributed to healthy replicas.

---

# 7.4 Indexing Strategies (Local, Global, Secondary)

> **Write short notes on: Local and Global Indexing [5 marks] (2081)**

An index is a data structure that provides fast access to rows in a table based on the values of one or more columns. Without an index, a query must scan the entire table (full table scan). With an index, the database can locate the relevant rows directly, similar to a book index that points to page numbers.

In partitioned databases, indexing becomes more complex because data is spread across multiple partitions. The way an index is structured relative to the table's partitions determines its query performance and maintenance characteristics.

## 7.4.1 Secondary Index

A secondary index is any index created on columns other than the primary key (or the partition key). The primary key index provides the default access path; secondary indexes provide alternative access paths for queries that filter or sort on non-primary-key columns.

Example: In a `Users` table partitioned by `user_id`, a secondary index on `email` allows efficient lookup by email address without scanning all partitions.

```sql
CREATE INDEX idx_users_email ON users(email);
```

In a partitioned database, secondary indexes must be implemented as either local or global.

## 7.4.2 Local Index (Document-Partitioned Index)

A local index is scoped to a single partition. Each partition maintains its own index that covers only the data stored within that partition. The local index is automatically partitioned in the same way as the table.

**How it works:** When data is written to a partition, only that partition's local index is updated. There is no cross-partition coordination for writes.

**Query behavior:** If a query includes the partition key, the database routes the query to the correct partition and uses its local index — this is very efficient. If the query does not include the partition key (e.g., searching by `email` across all users), the database must send the query to every partition, search each local index, and merge the results. This scatter-gather approach becomes expensive as the number of partitions grows.

```
Query: SELECT * FROM users WHERE email = 'x@y.com'
  → Partition 0: search local index → no match
  → Partition 1: search local index → found!
  → Partition 2: search local index → no match
  → Partition 3: search local index → no match
  → Merge results
```

**Advantages:**
- Writes are fast because only the local partition's index is updated.
- Partition maintenance (drop, archive) is simple because the index is co-located with the data.

**Disadvantages:**
- Cross-partition queries require scatter-gather, which increases latency.

## 7.4.3 Global Index (Term-Partitioned Index)

A global index spans the entire table, regardless of how the table is partitioned. The index itself may be partitioned (by the indexed term or a hash of it), but a single index entry can point to data in any table partition.

**How it works:** The global index is organized by the indexed column's values, not by the table's partition key. A lookup on the indexed column goes directly to the relevant portion of the global index, which provides a pointer to the exact partition and row.

**Query behavior:** Queries that do not include the table's partition key are efficient because the global index provides a direct lookup without scatter-gather.

```
Query: SELECT * FROM users WHERE email = 'x@y.com'
  → Global index on email: 'x@y.com' → Partition 1, Row 42
  → Fetch directly from Partition 1
```

**Advantages:**
- Reads on the indexed column are efficient; no scatter-gather needed.

**Disadvantages:**
- Writes are slower and more complex because inserting or updating a row may require updating index entries on a different node (the one holding the relevant portion of the global index).
- Partition maintenance (e.g., dropping a table partition) can invalidate global index entries, requiring an index rebuild.

**Local vs. Global Index Comparison:**

| Aspect | Local Index | Global Index |
|---|---|---|
| Scope | Per-partition | Across all partitions |
| Write Performance | Fast (local update only) | Slower (may update remote index partition) |
| Read (with partition key) | Fast | Fast |
| Read (without partition key) | Slow (scatter-gather) | Fast (direct lookup) |
| Partition Maintenance | Simple (co-located) | Complex (may need rebuild) |
| Best For | Partition-key queries, high write workloads | Cross-partition queries, read-heavy workloads |

**Design Decision (per Kleppmann, DDIA Ch. 6):** If the application's queries mostly include the partition key, local indexes are preferred because they keep writes fast. If the application frequently queries by non-partition-key columns, a global index avoids expensive scatter-gather at the cost of slower writes.

---

# 7.5 Monitoring and Performance Testing

Monitoring and performance testing are essential practices for maintaining and optimizing database systems in production. Monitoring provides continuous visibility into the database's health and behavior, while performance testing validates that the system can handle expected (and peak) workloads.

## 7.5.1 Database Monitoring

Database monitoring is the continuous, real-time observation of a database system's health, performance, and resource utilization. Its purpose is to detect problems early, prevent downtime, and provide data for capacity planning.

**Key Metrics to Monitor:**

1. **Query Performance Metrics:**
   - **Query Execution Time:** The time taken to parse, optimize, and execute a query. Consistently high values indicate missing indexes or inefficient queries.
   - **Slow Query Log:** A log of all queries exceeding a defined time threshold. Regularly reviewing this log helps identify candidates for optimization.
   - **Query Throughput (QPS/TPS):** The number of queries or transactions processed per second. A sudden drop may indicate a lock contention or resource exhaustion.

2. **Resource Utilization Metrics:**
   - **CPU Utilization:** High CPU may indicate complex query execution, excessive sorting, or inefficient joins.
   - **Memory Usage:** Monitors buffer pool and cache utilization. Insufficient memory forces the database to read from disk, degrading performance.
   - **Disk I/O:** Read/write throughput and latency. Disk I/O is often the primary bottleneck in database systems.
   - **Network I/O:** Data volume transferred between the database server and clients or replicas.

3. **Connection Metrics:**
   - **Active Connections:** The number of currently active client connections. Approaching the maximum connection limit can cause new requests to be rejected.
   - **Connection Pool Utilization:** The percentage of pooled connections in use. High utilization suggests the pool size needs to be increased or query times need to be reduced.

4. **Replication Metrics:**
   - **Replication Lag:** The delay between a write on the primary and its appearance on replicas. High lag means replicas are serving stale data.
   - **Replication Status:** Whether replicas are connected and in sync with the primary.

**Monitoring Tools:**

- **Built-in Tools:** PostgreSQL's `pg_stat_statements` and `pg_stat_activity`, MySQL's Performance Schema and slow query log.
- **Observability Platforms:** Datadog, New Relic, Grafana (with Prometheus) for dashboards, alerts, and historical analysis.
- **Database-Specific:** pgAdmin (PostgreSQL), MySQL Workbench, SolarWinds DPA.

## 7.5.2 Performance Testing

Performance testing evaluates how a database system behaves under specific workload conditions. It is typically performed before production deployment, after schema changes, or before expected traffic spikes.

**Types of Performance Tests:**

1. **Load Testing:** Simulates expected production workloads to verify that the system meets performance requirements (response time, throughput) under normal conditions.
2. **Stress Testing:** Pushes the system beyond normal capacity to identify the breaking point and observe how it degrades and recovers.
3. **Spike Testing:** Subjects the system to sudden, extreme increases in load to test auto-scaling and failover mechanisms.
4. **Endurance (Soak) Testing:** Runs the system under sustained load for an extended period to detect memory leaks, connection leaks, or gradual performance degradation.

**Performance Testing Methodology:**

1. **Establish a Baseline:** Monitor the system under normal load to determine baseline metrics (average query time, QPS, CPU usage). Any future deviation from this baseline signals a regression.
2. **Define Workload Profiles:** Model realistic workloads that reflect the actual read/write ratio, query mix, and concurrency levels of the application.
3. **Execute Tests:** Run the workload against the database using tools like `pgbench` (PostgreSQL), `sysbench` (MySQL), Apache JMeter, or `k6`.
4. **Analyze Results:** Compare measured metrics against requirements. Identify bottlenecks (e.g., a specific slow query, lock contention, insufficient buffer pool).
5. **Optimize and Re-test:** Apply optimizations (add indexes, rewrite queries, increase memory, partition tables) and re-run the test to verify improvement.

**Query Execution Plans:**

A critical tool for performance analysis is the query execution plan, generated using `EXPLAIN` (or `EXPLAIN ANALYZE` in PostgreSQL). It shows how the database engine executes a query — which indexes it uses, the join order, the estimated cost, and the actual time for each operation.

```sql
EXPLAIN ANALYZE
SELECT o.order_id, c.name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_date > '2024-01-01';
```

The output reveals whether the query uses an index scan or a sequential scan, and helps identify where to add indexes or restructure the query.
