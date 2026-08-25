# 6. Big Data & Modern Database Technologies

# 6.1 Hadoop Ecosystem (HDFS, MapReduce)

> **Explain the architecture of HDFS. How is Read and Write performed in HDFS? [7 marks] (2080)**
>
> **Explain the working principles of the MapReduce programming model. Discuss the roles of the Map and Reduce functions in distributed data processing, and illustrate your explanation with a real-world use case. [7 marks] (2081)**

## 6.1.1 Hadoop Overview

Apache Hadoop is an open-source framework for distributed storage and processing of large datasets across clusters of commodity hardware. It was designed to scale from single servers to thousands of machines, each offering local computation and storage. Hadoop provides fault tolerance by replicating data and re-executing failed tasks.

**Core Components of Hadoop:**

1. **HDFS (Hadoop Distributed File System):** The storage layer that distributes files across cluster nodes.
2. **MapReduce:** The processing framework that enables parallel computation across the cluster.
3. **YARN (Yet Another Resource Negotiator):** The resource management layer that schedules jobs and allocates cluster resources.

## 6.1.2 HDFS Architecture

HDFS follows a master-slave architecture designed for storing very large files (gigabytes to petabytes) with a write-once, read-many access pattern. It prioritizes high throughput over low latency.

**Components:**

**NameNode (Master):**
- Manages the file system namespace — the directory tree, file permissions, and file-to-block mapping.
- Stores metadata only, not actual file data.
- Maintains a record of which blocks belong to which file and which DataNodes store each block.
- Monitors DataNode health through periodic heartbeat signals. If a DataNode fails to send heartbeats, the NameNode marks it as dead and re-replicates its blocks to other healthy nodes.
- The NameNode is a single point of failure. In production, a Secondary NameNode or Standby NameNode (HA mode) is configured for fault tolerance.

**DataNode (Slave):**
- Stores actual data blocks on local disk.
- Serves read and write requests directly from clients.
- Sends periodic heartbeats and block reports to the NameNode.
- There are typically many DataNodes in a cluster (hundreds to thousands).

**Blocks and Replication:**

Files in HDFS are split into fixed-size blocks (default: 128 MB). Each block is replicated across multiple DataNodes for fault tolerance. The default replication factor is 3.

**Rack-Aware Replica Placement Policy:**
- First replica: on the same node as the writer (or a random node if the writer is not a DataNode).
- Second replica: on a different rack.
- Third replica: on a different node in the same rack as the second replica.

This balances reliability (data survives a rack failure) with network bandwidth (intra-rack copies are fast).

**HDFS Read Operation:**

```
Client                  NameNode                DataNodes
  |                        |                       |
  |--- Open file --------->|                       |
  |<-- Block locations ----|                       |
  |                        |                       |
  |--- Read Block 1 ------------------------------>| (nearest DataNode)
  |<-- Data stream --------------------------------|
  |                        |                       |
  |--- Read Block 2 ------------------------------>| (nearest DataNode)
  |<-- Data stream --------------------------------|
  |                        |                       |
  |--- Close file -------->|                       |
```

1. The client contacts the NameNode with the filename.
2. The NameNode returns the list of DataNodes that store each block of the file, sorted by proximity to the client.
3. The client connects directly to the nearest DataNode holding the first block and reads the data as a stream.
4. After reading the first block, the client moves to the next block (which may be on a different DataNode) and repeats.
5. The client closes the connection when all blocks have been read. The NameNode is not involved in data transfer.

**HDFS Write Operation:**

```
Client                  NameNode                DataNodes
  |                        |                       |
  |--- Create file ------->|                       |
  |<-- OK + DN list -------|                       |
  |                        |                       |
  |--- Write Block 1 (pipeline) ------------------>| DN1
  |                        |                  DN1 ->| DN2
  |                        |             DN2 ----->| DN3
  |<-- ACK from pipeline -------------------------------|
  |                        |                       |
  |--- Close file -------->|                       |
  |                (NameNode commits metadata)      |
```

1. The client asks the NameNode to create a new file. The NameNode checks permissions and verifies the file does not already exist.
2. The client receives a list of DataNodes for the replication pipeline.
3. The client splits data into blocks and writes each block to the first DataNode (DN1).
4. DN1 receives the data, stores it locally, and forwards it to DN2. DN2 stores it and forwards to DN3 (pipeline replication).
5. Acknowledgments (ACKs) flow back through the pipeline: DN3 → DN2 → DN1 → Client.
6. After all blocks are written, the client closes the file. The NameNode commits the file's metadata (block locations) to its persistent log.

## 6.1.3 MapReduce

MapReduce is a programming model and processing framework for parallel computation on large datasets distributed across a Hadoop cluster. It divides work into two phases — Map and Reduce — that execute in parallel across the cluster.

**How MapReduce Works:**

**Phase 1: Map**
- The input data is split into fixed-size chunks called input splits. Each split is assigned to a mapper task.
- The Map function processes each input split and produces intermediate key-value pairs.
- Mappers run independently and in parallel across different nodes.

**Phase 2: Shuffle and Sort**
- The framework automatically collects all intermediate key-value pairs from all mappers.
- It sorts and groups them by key so that all values associated with the same key are collected together.
- The grouped data is sent to the appropriate reducer.

**Phase 3: Reduce**
- The Reduce function receives a key and the list of all values associated with that key.
- It aggregates, summarizes, or transforms the values and produces the final output key-value pairs.
- The output is written to HDFS.

**MapReduce Execution Flow:**

```
Input Data → [Split 1] → Mapper 1 → (key, value) pairs ─┐
             [Split 2] → Mapper 2 → (key, value) pairs ──┤ Shuffle
             [Split 3] → Mapper 3 → (key, value) pairs ──┘ & Sort
                                                            │
                                    ┌───────────────────────┘
                                    ↓
                          (key, [values]) → Reducer 1 → Output 1
                          (key, [values]) → Reducer 2 → Output 2
```

**Real-World Example: Word Count**

Given input files containing text, count the frequency of each word across all files.

**Input:**

```
File 1: "hello world hello"
File 2: "world hello hadoop"
```

**Map Phase:**

Each mapper processes one file and emits (word, 1) for each word:

```
Mapper 1 output: (hello, 1), (world, 1), (hello, 1)
Mapper 2 output: (world, 1), (hello, 1), (hadoop, 1)
```

**Shuffle and Sort Phase:**

The framework groups values by key:

```
(hadoop, [1])
(hello, [1, 1, 1])
(world, [1, 1])
```

**Reduce Phase:**

Each reducer sums the values for its assigned keys:

```
Reducer output: (hadoop, 1), (hello, 3), (world, 2)
```

**Word Count Pseudocode:**

```
// Map Function
function map(key: docId, value: document):
    for each word in document:
        emit(word, 1)

// Reduce Function
function reduce(key: word, values: list of counts):
    total = sum(values)
    emit(word, total)
```

**Real-World Use Case: Log Analysis**

A web company has terabytes of server log files distributed across its cluster. Using MapReduce:
- **Map:** Each mapper processes one log file. For each log line, it extracts the URL and emits (URL, 1).
- **Shuffle:** The framework groups all counts by URL.
- **Reduce:** Each reducer sums the counts per URL, producing the total number of hits per page.

This computation runs in parallel across hundreds of nodes, processing terabytes of logs in minutes.

**Advantages of MapReduce:**
- Automatically parallelizes across the cluster.
- Handles fault tolerance — if a mapper or reducer fails, the task is re-executed on another node.
- Scalable — adding more nodes increases processing capacity linearly.

**Limitations of MapReduce:**
- High disk I/O — intermediate results are written to disk between Map and Reduce phases.
- Not suitable for iterative algorithms (e.g., machine learning) that require multiple passes over the data.
- Higher latency compared to in-memory frameworks like Apache Spark.

---

# 6.2 Apache Spark (RDDs, DataFrames, Spark SQL)

Apache Spark is a unified analytics engine for large-scale distributed data processing. It was designed to address the limitations of MapReduce — particularly its high disk I/O overhead — by performing computation in memory. Spark is up to 100x faster than Hadoop MapReduce for in-memory processing.

## 6.2.1 Spark Architecture

Spark follows a driver-executor architecture:

**Driver Program:**
- The process where the main application (SparkSession) runs.
- Converts user code into a Directed Acyclic Graph (DAG) of tasks.
- Schedules tasks across executors on the cluster.
- Collects results and returns them to the user.

**Executors:**
- Worker processes running on cluster nodes.
- Execute the tasks assigned by the driver.
- Store data in memory or disk for caching.
- Report results back to the driver.

**Cluster Manager:**
- An external service that allocates resources (CPU, memory) to the Spark application.
- Supported cluster managers: YARN, Kubernetes, Mesos, Spark Standalone.

```
                  [Driver Program]
                 (SparkSession, DAG)
                   /      |      \
          [Executor 1] [Executor 2] [Executor 3]
          (Worker Node) (Worker Node) (Worker Node)
                        |
                 [Cluster Manager]
              (YARN / Kubernetes / Mesos)
```

## 6.2.2 RDD (Resilient Distributed Dataset)

An RDD is the fundamental, low-level data abstraction in Spark. It is an immutable, fault-tolerant, distributed collection of objects that can be processed in parallel.

**Properties of RDDs:**

1. **Immutable:** Once created, an RDD cannot be modified. Transformations create new RDDs.
2. **Distributed:** Data is partitioned across multiple nodes in the cluster.
3. **Fault-Tolerant:** If a partition is lost (node failure), Spark reconstructs it by replaying the sequence of transformations (lineage) that produced it. This is more efficient than data replication.
4. **Lazy Evaluation:** Transformations on RDDs are not executed immediately. Spark records them in a DAG and executes them only when an action is called.

**Creating RDDs:**

```python
from pyspark import SparkContext
sc = SparkContext("local", "Example")

# From a collection
rdd = sc.parallelize([1, 2, 3, 4, 5])

# From a file
rdd = sc.textFile("hdfs:///data/logs.txt")
```

**Transformations (Lazy):**

Transformations create a new RDD from an existing one. They are not executed immediately — Spark builds a DAG of operations.

```python
# filter: keep only even numbers
evens = rdd.filter(lambda x: x % 2 == 0)

# map: square each number
squares = rdd.map(lambda x: x ** 2)

# flatMap: split lines into words
words = lines_rdd.flatMap(lambda line: line.split(" "))

# reduceByKey: aggregate values by key
word_counts = pairs_rdd.reduceByKey(lambda a, b: a + b)
```

**Actions (Eager):**

Actions trigger the execution of the DAG and return results to the driver or write to storage.

```python
# collect: return all elements to the driver
result = evens.collect()          # [2, 4]

# count: return the number of elements
n = rdd.count()                   # 5

# reduce: aggregate all elements
total = rdd.reduce(lambda a, b: a + b)  # 15

# saveAsTextFile: write to HDFS
rdd.saveAsTextFile("hdfs:///output/result")
```

**Word Count in Spark (RDD):**

```python
text_rdd = sc.textFile("hdfs:///data/books.txt")

word_counts = (text_rdd
    .flatMap(lambda line: line.split(" "))
    .map(lambda word: (word, 1))
    .reduceByKey(lambda a, b: a + b))

word_counts.saveAsTextFile("hdfs:///output/counts")
```

## 6.2.3 DataFrames

A DataFrame is a higher-level, structured API built on top of RDDs. It organizes data into named columns, similar to a table in a relational database. DataFrames use the Catalyst optimizer and Tungsten execution engine for automatic query optimization.

**Advantages over RDDs:**
- Higher-level API — more concise and readable code.
- Automatic optimization via the Catalyst query optimizer.
- Support for SQL queries via Spark SQL.
- Better performance due to Tungsten's efficient memory management.

**Creating DataFrames:**

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Example").getOrCreate()

# From a JSON file
df = spark.read.json("hdfs:///data/students.json")

# From a CSV file
df = spark.read.csv("hdfs:///data/students.csv", header=True, inferSchema=True)

# From an RDD
rdd = sc.parallelize([("Ram", 25, "CS"), ("Sita", 24, "IT")])
df = rdd.toDF(["name", "age", "department"])
```

**DataFrame Operations:**

```python
# Show the first 5 rows
df.show(5)

# Select specific columns
df.select("name", "department").show()

# Filter rows
df.filter(df.age > 23).show()

# Group by and aggregate
df.groupBy("department").count().show()

# Add a new column
df.withColumn("senior", df.age > 25).show()

# Order by
df.orderBy(df.age.desc()).show()
```

## 6.2.4 Spark SQL

Spark SQL allows running SQL queries directly on DataFrames. It provides a familiar SQL interface for data analysts and integrates with Hive for access to existing data warehouses.

```python
# Register DataFrame as a temporary SQL view
df.createOrReplaceTempView("students")

# Run SQL queries
result = spark.sql("""
    SELECT department, AVG(age) AS avg_age, COUNT(*) AS total
    FROM students
    WHERE age > 20
    GROUP BY department
    ORDER BY avg_age DESC
""")

result.show()
```

**Spark SQL can also read from external databases:**

```python
jdbc_df = spark.read.format("jdbc") \
    .option("url", "jdbc:postgresql://host:5432/mydb") \
    .option("dbtable", "employees") \
    .option("user", "admin") \
    .option("password", "pass") \
    .load()
```

**MapReduce vs. Spark:**

1. **Processing:** MapReduce writes intermediate results to disk. Spark keeps data in memory (up to 100x faster).
2. **Ease of Use:** MapReduce requires verbose Java code. Spark provides concise APIs in Python, Scala, Java, and R.
3. **Iterative Processing:** MapReduce restarts the entire job for each iteration. Spark caches intermediate data in memory, making iterative algorithms (ML, graph processing) much faster.
4. **Real-Time Processing:** MapReduce is batch-only. Spark supports batch, streaming (Spark Streaming), and interactive queries.
5. **DAG Execution:** MapReduce has a rigid Map→Reduce pipeline. Spark uses a flexible DAG that can combine multiple transformations before execution.

---

# 6.3 Time-Series Databases and Its Implementation

> **Explain the concept of Time-Series Databases. How do they optimize storage for high-velocity telemetry data compared to a standard Relational DBMS? [7 marks] (2082)**

A time-series database (TSDB) is a database system optimized for storing, retrieving, and analyzing time-stamped data — data points that are recorded sequentially over time. Each data point typically consists of a timestamp, a metric name (or tag), and a value.

**Characteristics of Time-Series Data:**

1. **Time-Ordered:** Data is naturally ordered by timestamp. Queries almost always involve time ranges.
2. **Append-Heavy:** New data points are continuously appended. Updates and deletes are rare.
3. **High Volume:** Telemetry systems can generate millions of data points per second (e.g., IoT sensors, server metrics, financial ticks).
4. **Recent Data is Most Valuable:** Queries predominantly access recent data. Older data is accessed less frequently and can be aggregated or archived.

**Examples of Time-Series Data:**

- Server CPU usage every 10 seconds.
- IoT sensor readings (temperature, humidity) every minute.
- Stock prices every millisecond.
- Application response time metrics.

**How TSDBs Optimize Storage Compared to Relational DBMS:**

**1. Columnar Storage:**

TSDBs store data in columnar format rather than row-based format. Since time-series queries typically access a few columns (e.g., timestamp and value) across many rows, columnar storage reads only the required columns, drastically reducing disk I/O. In a relational DBMS, row-based storage reads entire rows even if only one column is needed.

**2. Time-Based Partitioning:**

TSDBs automatically partition data into time-based chunks (e.g., one chunk per hour or per day). This provides several benefits:
- Range queries on time windows only scan the relevant chunks, not the entire table.
- Dropping expired data is instantaneous — simply delete the entire chunk instead of scanning and deleting individual rows.
- In a relational DBMS, deleting old data requires expensive DELETE operations with full table scans.

**3. Specialized Compression:**

Time-series data has high redundancy — timestamps are sequential, and values often change slowly. TSDBs exploit these patterns:
- **Delta-of-delta encoding for timestamps:** Instead of storing absolute timestamps, store the difference between consecutive differences. Sequential timestamps (e.g., every 10s) compress to near-zero storage.
- **XOR encoding for values:** Float values that change slowly are XOR-encoded, storing only the bits that differ between consecutive values.
- **Run-length encoding:** Repeated identical values are stored as (value, count).
- **Dictionary encoding for tags:** Repeated string tags (e.g., "cpu", "memory") are stored as integer codes.

TSDBs achieve 90-95% compression ratios. A relational DBMS uses general-purpose compression (e.g., TOAST in PostgreSQL) that is far less efficient for time-series patterns.

**4. Downsampling and Retention Policies:**

TSDBs provide built-in mechanisms to automatically aggregate older high-resolution data into lower-resolution summaries (e.g., converting per-second data to per-hour averages after 7 days). Retention policies automatically delete data older than a configured duration. These features are absent in standard relational DBMS.

**5. Write-Optimized Ingestion:**

TSDBs use append-only write paths optimized for sequential writes. Many use Log-Structured Merge Trees (LSM trees) or similar structures that batch writes in memory and flush to disk sequentially, achieving very high write throughput. A relational DBMS with B-tree indexes incurs random I/O on every insert and must maintain index consistency.

**Example Implementation with InfluxDB:**

```
// Write data points using InfluxDB Line Protocol
cpu,host=server01,region=us-east usage=72.5 1693000000000000000
cpu,host=server01,region=us-east usage=68.3 1693000010000000000
cpu,host=server02,region=eu-west usage=45.2 1693000000000000000

// Query: Average CPU usage per host in the last hour
SELECT MEAN(usage) FROM cpu
WHERE time > now() - 1h
GROUP BY host
```

**Popular Time-Series Databases:** InfluxDB, TimescaleDB (PostgreSQL extension), Prometheus, QuestDB, Amazon Timestream.

---

# 6.4 Blockchain Databases (Decentralized Storage)

> **Explain the concept of a blockchain database and how it provides decentralized storage and immutability. Illustrate with an example how transactions are recorded and verified in a blockchain-based database system. [8 marks] (2082)**
>
> **Explain the working mechanism of blockchain technology with appropriate illustrations. Why is a blockchain-based database considered more secure than traditional centralized database systems? [7 marks] (2081)**
>
> **Write short notes on: Blockchain Database [5 marks] (2080)**

## 6.4.1 Blockchain Concept

A blockchain is a decentralized, distributed, append-only ledger that records transactions across a peer-to-peer network of nodes. Each record (block) is cryptographically linked to the previous block, forming an immutable chain. No single entity controls the database — instead, all nodes maintain a copy of the ledger and use consensus mechanisms to agree on its state.

**Core Properties:**

1. **Decentralization:** No central authority or single point of control. Every node in the network holds a full copy of the blockchain.
2. **Immutability:** Once a block is added to the chain, it cannot be altered or deleted. Any modification to a past block would change its hash, breaking the chain of all subsequent blocks.
3. **Transparency:** All transactions are visible to all participants in the network (in public blockchains).
4. **Consensus-Driven:** Transactions are only added when a majority of nodes agree on their validity through a consensus protocol.

## 6.4.2 Block Structure

Each block in the blockchain contains:

1. **Block Header:**
   - **Previous Block Hash:** The cryptographic hash of the preceding block, creating the "chain."
   - **Timestamp:** When the block was created.
   - **Nonce:** A number used in the consensus process (Proof of Work).
   - **Merkle Root:** A single hash that summarizes all transactions in the block.

2. **Block Body:**
   - A list of validated transactions.

```
┌─────────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
│      Block 0        │    │      Block 1        │    │      Block 2        │
│  (Genesis Block)    │    │                     │    │                     │
├─────────────────────┤    ├─────────────────────┤    ├─────────────────────┤
│ Prev Hash: 0000     │◄───│ Prev Hash: a3f2...  │◄───│ Prev Hash: 7b1c...  │
│ Timestamp           │    │ Timestamp           │    │ Timestamp           │
│ Nonce               │    │ Nonce               │    │ Nonce               │
│ Merkle Root         │    │ Merkle Root         │    │ Merkle Root         │
├─────────────────────┤    ├─────────────────────┤    ├─────────────────────┤
│ Transactions:       │    │ Transactions:       │    │ Transactions:       │
│  Tx0: A→B 10 BTC   │    │  Tx1: B→C 5 BTC    │    │  Tx3: C→D 3 BTC    │
│                     │    │  Tx2: A→D 2 BTC    │    │  Tx4: D→A 1 BTC    │
└─────────────────────┘    └─────────────────────┘    └─────────────────────┘
```

## 6.4.3 Merkle Tree

A Merkle tree is a binary tree of hashes used to efficiently summarize and verify all transactions within a block.

**Construction:**

1. Each transaction is individually hashed (leaf nodes).
2. Pairs of leaf hashes are concatenated and hashed together to form parent nodes.
3. This pairing continues upward until a single root hash (Merkle Root) remains.

```
                    Merkle Root
                   /           \
              Hash(AB)        Hash(CD)
              /     \         /     \
         Hash(A)  Hash(B)  Hash(C)  Hash(D)
           |        |        |        |
          Tx A     Tx B     Tx C     Tx D
```

**Purpose:** If any single transaction is modified, its hash changes, which propagates up the tree, changing the Merkle Root. This makes tampering immediately detectable. The Merkle tree also enables efficient verification — a node can verify that a specific transaction is included in a block by checking only a logarithmic number of hashes (Merkle proof) rather than downloading all transactions.

## 6.4.4 How Transactions Are Recorded and Verified

**Step-by-step process:**

**Step 1: Transaction Initiation.**
A user initiates a transaction (e.g., "Ram sends 5 BTC to Sita"). The transaction is digitally signed using the sender's private key to prove authenticity.

**Step 2: Broadcasting.**
The signed transaction is broadcast to all nodes in the peer-to-peer network.

**Step 3: Validation.**
Each node independently validates the transaction:
- Verifies the digital signature using the sender's public key.
- Checks that the sender has sufficient balance (no double-spending).
- Checks that the transaction format is correct.

**Step 4: Block Formation.**
Valid transactions are collected into a candidate block by a miner (or validator) node.

**Step 5: Consensus.**
The miner must prove the validity of the block to the network using a consensus mechanism:

**Proof of Work (PoW):** The miner must find a nonce such that the hash of the block header starts with a specified number of leading zeros. This requires enormous computational effort (trial and error) but is trivially easy for other nodes to verify. The first miner to find a valid nonce broadcasts the block.

**Proof of Stake (PoS):** Validators are chosen based on the amount of cryptocurrency they "stake" (lock up as collateral). The chosen validator creates the block and other validators attest to its correctness. This is more energy-efficient than PoW.

**Step 6: Block Addition.**
Once the network accepts the block (majority consensus), it is appended to the chain. Every node updates its local copy of the blockchain.

**Step 7: Confirmation.**
The transaction is considered confirmed. As more blocks are added on top, the transaction becomes increasingly difficult to reverse (deeper in the chain = more secure).

## 6.4.5 Why Blockchain is More Secure Than Traditional Centralized Databases

1. **No Single Point of Failure:** A centralized database can be compromised by attacking a single server. A blockchain is distributed across thousands of nodes — an attacker would need to compromise a majority of the network simultaneously.

2. **Immutability Through Hash Chaining:** In a centralized database, an administrator can modify or delete records. In a blockchain, changing a past block requires recalculating the hashes of all subsequent blocks and doing so faster than the rest of the network continues to add new blocks — computationally infeasible.

3. **Cryptographic Verification:** Every transaction is digitally signed with the sender's private key and verified using the public key. This prevents forgery and unauthorized transactions. Centralized databases rely on access control, which can be bypassed by insider threats.

4. **Consensus Requirement:** No single node can unilaterally add or modify data. Changes require agreement from a majority of nodes. In a centralized database, a single compromised admin account can alter data.

5. **Transparency and Auditability:** All transactions are visible to all participants and permanently recorded. Any attempt to alter the ledger is immediately detectable by comparing hashes across nodes.

6. **Decentralized Trust:** Centralized databases require trust in the database administrator. Blockchain eliminates this trust requirement — the mathematical properties of cryptographic hashing and consensus provide trust.

**Blockchain Database vs. Traditional Database:**

1. **Control:** Traditional databases are centrally controlled by an organization. Blockchain databases are governed by consensus among distributed participants.
2. **Mutability:** Traditional databases allow CRUD operations (including updates and deletes). Blockchain databases are append-only — data can only be added, never modified or deleted.
3. **Performance:** Traditional databases offer high throughput and low latency. Blockchain databases have lower throughput due to the overhead of consensus mechanisms.
4. **Use Cases:** Traditional databases are suited for general-purpose applications. Blockchain databases are suited for scenarios requiring trust, transparency, and tamper-proof records — supply chain tracking, financial transactions, digital identity, voting systems.

**Examples of Blockchain Database Systems:** BigchainDB, Amazon QLDB (Quantum Ledger Database), Hyperledger Fabric, Ethereum (smart contracts).
