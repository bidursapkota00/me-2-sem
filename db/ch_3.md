# 3. Advanced Relational Databases

# 3.1 Query Processing and Optimization

> **What is Query Optimization? Compare Cost-Based Optimization (CBO) with Rule-Based Optimization (RBO). How does the database engine use statistics to create an optimal execution plan? [8 marks] (2082)**

Query processing refers to the sequence of activities involved in extracting data from a database in response to a user query. The system transforms a high-level SQL query into an efficient low-level execution strategy.

**Steps of Query Processing:**

**1. Parsing and Translation:**

The SQL query is first checked for syntactic correctness. The parser verifies that relation names and attribute names are valid by consulting the system catalog (data dictionary). The query is then translated into an internal representation, typically a relational algebra expression. Views referenced in the query are replaced by their definitions during this step.

**2. Optimization:**

A single SQL query can be translated into many equivalent relational algebra expressions, each of which can be executed using different algorithms. The optimizer evaluates multiple candidate execution plans and selects the one with the lowest estimated cost. An execution plan (or query evaluation plan) specifies not only the order of operations but also the specific algorithm to be used for each operation (e.g., nested-loop join vs. merge join vs. hash join).

**3. Evaluation:**

The chosen execution plan is passed to the query execution engine, which coordinates the low-level operations (disk reads, filter applications, joins) and returns the result set to the user.

**Query Optimization Approaches:**

**Rule-Based Optimization (RBO):**

Rule-based optimization (also called heuristic optimization) uses a fixed set of predefined rules to transform the query into a more efficient form. These rules are applied regardless of the actual data in the database.

Common heuristic rules include:

1. **Perform selections early:** Push selection operations as far down the query tree as possible to reduce the size of intermediate results before expensive operations like joins.
2. **Perform projections early:** Remove unnecessary attributes as early as possible to reduce tuple width.
3. **Combine cascaded selections:** Multiple selection predicates on the same relation can be combined into a single selection using conjunction.
4. **Reorder joins:** Rearrange the order of joins to process smaller intermediate results first.

RBO is fast because it does not require statistical information, but it may not always produce the optimal plan because it ignores the actual distribution and size of data.

**Cost-Based Optimization (CBO):**

Cost-based optimization estimates the cost of each candidate execution plan and selects the plan with the lowest estimated cost. Cost is typically measured in terms of disk I/O operations, CPU time, and communication cost (in distributed systems).

The optimizer relies on statistical information stored in the system catalog:

1. **Number of tuples (n_r):** The total number of rows in a relation r.
2. **Number of blocks (b_r):** The number of disk blocks that contain tuples of relation r.
3. **Tuple size (l_r):** The average size of a tuple in relation r (in bytes).
4. **Number of distinct values (V(A, r)):** The number of distinct values for attribute A in relation r.
5. **Selection cardinality:** The estimated number of tuples satisfying a selection condition.
6. **Index statistics:** Height of index trees, number of leaf pages, and clustering information.

The optimizer uses these statistics to estimate the size of intermediate results and the cost of different algorithms. For example, for a join of two relations, the optimizer compares the cost of nested-loop join, merge join, and hash join, then selects the cheapest option.

Modern cost-based optimizers use dynamic programming to efficiently explore the space of possible join orderings and avoid evaluating every permutation.

**CBO vs. RBO:**

1. **Basis:** CBO uses statistical data about the actual database content. RBO uses fixed, predefined transformation rules.
2. **Accuracy:** CBO generally produces better plans because it considers data distribution. RBO may produce suboptimal plans when data characteristics differ from what the rules assume.
3. **Overhead:** CBO requires maintaining up-to-date statistics (using commands like `ANALYZE` or `UPDATE STATISTICS`). RBO has negligible optimization overhead.
4. **Adaptability:** CBO adapts to changes in data size and distribution. RBO applies the same transformations regardless of data changes.
5. **Usage:** Most modern DBMS (PostgreSQL, Oracle, MySQL) use CBO as the primary approach. RBO is used as a fallback or in combination with CBO for initial transformations.

**Measures of Query Cost:**

1. **Disk I/O cost:** Number of block transfers (reads/writes) between disk and memory. This is usually the dominant cost factor.
2. **CPU cost:** Time spent on in-memory operations such as comparisons, sorting, and hashing.
3. **Communication cost:** Time for data transfer over a network (relevant in distributed databases).

---

# 3.2 Advanced Indexing (B Trees, Hash Indexing, Bitmap Indexing)

> **Write algorithm for insertion in B+ Tree Index tree. Construct B+ tree of order 4 for the following set of keys: 2, 3, 5, 7, 11, 17, 19, 23, 29, 31. [7 marks] (2080)**
>
> **What are the limitations of static hashing in database systems? How does dynamic hashing address these limitations? [8 marks] (2081)**

An index is an auxiliary data structure that speeds up data retrieval by providing efficient access paths to records. Without an index, the database must perform a full table scan to find records matching a query condition.

**Types of Indexes:**

1. **Ordered Indexes:** Keep search keys in sorted order (e.g., B+ tree indexes).
2. **Hash Indexes:** Distribute search keys across buckets using a hash function.

## 3.2.1 B+ Tree Index

A B+ tree is a balanced, multi-level tree index structure that is the most widely used indexing method in database systems. It maintains sorted data and allows searches, insertions, deletions, and range queries in O(log n) time.

**Properties of a B+ Tree of Order n:**

1. Every node has at most n children (n-1 search keys).
2. Every non-root internal node has at least ⌈n/2⌉ children.
3. The root has at least 2 children if it is not a leaf.
4. All leaf nodes are at the same depth (the tree is balanced).
5. A leaf node holds between ⌈(n-1)/2⌉ and n-1 search key values.
6. Leaf nodes are linked together in a linked list for efficient sequential and range access.
7. Only leaf nodes contain pointers to actual data records. Internal nodes store only search keys and child pointers, serving as a multi-level sparse index.

**Node Structure:**

1. **Internal Node:** Contains search keys K1 < K2 < ... < Km and m+1 pointers P0, P1, ..., Pm. All keys in the subtree pointed to by Pi are between Ki and Ki+1.
2. **Leaf Node:** Contains search key values and pointers to corresponding data records. The last pointer in each leaf node points to the next leaf node in sequence.

**Search Algorithm:**

1. Start at the root node.
2. Within the current node, find the appropriate child pointer by comparing the search key with the keys in the node (using binary search or linear scan).
3. Follow the pointer to the next level.
4. Repeat until a leaf node is reached.
5. Search the leaf node for the key and return the associated record pointer if found.

**Insertion Algorithm:**

1. **Find the leaf:** Perform a search to locate the leaf node where the new key should be inserted.
2. **Insert if space exists:** If the leaf node has fewer than n-1 keys, insert the new key in sorted order. Done.
3. **Split if full:** If the leaf node is full (already has n-1 keys):
   - Create a temporary node with all n keys (existing n-1 plus the new key) in sorted order.
   - Split: the first ⌈n/2⌉ keys remain in the original node, the remaining keys go to a new leaf node.
   - Copy up the smallest key of the new node to the parent as a separator.
   - Link the new leaf node into the leaf linked list.
4. **Propagate splits:** If the parent internal node is also full after inserting the new separator:
   - Split the internal node similarly: the first ⌈n/2⌉-1 keys stay, the middle key is pushed up to the parent, and the remaining keys go to a new internal node.
   - Repeat upward as needed.
5. **New root:** If the root splits, create a new root with the pushed-up key and two children. The tree height increases by one.

**Example: B+ Tree of Order 4 for Keys 2, 3, 5, 7, 11, 17, 19, 23, 29, 31**

Order 4 means each node can hold at most 3 keys and 4 pointers. A leaf must have at least ⌈3/2⌉ = 2 keys.

Step-by-step construction:

1. Insert 2, 3, 5: Leaf = [2, 3, 5] (full).
2. Insert 7: Leaf overflows. Split: [2, 3] and [5, 7]. Push 5 up to root. Root = [5].
3. Insert 11: Goes to right leaf [5, 7, 11] (full).
4. Insert 17: Right leaf overflows. Split [5, 7] and [11, 17]. Push 11 up. Root = [5, 11].
5. Insert 19: Goes to [11, 17, 19] (full).
6. Insert 23: Overflows. Split [11, 17] and [19, 23]. Push 19 up. Root = [5, 11, 19].
7. Insert 29: Goes to [19, 23, 29] (full).
8. Insert 31: Overflows. Split [19, 23] and [29, 31]. Push 29 up. Root overflows [5, 11, 19, 29]. Split root: left internal = [5], right internal = [19, 29], push 11 up as new root.

Final structure:

```
                   [11]
                  /    \
             [5]        [19, 29]
            /   \      /   |    \
        [2,3] [5,7] [11,17] [19,23] [29,31]
```

All leaf nodes are linked: [2,3] → [5,7] → [11,17] → [19,23] → [29,31].

**Deletion in B+ Tree:**

1. Find the leaf node containing the key.
2. Remove the key from the leaf.
3. If the leaf still has at least ⌈(n-1)/2⌉ keys, done.
4. If the leaf underflows, borrow a key from a sibling (if the sibling has more than the minimum). Update the separator key in the parent.
5. If no sibling can lend, merge the leaf with a sibling and remove the separator from the parent. If the parent underflows, propagate the merge upward.

## 3.2.2 Hash Indexing

Hash indexing uses a hash function to map search key values directly to bucket addresses, providing O(1) average-case lookup for equality queries. A bucket is a unit of storage (typically a disk block or group of blocks) that holds records.

**Static Hashing:**

In static hashing, the number of buckets B is fixed at the time of file creation. A hash function h maps each search key value K to a bucket address in the range {0, 1, ..., B-1}.

**Limitations of Static Hashing:**

1. **Fixed bucket count:** The number of buckets cannot change after creation. If the database grows significantly, the fixed number of buckets becomes insufficient, leading to long overflow chains.
2. **Bucket overflow:** When a bucket is full, overflow buckets are chained using linked lists (overflow chaining). As chains grow, lookup time degrades from O(1) toward O(n).
3. **Wasted space:** If the number of buckets is chosen too large for a small database, significant space is wasted on empty or partially filled buckets.
4. **Expensive reorganization:** To resize the hash table, a complete reorganization is required. All existing records must be rehashed with a new function and redistributed, which is very costly and disrupts normal database operations.
5. **Skew:** If the hash function does not distribute keys uniformly, some buckets receive disproportionately more records, creating hotspots.

**Dynamic Hashing (Extendable Hashing):**

Dynamic hashing allows the hash structure to grow and shrink dynamically as the database changes, avoiding periodic reorganization.

**Extendable Hashing:**

Extendable hashing uses a directory of pointers to buckets. The hash function produces a value of b bits (e.g., 32 bits), but only a prefix of these bits is used to index into the directory.

1. **Global Depth (d):** The number of bits of the hash value currently used to index the directory. The directory has 2^d entries.
2. **Local Depth (d_i):** Stored with each bucket, indicating how many bits of the hash value determine that bucket's contents.
3. **Lookup:** Compute h(K), take the first d bits, and use them to index the directory. Follow the pointer to the appropriate bucket.
4. **Insertion:** If the target bucket has space, insert. If the bucket overflows:
   - If local depth < global depth: split the bucket, increment local depth, and update directory pointers. No directory growth needed.
   - If local depth = global depth: double the directory (increment global depth), then split the bucket and update pointers.
5. **Advantages:** Only one bucket is split at a time (no full reorganization). Performance remains near O(1) for lookups.
6. **Disadvantages:** Adds an extra level of indirection (directory lookup). If the directory grows too large to fit in memory, an extra disk access is needed.

**Linear Hashing:**

Linear hashing is another dynamic hashing scheme that does not require a directory. Buckets are split in a predetermined linear order (not necessarily the bucket that overflowed), and overflow chains are used temporarily until the overflowing bucket is eventually split. It avoids the directory overhead of extendable hashing.

## 3.2.3 Bitmap Indexing

A bitmap index uses bit arrays (bitmaps) to represent the presence or absence of a column value for each row in a table. For each distinct value v of an indexed column, a separate bitmap is created where the i-th bit is 1 if the i-th row has value v, and 0 otherwise.

**Example:**

For a table with 8 rows and a "Gender" column with values {M, F}:

```
Row:      1  2  3  4  5  6  7  8
Gender:   M  F  M  M  F  M  F  M

Bitmap for M: 1  0  1  1  0  1  0  1
Bitmap for F: 0  1  0  0  1  0  1  0
```

**Advantages:**

1. **Space efficient:** Extremely compact for low-cardinality columns (columns with few distinct values such as gender, status, boolean flags).
2. **Fast multi-condition queries:** Complex WHERE clauses with multiple conditions are resolved by performing bitwise operations (AND, OR, NOT) on the corresponding bitmaps. These are CPU-native operations and execute extremely fast.
3. **Efficient COUNT operations:** Counting rows that match a condition simply requires counting the number of 1-bits in the resulting bitmap.
4. **Ideal for OLAP:** Particularly effective in data warehousing and analytical workloads where queries involve ad-hoc filtering across multiple dimensions.

**Disadvantages:**

1. **Poor write performance:** Insert, update, and delete operations require modifying multiple bitmaps and can cause locking and concurrency issues. Not suitable for OLTP workloads with frequent writes.
2. **Inefficient for high-cardinality columns:** When the number of distinct values is large (e.g., primary keys, timestamps), the number of bitmaps becomes very large and mostly sparse, negating the space advantage.
3. **Overhead for small tables:** The per-row bitmap infrastructure adds unnecessary overhead when the table has very few rows.

**Bitwise Query Example:**

Query: Find all male employees who are active.

```
Bitmap for Gender=M:    1 0 1 1 0 1 0 1
Bitmap for Status=Active: 1 1 0 1 0 1 1 0

AND result:             1 0 0 1 0 1 0 0
```

Rows 1, 4, and 6 satisfy both conditions.

---

# 3.3 Materialized Views and Caching Strategies

> **How does a materialized view differ from a standard (regular) view in a database? Explain materialized views and caching strategies in detail. [7 marks] (2081)**
>
> **In a university database, how can you efficiently get the total salary paid to instructors in each department without recalculating the sum every time? Write necessary SQL queries to create, refresh, and view for this purpose. [7 marks] (2080)**

## 3.3.1 Views

A view is a virtual relation defined by a query expression. It does not store data physically. Every time a view is accessed, the underlying query is re-executed against the current state of the base tables.

```sql
CREATE VIEW faculty AS
SELECT ID, name, dept_name
FROM Instructor;
```

When a user queries the view `SELECT * FROM faculty WHERE dept_name = 'Physics'`, the DBMS internally replaces `faculty` with the view definition and executes the combined query against the base Instructor table.

## 3.3.2 Materialized Views

A materialized view is a database object that stores the result of a query physically on disk. Unlike a regular view, accessing a materialized view does not require re-executing the underlying query. The precomputed results are read directly, providing significantly faster access for complex aggregation and join queries.

**Creation:**

```sql
CREATE MATERIALIZED VIEW dept_salary_summary AS
SELECT dept_name, SUM(salary) AS total_salary, COUNT(*) AS num_instructors
FROM Instructor
GROUP BY dept_name;
```

**Querying:**

```sql
SELECT * FROM dept_salary_summary;
```

This returns the precomputed totals instantly without scanning the entire Instructor table.

**Materialized View vs. Standard View:**

1. **Data Storage:** A standard view stores only the query definition. A materialized view stores both the query definition and the computed result set.
2. **Performance:** A standard view recomputes results on every access. A materialized view returns precomputed results, which is much faster for complex queries.
3. **Data Freshness:** A standard view always reflects the current base table data. A materialized view may contain stale data if the base tables have been modified since the last refresh.
4. **Storage Cost:** A standard view consumes no extra storage. A materialized view requires disk space proportional to the query result size.
5. **Maintenance:** A standard view requires no maintenance. A materialized view must be periodically refreshed to stay current.

**Refresh Strategies:**

1. **Immediate (Eager) Refresh:** The materialized view is updated as part of the same transaction that modifies the base tables. This guarantees that the view is always current but adds overhead to every update transaction.

2. **Deferred (Lazy) Refresh:** The update is performed on a schedule (e.g., nightly) or on demand. This reduces the overhead on update transactions but means the view may be temporarily out of date.

3. **Incremental Maintenance:** Instead of recomputing the entire view from scratch, only the changes (deltas) to the base tables are applied to the view. This is much more efficient for views over large tables with small update volumes.

4. **Full Recomputation:** The entire view is dropped and recomputed from the base tables. This is simpler but expensive for large views.

**Refresh SQL Example (PostgreSQL):**

```sql
-- Manual refresh
REFRESH MATERIALIZED VIEW dept_salary_summary;

-- View the refreshed data
SELECT * FROM dept_salary_summary
WHERE total_salary > 500000;
```

**When to Use Materialized Views:**

1. Frequently executed expensive queries involving aggregations, joins, or complex calculations.
2. Data warehouse environments where base tables are updated in batch and the view can be refreshed after each batch.
3. Summary tables for dashboards and reporting where real-time accuracy is not critical.

## 3.3.3 Caching Strategies

Caching in the context of databases refers to storing frequently accessed data in a faster storage layer (typically main memory) to reduce the number of expensive disk I/O operations.

**Database Buffer Cache:**

The DBMS maintains a buffer pool in main memory. When a page (block) of data is read from disk, it is stored in the buffer pool. Subsequent requests for the same page are served from memory rather than disk. The buffer manager uses replacement policies (such as LRU, or Least Recently Used) to decide which pages to evict when the buffer pool is full.

**Application-Level Caching:**

In modern architectures, an in-memory caching layer (such as Redis or Memcached) is placed between the application and the database. Frequently queried results are stored in the cache. The application checks the cache first and only queries the database on a cache miss.

**Cache Invalidation Strategies:**

1. **Time-To-Live (TTL):** Cached entries automatically expire after a fixed duration. Simple to implement but may serve stale data within the TTL window.
2. **Write-Through:** Every write to the database also updates the cache immediately. Ensures cache consistency but adds latency to write operations.
3. **Write-Behind (Write-Back):** Writes are made to the cache first and asynchronously propagated to the database. Provides low write latency but risks data loss if the cache fails before propagation.
4. **Cache-Aside (Lazy Loading):** The application manages the cache manually. On a miss, it reads from the database, stores the result in the cache, and returns it. On a write, it updates the database and invalidates or updates the cache entry.

---

# 3.4 Stored Procedures, Triggers, and UDFs

> **Define trigger and its role in maintaining data integrity. How can trigger be utilized to enforce constraint "A reviewer can review a maximum of 5 papers"? [7 marks] (2080)**
>
> **Define stored procedure. How can we create parameterized stored procedure? Explain with necessary syntax and example. [7 marks] (2080)**

## 3.4.1 Stored Procedures

A stored procedure is a named block of precompiled SQL and procedural statements stored in the database. It encapsulates complex business logic, can accept input and output parameters, and is invoked explicitly by the application using a CALL statement.

**Advantages:**

1. **Reduced network traffic:** Instead of sending multiple SQL statements from the application, a single CALL to a stored procedure executes the logic on the database server.
2. **Code reuse:** The same procedure can be called from multiple applications without duplicating logic.
3. **Security:** Users can be granted permission to execute a procedure without granting direct access to the underlying tables.
4. **Performance:** Stored procedures are precompiled and their execution plans are cached, reducing parsing and optimization overhead on repeated calls.

**Syntax (Standard SQL / PostgreSQL):**

```sql
CREATE OR REPLACE PROCEDURE transfer_funds(
    IN sender_id INT,
    IN receiver_id INT,
    IN amount DECIMAL(10,2)
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Debit the sender
    UPDATE Account SET balance = balance - amount
    WHERE account_id = sender_id;

    -- Credit the receiver
    UPDATE Account SET balance = balance + amount
    WHERE account_id = receiver_id;

    COMMIT;
END;
$$;
```

**Calling a Stored Procedure:**

```sql
CALL transfer_funds(101, 202, 5000.00);
```

**Parameterized Stored Procedure:**

Parameters allow stored procedures to accept dynamic input values. There are three parameter modes:

1. **IN:** Input parameter. The caller passes a value to the procedure. This is the default mode.
2. **OUT:** Output parameter. The procedure sets a value that the caller can read after execution.
3. **INOUT:** Bidirectional parameter. The caller passes an initial value, and the procedure can modify it.

```sql
CREATE OR REPLACE PROCEDURE get_dept_stats(
    IN p_dept_name VARCHAR(50),
    OUT p_total_salary DECIMAL(12,2),
    OUT p_count INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT SUM(salary), COUNT(*)
    INTO p_total_salary, p_count
    FROM Instructor
    WHERE dept_name = p_dept_name;
END;
$$;
```

**Calling with OUT parameters:**

```sql
CALL get_dept_stats('Computer Science', NULL, NULL);
```

## 3.4.2 Triggers

A trigger is a special database object that automatically executes (fires) a specified block of code in response to a particular event (INSERT, UPDATE, or DELETE) on a specified table. Triggers are event-driven and are never called explicitly by the application.

**Components of a Trigger:**

1. **Event:** The database operation that activates the trigger (INSERT, UPDATE, DELETE).
2. **Condition:** An optional boolean condition that must be true for the trigger body to execute (specified using a WHEN clause).
3. **Action:** The block of SQL or procedural code that is executed when the trigger fires.
4. **Timing:** Specifies whether the trigger fires BEFORE or AFTER the triggering event.
5. **Granularity:** FOR EACH ROW (fires once per affected row) or FOR EACH STATEMENT (fires once per SQL statement, regardless of how many rows are affected).

**OLD and NEW References:**

1. **NEW:** Refers to the new row being inserted or the updated values in an UPDATE operation.
2. **OLD:** Refers to the row being deleted or the original values before an UPDATE.

**Syntax:**

```sql
CREATE TRIGGER trigger_name
{BEFORE | AFTER} {INSERT | UPDATE | DELETE}
ON table_name
FOR EACH ROW
[WHEN (condition)]
BEGIN
    -- trigger body
END;
```

**Example: Enforce "A reviewer can review a maximum of 5 papers"**

Given a Reviews(reviewer_id, paper_id) table:

```sql
CREATE OR REPLACE FUNCTION check_review_limit()
RETURNS TRIGGER AS $$
DECLARE
    review_count INT;
BEGIN
    SELECT COUNT(*) INTO review_count
    FROM Reviews
    WHERE reviewer_id = NEW.reviewer_id;

    IF review_count >= 5 THEN
        RAISE EXCEPTION 'Reviewer % has already reviewed 5 papers',
            NEW.reviewer_id;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER enforce_review_limit
BEFORE INSERT ON Reviews
FOR EACH ROW
EXECUTE FUNCTION check_review_limit();
```

When an INSERT on Reviews is attempted, the trigger fires before the insertion. It counts the number of existing reviews by the same reviewer. If the count is already 5, the trigger raises an exception and the insert is rejected. Otherwise, RETURN NEW allows the insert to proceed.

**Role of Triggers in Data Integrity:**

1. **Enforce complex constraints:** Triggers can enforce business rules that cannot be expressed using standard CHECK, UNIQUE, or FOREIGN KEY constraints (e.g., cross-table constraints, count limits).
2. **Maintain derived data:** Triggers can automatically update summary tables or materialized views when base data changes.
3. **Audit logging:** Triggers can record changes to an audit table, capturing who changed what and when.
4. **Cascading actions:** Triggers can propagate changes to related tables when certain events occur.

## 3.4.3 User-Defined Functions (UDFs)

A user-defined function is a named routine stored in the database that accepts parameters, performs a computation, and returns a value. Unlike stored procedures, functions return a value and can be used directly within SQL expressions (e.g., in SELECT, WHERE, or ORDER BY clauses).

**Syntax:**

```sql
CREATE OR REPLACE FUNCTION get_department_budget(p_dept VARCHAR)
RETURNS DECIMAL(12,2)
LANGUAGE plpgsql
AS $$
DECLARE
    total DECIMAL(12,2);
BEGIN
    SELECT SUM(salary) INTO total
    FROM Instructor
    WHERE dept_name = p_dept;

    RETURN COALESCE(total, 0);
END;
$$;
```

**Using the Function in a Query:**

```sql
SELECT dept_name, get_department_budget(dept_name) AS budget
FROM Department;
```

**Stored Procedure vs. User-Defined Function:**

1. **Return value:** A function must return a value (scalar or table). A procedure does not return a value directly (it uses OUT parameters or result sets).
2. **Usage in SQL:** A function can be called from within a SELECT, WHERE, or other SQL expression. A procedure must be invoked using a CALL statement.
3. **Side effects:** Functions are generally expected to be free of side effects (no data modification). Procedures are designed to perform data modifications and transaction control.
4. **Transaction control:** Procedures can contain COMMIT and ROLLBACK statements. Functions typically cannot.
