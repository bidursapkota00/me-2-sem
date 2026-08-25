# 5. NoSQL Databases

# 5.1 Types of NoSQL Databases (Document, Key-Value, Column-Family, Graph)

> **What are the key differences between structured, semi-structured, and unstructured data? Explain in detail why graph databases are better suited for social network applications over relational databases? [8 marks] (2081)**
>
> **How NoSQL differs from Relational Database? Explain different types of NoSQL Data Models. Also, explain with an example, how Aggregation is performed in NoSQL. [8 marks] (2082)**
>
> **Define SQL and NoSQL. Explain different types of NoSQL database with their data model, characteristics, advantages and disadvantages. [8 marks] (2081)**

## 5.1.1 SQL vs. NoSQL

**SQL (Relational) databases** store data in structured tables with predefined schemas. They use SQL as the query language and follow the ACID transaction model. Examples: MySQL, PostgreSQL, Oracle.

**NoSQL (Not Only SQL) databases** are non-relational databases designed for flexible schemas, horizontal scalability, and specific data model requirements that relational databases handle inefficiently. They generally follow the BASE model.

**ACID vs. BASE:**

**ACID (Relational Databases):**
- **Atomicity:** A transaction either completes entirely or not at all.
- **Consistency:** The database moves from one valid state to another valid state after every transaction.
- **Isolation:** Concurrent transactions do not interfere with each other.
- **Durability:** Once committed, data persists even after system failure.

**BASE (NoSQL Databases):**
- **Basically Available:** The system guarantees availability — every request receives a response (success or failure).
- **Soft State:** The state of the system may change over time, even without input, due to eventual consistency propagation.
- **Eventually Consistent:** The system will become consistent over time, but reads may return stale data temporarily.

**NoSQL vs. Relational Database:**

1. **Data Model:** Relational databases use fixed tables with rows and columns. NoSQL databases use flexible models — documents, key-value pairs, column families, or graphs.
2. **Schema:** Relational databases require a rigid, predefined schema (schema-on-write). NoSQL databases allow dynamic, flexible schemas (schema-on-read).
3. **Scalability:** Relational databases typically scale vertically (more powerful hardware). NoSQL databases are designed for horizontal scaling (more servers/nodes).
4. **Query Language:** Relational databases use standardized SQL. NoSQL databases use database-specific query mechanisms (MongoDB Query Language, CQL, Cypher, etc.).
5. **Joins:** Relational databases support complex multi-table joins natively. NoSQL databases generally avoid joins; related data is denormalized and embedded within a single aggregate.
6. **Transactions:** Relational databases provide full ACID transactions. Most NoSQL databases provide eventual consistency or limited transaction support (though some modern NoSQL systems like MongoDB 4.0+ support multi-document ACID transactions).
7. **Use Cases:** Relational databases are best for structured data with complex relationships and strict consistency requirements (banking, ERP). NoSQL databases are best for large-scale, high-throughput applications with flexible or evolving schemas (social media, IoT, real-time analytics).

## 5.1.2 Aggregate Orientation

A central concept in NoSQL (introduced by Sadalage and Fowler in *NoSQL Distilled*) is the **aggregate** — a collection of related objects treated as a unit for data manipulation. In relational databases, data is normalized across multiple tables. In aggregate-oriented NoSQL databases, related data is grouped into a single unit (document, row with column families, or key-value pair) that can be stored, retrieved, and replicated atomically.

Aggregate orientation makes it easy to distribute data across clusters because the aggregate is the natural unit of replication and sharding. However, it makes cross-aggregate queries more difficult.

Three of the four NoSQL types (key-value, document, column-family) are aggregate-oriented. Graph databases are not aggregate-oriented — they focus on relationships between individual entities.

## 5.1.3 Key-Value Databases

**Data Model:** The simplest NoSQL model. Data is stored as a collection of key-value pairs, where the key is a unique identifier (string) and the value is an opaque blob (the database does not inspect or index the value's internal structure).

```
Key: "user:1001"    →  Value: {"name": "Ram", "age": 25, "city": "Kathmandu"}
Key: "session:abc"  →  Value: {token: "xyz", expires: "2026-09-01"}
```

**Characteristics:**
- Extremely fast lookups by key (O(1) hash-based access).
- The database treats the value as an opaque object — no querying by value content.
- Horizontally scalable — keys are easily partitioned across nodes using consistent hashing.

**Advantages:**
- Very high performance for simple read/write operations.
- Easy to scale horizontally.
- Simple API: GET, PUT, DELETE.

**Disadvantages:**
- No support for complex queries, joins, or filtering by value attributes.
- No built-in relationships between data items.
- Application must manage data structure within values.

**Examples:** Redis, Amazon DynamoDB, Riak, Memcached.

**Use Cases:** Session management, caching, user preferences, shopping carts.

## 5.1.4 Document Databases

**Data Model:** Data is stored as self-contained documents, typically in JSON, BSON, or XML format. Each document contains key-value pairs, but unlike key-value stores, the database understands the internal structure of the document and can query, index, and filter by any field within it.

```json
{
  "_id": "1001",
  "name": "Sita Sharma",
  "department": "Computer Science",
  "courses": [
    {"code": "CMP553", "title": "Database Engineering", "credits": 3},
    {"code": "CMP551", "title": "Machine Learning", "credits": 3}
  ],
  "address": {
    "city": "Pokhara",
    "district": "Kaski"
  }
}
```

**Characteristics:**
- Documents in the same collection can have different structures (flexible schema).
- Supports nested documents and arrays, allowing hierarchical data to be stored in a single document.
- Rich query language — can query by any field, including nested fields.
- Documents are the unit of atomicity — operations on a single document are atomic.

**Advantages:**
- Flexible schema accommodates evolving data requirements without migration.
- Natural mapping to objects in application code (reduces impedance mismatch).
- Supports indexing on any field for efficient queries.
- Related data can be embedded in a single document, reducing the need for joins.

**Disadvantages:**
- Cross-document queries (equivalent to joins) are less efficient than in relational databases.
- Data denormalization can lead to data duplication and update anomalies.
- Large, deeply nested documents can become unwieldy.

**Examples:** MongoDB, CouchDB, Amazon DocumentDB.

**Use Cases:** Content management, e-commerce catalogs, user profiles, event logging.

## 5.1.5 Column-Family Databases (Wide-Column Stores)

**Data Model:** Data is organized into column families (groups of related columns). Each row is identified by a row key and can have a different set of columns. Conceptually, it is a two-dimensional map: the row key maps to a set of column-family maps, and each column family maps column names to values.

```
Row Key: "student:1001"
  Column Family "info":    {name: "Hari", dept: "CS", year: 3}
  Column Family "grades":  {CMP553: "A", CMP551: "B+", CMP555: "A-"}

Row Key: "student:1002"
  Column Family "info":    {name: "Gita", dept: "IT"}
  Column Family "grades":  {CMP553: "B"}
```

**Characteristics:**
- Columns are grouped into column families, which are the unit of storage and access.
- Each row can have a different number of columns within a column family (sparse storage).
- Optimized for read/write operations on large datasets across distributed clusters.
- Data is stored column-wise on disk, making column-based queries (aggregations, analytics) efficient.

**Advantages:**
- Excellent horizontal scalability for very large datasets (petabyte scale).
- High write throughput — designed for write-heavy workloads.
- Tunable consistency (e.g., Cassandra allows per-query consistency levels).
- Efficient for queries that access specific column families.

**Disadvantages:**
- No support for joins or complex relational queries.
- Data modeling is query-driven — the schema must be designed around the expected queries.
- Limited support for ad-hoc queries.

**Examples:** Apache Cassandra, HBase, Google Bigtable.

**Use Cases:** Time-series data, IoT sensor data, recommendation engines, logging at scale.

## 5.1.6 Graph Databases

**Data Model:** Data is stored as nodes (entities), edges (relationships), and properties (attributes of nodes and edges). The graph structure directly represents relationships, making traversal operations highly efficient.

```
(Ram:Person {age: 25}) -[:FRIEND {since: 2020}]-> (Sita:Person {age: 24})
(Ram:Person)           -[:ENROLLED_IN]->          (CMP553:Course {title: "DB Engineering"})
```

**Characteristics:**
- Relationships are first-class citizens — they are stored explicitly, not computed at query time via joins.
- Traversal of relationships is O(1) per hop (follows direct pointers), unlike relational databases where joins require index lookups.
- Schema-flexible — new types of nodes and relationships can be added without altering existing data.

**Advantages:**
- Extremely efficient for relationship-heavy queries (social networks, recommendation engines, fraud detection).
- Intuitive data modeling — the graph model closely mirrors real-world networks.
- Variable-length path traversal (e.g., friends-of-friends at arbitrary depth) is natural and fast.

**Disadvantages:**
- Not optimized for aggregate operations (sums, counts across large datasets).
- Horizontal scaling is more challenging than aggregate-oriented NoSQL databases.
- Less mature tooling and ecosystem compared to relational and document databases.

**Examples:** Neo4j, Amazon Neptune, JanusGraph, ArangoDB.

**Use Cases:** Social networks, fraud detection, knowledge graphs, network/IT infrastructure mapping, recommendation engines.

**Why Graph Databases are Better for Social Networks than Relational Databases:**

In a social network, the core operations involve traversing relationships — finding friends, friends-of-friends, mutual connections, shortest paths, and influence networks. In a relational database, these operations require recursive self-joins on a friendship table, which become exponentially expensive as the depth of traversal increases. For example, finding friends-of-friends requires a 2-level self-join; finding connections at depth 5 requires 5 self-joins, each involving large intermediate result sets.

In a graph database, each node stores direct pointers to its adjacent nodes. Traversal simply follows these pointers, making each hop a constant-time operation regardless of the total database size. A 5-hop traversal in a graph database touches only the nodes along the path, while a relational database would need to scan and join large tables. This makes graph databases orders of magnitude faster for relationship-centric queries.

---

# 5.2 NoSQL Data Models

> **Write the key features of NoSQL systems. Describe how CRUD operations are performed using any NoSQL database tool of your choice. [7 marks] (2081)**

**Key Features of NoSQL Systems:**

1. **Flexible Schema:** No rigid schema definition required. Data structure can vary between records in the same collection.
2. **Horizontal Scalability:** Designed to scale out by adding more commodity servers (nodes) to a cluster.
3. **High Availability:** Built-in replication across nodes ensures the system remains available even if individual nodes fail.
4. **Partition Tolerance:** Data is automatically distributed across nodes with built-in fault tolerance.
5. **Aggregate-Oriented Storage:** Data that is accessed together is stored together (documents, column families, key-value aggregates).
6. **Eventual Consistency:** Most NoSQL databases prioritize availability and performance over strict consistency, using eventual consistency.
7. **Denormalized Data Model:** Related data is embedded/denormalized rather than normalized across tables, reducing the need for joins.
8. **Schema-on-Read:** The schema is applied when data is read rather than when it is written, allowing flexible ingestion.

**CRUD Operations in MongoDB:**

MongoDB stores data as BSON (Binary JSON) documents in collections (analogous to tables). Below are the CRUD operations using the MongoDB shell (mongosh):

**Create (Insert):**

```javascript
// Insert a single document
db.students.insertOne({
  name: "Hari Bahadur",
  department: "Computer Science",
  semester: 2,
  courses: ["CMP553", "CMP551"],
  gpa: 3.7
});

// Insert multiple documents
db.students.insertMany([
  { name: "Sita Kumari", department: "IT", semester: 3, gpa: 3.5 },
  { name: "Ram Prasad", department: "Computer Science", semester: 2, gpa: 3.9 }
]);
```

**Read (Query):**

```javascript
// Find all students
db.students.find();

// Find students in Computer Science department
db.students.find({ department: "Computer Science" });

// Find students with GPA greater than 3.6
db.students.find({ gpa: { $gt: 3.6 } });

// Find one student by name, return only name and gpa fields
db.students.findOne(
  { name: "Hari Bahadur" },
  { name: 1, gpa: 1, _id: 0 }
);
```

**Update:**

```javascript
// Update a single document
db.students.updateOne(
  { name: "Hari Bahadur" },
  { $set: { gpa: 3.8, semester: 3 } }
);

// Update multiple documents
db.students.updateMany(
  { department: "Computer Science" },
  { $inc: { semester: 1 } }   // increment semester by 1
);

// Replace an entire document
db.students.replaceOne(
  { name: "Ram Prasad" },
  { name: "Ram Prasad", department: "CS", semester: 3, gpa: 3.95 }
);
```

**Delete:**

```javascript
// Delete a single document
db.students.deleteOne({ name: "Sita Kumari" });

// Delete multiple documents
db.students.deleteMany({ gpa: { $lt: 3.0 } });
```

---

# 5.3 CRUD, Aggregation, Sharding Operation and Its Implementation Using NoSQL Database Tools

> **What is Sharding? Explain Sharding operation and its implementation using any NoSQL database tools. [8 marks] (2080)**

## 5.3.1 Aggregation in MongoDB

The aggregation pipeline processes documents through a series of stages, where the output of one stage becomes the input to the next. It is used for complex data transformations and analytics — grouping, filtering, computing averages, sums, counts, etc.

**Common Aggregation Pipeline Stages:**

1. **$match:** Filters documents (similar to WHERE in SQL).
2. **$group:** Groups documents by a field and computes aggregate values (SUM, AVG, COUNT, etc.).
3. **$project:** Reshapes documents — include, exclude, or compute new fields.
4. **$sort:** Orders documents by specified fields.
5. **$limit:** Restricts the number of documents passed to the next stage.
6. **$unwind:** Deconstructs an array field, creating one document per array element.
7. **$lookup:** Performs a left outer join with another collection (similar to JOIN in SQL).

**Example: Find the average GPA and student count per department**

```javascript
db.students.aggregate([
  // Stage 1: Filter only active students
  { $match: { status: "active" } },

  // Stage 2: Group by department
  {
    $group: {
      _id: "$department",
      avgGPA: { $avg: "$gpa" },
      totalStudents: { $sum: 1 },
      maxGPA: { $max: "$gpa" }
    }
  },

  // Stage 3: Sort by average GPA descending
  { $sort: { avgGPA: -1 } },

  // Stage 4: Reshape the output
  {
    $project: {
      department: "$_id",
      avgGPA: { $round: ["$avgGPA", 2] },
      totalStudents: 1,
      maxGPA: 1,
      _id: 0
    }
  }
]);
```

**Output:**

```json
[
  { "department": "Computer Science", "avgGPA": 3.75, "totalStudents": 45, "maxGPA": 4.0 },
  { "department": "IT", "avgGPA": 3.62, "totalStudents": 38, "maxGPA": 3.95 }
]
```

**Example: Aggregation with $unwind (nested array)**

```javascript
// Each student has a "courses" array. Count enrollments per course.
db.students.aggregate([
  { $unwind: "$courses" },
  {
    $group: {
      _id: "$courses",
      enrollmentCount: { $sum: 1 }
    }
  },
  { $sort: { enrollmentCount: -1 } }
]);
```

## 5.3.2 Sharding in MongoDB

Sharding is the process of distributing data across multiple servers (shards) to handle large datasets and high-throughput operations. Each shard holds a subset of the total data. Sharding provides horizontal scalability — as data grows, more shards are added to the cluster.

**Architecture of a Sharded MongoDB Cluster:**

A sharded cluster consists of three components:

1. **Shards:** Individual MongoDB instances (deployed as replica sets) that store a subset of the sharded data. Each shard is responsible for a range of shard key values.
2. **Config Servers:** A replica set that stores the cluster's metadata — the mapping of data chunks to shards, the shard key ranges, and cluster configuration. The config servers are the source of truth for the data distribution.
3. **Mongos (Query Router):** A routing process that sits between the client application and the sharded cluster. It receives queries from clients, consults the config server metadata to determine which shard(s) contain the relevant data, routes the query to the appropriate shard(s), and merges the results.

```
                    Client Application
                          |
                       [mongos]  (Query Router)
                      /    |    \
                [Shard 1] [Shard 2] [Shard 3]
                (Replica   (Replica   (Replica
                 Set)       Set)       Set)
                          |
                   [Config Servers]
                    (Replica Set)
```

**Shard Key:**

The shard key is a field (or compound field) chosen from the documents in a collection. It determines how data is partitioned across shards. The shard key value is used to divide the collection into chunks, and each chunk is assigned to a shard.

**Choosing a Good Shard Key:**
- **High Cardinality:** Many distinct values allow fine-grained distribution.
- **Even Distribution:** Values should be uniformly distributed to avoid hotspots (one shard receiving disproportionate traffic).
- **Query Isolation:** Queries that include the shard key can be routed to a single shard (targeted query). Queries without the shard key must be broadcast to all shards (scatter-gather), which is less efficient.
- **Avoid Monotonically Increasing Keys:** Keys like timestamps or auto-increment IDs cause all new writes to hit the last shard, creating a bottleneck.

**Chunks and Balancing:**

MongoDB divides the shard key space into contiguous ranges called chunks. As data grows, chunks that exceed a size threshold are automatically split. The balancer is a background process that monitors chunk distribution across shards and migrates chunks from overloaded shards to underloaded ones to maintain even distribution.

**Implementation Steps:**

```javascript
// Step 1: Connect to mongos
mongosh --host mongos-host:27017

// Step 2: Enable sharding for a database
sh.enableSharding("universityDB");

// Step 3: Create an index on the shard key
db.students.createIndex({ department: 1 });

// Step 4: Shard the collection with the chosen shard key
sh.shardCollection("universityDB.students", { department: 1 });

// Step 5: Verify sharding status
sh.status();

// Step 6: Insert data (mongos routes writes to the correct shard)
db.students.insertOne({
  name: "Hari Bahadur",
  department: "Computer Science",
  semester: 2
});

// Step 7: Query data (mongos routes to the correct shard if shard key is used)
db.students.find({ department: "Computer Science" });  // targeted query
db.students.find({ name: "Hari Bahadur" });            // scatter-gather query
```

**Sharding Strategies:**

1. **Range-Based Sharding:** Chunks are divided by contiguous ranges of shard key values. Good for range queries but can lead to uneven distribution if data is skewed.
2. **Hash-Based Sharding:** A hash function is applied to the shard key value. Provides more uniform data distribution but does not support efficient range queries.
3. **Zone-Based Sharding:** Data is assigned to specific shards based on zones (e.g., geographic regions). Useful for data locality requirements.

## 5.3.3 CRUD and Sharding in Cassandra

Apache Cassandra is a column-family NoSQL database designed for high availability and massive scalability with no single point of failure.

**Data Model:**
- **Keyspace:** The top-level container (equivalent to a database in RDBMS). Defines the replication strategy.
- **Table:** A collection of rows, where each row is identified by a primary key.
- **Primary Key:** Consists of a **partition key** (determines which node stores the data) and optional **clustering columns** (determines the sort order within a partition).

**CRUD Operations in CQL (Cassandra Query Language):**

```sql
-- Create a keyspace with replication
CREATE KEYSPACE university
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};

USE university;

-- Create a table
CREATE TABLE students (
  student_id UUID PRIMARY KEY,
  name TEXT,
  department TEXT,
  semester INT,
  gpa DECIMAL
);

-- INSERT (also acts as UPSERT — updates if the key exists)
INSERT INTO students (student_id, name, department, semester, gpa)
VALUES (uuid(), 'Hari Bahadur', 'Computer Science', 2, 3.7);

-- SELECT (read)
SELECT * FROM students WHERE student_id = some_uuid;
SELECT name, gpa FROM students;

-- UPDATE
UPDATE students SET gpa = 3.8 WHERE student_id = some_uuid;

-- DELETE
DELETE FROM students WHERE student_id = some_uuid;
```

**Tunable Consistency in Cassandra:**

Cassandra allows setting the consistency level per query, balancing between consistency and availability:
- **ONE:** Only one replica must respond. Fastest but weakest consistency.
- **QUORUM:** A majority (⌊N/2⌋ + 1, where N = replication factor) must respond. Provides strong consistency when used for both reads and writes (R + W > N).
- **ALL:** All replicas must respond. Strongest consistency but lowest availability.
- **LOCAL_QUORUM:** A quorum within the local data center only. Reduces cross-datacenter latency.

---

# 5.4 Graph Traversal and Graph Databases and Its Implementation

> **A social network stores users and their friendships in a graph database. Write a query (using a suitable graph query language) to find all friends-of-friends of a given user. Explain how graph traversal works in this scenario and discuss the advantages of using a graph database for such operations. [7 marks] (2082)**

## 5.4.1 Graph Database Concepts

A graph database stores data as a property graph consisting of:

1. **Nodes (Vertices):** Represent entities (persons, products, locations). Each node can have labels (types) and properties (key-value attributes).
2. **Edges (Relationships):** Represent connections between nodes. Each edge has a type, direction, and can have properties.
3. **Properties:** Key-value pairs attached to nodes or edges.

**Index-Free Adjacency:** In graph databases like Neo4j, each node directly stores pointers to its adjacent nodes. When traversing a relationship, the database follows the pointer directly — it does not need to perform an index lookup or a join. This is called index-free adjacency, and it makes traversal operations O(1) per hop regardless of the total graph size.

## 5.4.2 Neo4j and Cypher Query Language

Neo4j is the most widely used graph database. It uses Cypher as its declarative query language. Cypher uses an ASCII-art pattern syntax to describe graph patterns.

**Basic Syntax:**
- `(n:Label {property: value})` — a node with a label and property.
- `-[:RELATIONSHIP_TYPE]->` — a directed relationship.
- `MATCH` — finds patterns in the graph.
- `CREATE` — creates nodes and relationships.
- `RETURN` — specifies what to output.

**Creating Nodes and Relationships:**

```cypher
// Create Person nodes
CREATE (ram:Person {name: 'Ram', age: 25})
CREATE (sita:Person {name: 'Sita', age: 24})
CREATE (hari:Person {name: 'Hari', age: 26})
CREATE (gita:Person {name: 'Gita', age: 23})
CREATE (shyam:Person {name: 'Shyam', age: 27})

// Create FRIEND relationships
CREATE (ram)-[:FRIEND]->(sita)
CREATE (ram)-[:FRIEND]->(hari)
CREATE (sita)-[:FRIEND]->(gita)
CREATE (hari)-[:FRIEND]->(shyam)
CREATE (gita)-[:FRIEND]->(shyam)
```

**Graph Structure:**

```
Ram --FRIEND--> Sita --FRIEND--> Gita --FRIEND--> Shyam
 |                                                  ^
 +---FRIEND---> Hari ----------FRIEND--------------+
```

**Query: Find All Friends of Ram**

```cypher
MATCH (ram:Person {name: 'Ram'})-[:FRIEND]->(friend)
RETURN friend.name AS FriendName;
```

Result: Sita, Hari

**Query: Find All Friends-of-Friends of Ram**

```cypher
MATCH (ram:Person {name: 'Ram'})-[:FRIEND]->()-[:FRIEND]->(fof:Person)
WHERE NOT (ram)-[:FRIEND]->(fof) AND ram <> fof
RETURN DISTINCT fof.name AS FriendOfFriend;
```

Result: Gita, Shyam

**Explanation:** The pattern `(ram)-[:FRIEND]->()-[:FRIEND]->(fof)` traverses exactly two FRIEND hops from Ram. The `WHERE NOT (ram)-[:FRIEND]->(fof)` clause excludes direct friends of Ram (to return only 2nd-degree connections). `ram <> fof` ensures Ram himself is excluded. `DISTINCT` removes duplicates (Shyam is reachable via both Sita→Gita→Shyam and Hari→Shyam).

**Query: Variable-Length Traversal (Friends within 1-3 hops)**

```cypher
MATCH (ram:Person {name: 'Ram'})-[:FRIEND*1..3]-(person:Person)
WHERE ram <> person
RETURN DISTINCT person.name, length(shortestPath((ram)-[:FRIEND*]-(person))) AS distance;
```

## 5.4.3 How Graph Traversal Works

**Step-by-step traversal for "friends-of-friends of Ram":**

1. **Start:** Locate the node Ram (using an index on the name property).
2. **First hop:** Follow all outgoing FRIEND edges from Ram. This yields: Sita, Hari. These are Ram's direct friends.
3. **Second hop:** For each friend found in step 2, follow their outgoing FRIEND edges:
   - From Sita: follow FRIEND → Gita.
   - From Hari: follow FRIEND → Shyam.
4. **Filter:** Remove any results that are Ram's direct friends (Sita, Hari) or Ram himself.
5. **Result:** Gita, Shyam.

Each hop is a constant-time pointer traversal. The database only touches the nodes and edges along the path — it does not scan the entire graph.

## 5.4.4 Advantages of Graph Databases for Relationship-Heavy Operations

1. **Constant-Time Traversal:** Each relationship hop is O(1) due to index-free adjacency. In a relational database, each hop requires a JOIN operation whose cost depends on table size.
2. **Natural Modeling:** Social networks are inherently graph-structured. The graph model directly represents users as nodes and friendships as edges, eliminating the need for intermediate join tables.
3. **Deep Traversal Efficiency:** Finding connections at depth n in a relational database requires n self-joins, each potentially scanning millions of rows. In a graph database, depth-n traversal only follows pointers along the path.
4. **Expressive Queries:** Cypher's pattern-matching syntax makes complex relationship queries intuitive and concise. The equivalent SQL for a friends-of-friends query would require nested subqueries or recursive CTEs.
5. **Dynamic Schema:** New relationship types and node properties can be added without altering existing data, making it easy to evolve the social network's data model.
