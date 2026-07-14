**1. a)** Design an appropriate Entity-Relationship (ER) model for Pokhara University which wants to design a database for its Examination Section to manage students, courses, exams, and results. Then, convert the ER model into a relational schema with necessary DDL, SQL Queries and Keys. **(8)**

**b)** Explain advanced SQL subqueries and aggregations. Provide an SQL snippet that uses a Window Function (like RANK() or OVER()) to solve a real-world data analytical problem. **(7)**

**2. a)** What is Query Optimization? Compare Cost-Based Optimization (CBO) with Rule-Based Optimization (RBO). How does the database engine use statistics to create an optimal execution plan? **(8)**

**b)** How Client Server architecture is different from Peer to Peer System Architecture? Compare their trade-offs in terms of performance, scalability, and data consistency. **(7)**

**3. a)** Explain the Two-Phase Commit (2PC) protocol in detail. Under what specific failure conditions does 2PC lead to a "blocking" state, and how does this affect system availability? **(8)**

**b)** Compare Data Fragmentation (Horizontal vs. Vertical) with Data Replication. In a globally distributed application, how would you decide which attributes to fragment and which to replicate to minimize network latency? **(7)**

**OR**

Discuss Consistency Models in distributed systems. Explain the trade-offs between Strong Consistency and Eventual Consistency in the context of a high-traffic social media platform.

**4. a)** How NoSQL differs from Relational Database? Explain different types of NoSQL Data Models. Also, explain with an example, how Aggregation is performed in NoSQL. **(8)**

**b)** A social network stores users and their friendships in a graph database. Write a query (using a suitable graph query language) to find all friends-of-friends of a given user. Explain how graph traversal works in this scenario and discuss the advantages of using a graph database for such operations. **(7)**

**5. a)** Explain the concept of Time-Series Databases. How do they optimize storage for high-velocity telemetry data compared to a standard Relational DBMS? **(7)**

**b)** Explain the concept of a blockchain database and how it provides decentralized storage and immutability. Illustrate with an example how transactions are recorded and verified in a blockchain-based database system. **(8)**

**6. a)** Explain the concepts of vector databases, edge databases, and serverless databases. Compare their architectures, use cases, and advantages, and discuss how they differ from traditional database systems. **(8)**

**b)** Compare horizontal and vertical database partitioning. Design a scenario for a large e-commerce system and explain which partitioning strategy you would use for the Orders table and why. **(7)**

**7.** Write short notes on: (Any two) **(2×5)**
a) Authentication vs Authorization
b) Load Balancing and high Availability
c) Sharding

---

**1. a)** What are the key differences between structured, semi-structured, and unstructured data? Explain in detail why graph databases are better suited for social network applications over relational databases? **(8)**

**b)** Differentiate between a Cartesian Product and a Join in relational databases. Additionally, explain how a foreign key can be used to enforce referential integrity constraints, including appropriate SQL syntax. **(7)**

**2. a)** What are the limitations of static hashing in database systems? How does dynamic hashing address these limitations? Explain with suitable illustrations. **(8)**

**b)** How does a materialized view differ from a standard (regular) view in a database? Explain materialized views and caching strategies in detail. **(7)**

**3. a)** What is distributed computing? Describe the various types of DDBMS architectures, focusing on the three key aspects: autonomy, distribution, and heterogeneity. **(7)**

**b)** What are the advantages and potential drawbacks of vertical fragmentation in distributed databases? Given a set of attributes and their access frequencies, describe the process to create vertical fragments using clustered affinity matrix. Assumptions can be made if necessary. **(8)**

**4. a)** How does the Two-Phase Commit (2PC) protocol differ from the Three-Phase Commit (3PC) protocol? Provide a detailed comparison including their communication structure and state transition diagrams. **(8)**

**b)** Write the key features of NoSQL systems. Describe how CRUD operations are performed using any NoSQL database tool of your choice. **(7)**

**5. a)** Define SQL and NoSQL. Explain different types of NoSQL database with their data model, characteristics, advantages and disadvantages. **(8)**

**b)** Explain the working principles of the MapReduce programming model. Discuss the roles of the Map and Reduce functions in distributed data processing, and illustrate your explanation with a real-world use case. **(7)**

**6. a)** Explain the working mechanism of blockchain technology with appropriate illustrations. Why is a blockchain-based database considered more secure than traditional centralized database systems? **(7)**

**b)** Differentiate between Redis and Memcached Caching Strategies. What are the various techniques for horizontal partitioning in databases? Explain any one of these techniques in detail. **(8)**

**7.** Write short notes on: (Any two) **(2×5)**
a) Local and Global Indexing
b) Vector Database
c) Edge Database

---

**1. a)** Design ER model for conference management system that manages authors, papers, reviewers, sessions, and scheduling. Also write SQL DDL to convert this ER model to equivalent relational schemas. **(8)**

**b)** Define trigger and its role in maintaining data integrity. In question 1 a), how can trigger be utilized to enforce constraint "A reviewer can review a maximum of 5 papers"? **(7)**

**2. a)** Given relational schemas:

- Employee(eid, emp_name, address, supervisor_id)
- Department(did, dep_name)
- Project(pid, prj_name, did)
- Workson(eid, pid, hours)

Write relational algebraic expression and SQL for performing following operations: **(8)**
&nbsp;&nbsp;&nbsp;i. List the name of all employees for computer department along with their supervisor Name.
&nbsp;&nbsp;&nbsp;ii. Find the total number of projects from each department along with department name.
&nbsp;&nbsp;&nbsp;iii. Find the employee's name who do not work in any project.
&nbsp;&nbsp;&nbsp;iv. Find the name of each project with more than 3 employees.

**b)** Write algorithm for insertion in B+ Tree Index tree. Construct B+ tree of order 4 for the following set of keys: 2, 3, 5, 7, 11, 17, 19, 23, 29, 31. **(7)**

**3. a)** In a university database, how can you efficiently get the total salary paid to instructors in each department without recalculating the sum every time? Write necessary SQL queries to create, refresh, and view for this purpose. **(7)**

**b)** Explain the difference between strong consistency, eventual consistency, and causal consistency with suitable examples. **(8)**

**4. a)** Differentiate between horizontal and vertical fragmentation. Explain how horizontal fragmentation is achieved with real world example. **(8)**

**b)** Define stored procedure. How can we create parameterized stored procedure? Explain with necessary syntax and example. **(7)**

**5. a)** What is Sharding? Explain Sharding operation and its implementation using any NoSQL database tools. **(8)**

**b)** Explain the architecture of HDFS. How is Read and Write performed in HDFS? **(7)**

**6. a)** What is database partitioning? Explain different database partitioning techniques in detail with example. **(7)**

**b)** Differentiate between authentication and authorization. Can a system be strongly consistent and highly available at the same time? Relate your answer to the CAP theorem. **(8)**

**7.** Write short notes on any two: **(2×5 = 10)**
a) Blockchain Database
b) Vector Database
c) Cloud Database
