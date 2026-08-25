# 4. Distributed Database Systems

# 4.1 Architectural Models for Distributed DBMSs

> **How Client Server architecture is different from Peer to Peer System Architecture? Compare their trade-offs in terms of performance, scalability, and data consistency. [7 marks] (2082)**
>
> **What is distributed computing? Describe the various types of DDBMS architectures, focusing on the three key aspects: autonomy, distribution, and heterogeneity. [7 marks] (2081)**

A distributed database is a collection of logically interrelated databases spread across multiple sites connected by a network. A Distributed Database Management System (DDBMS) manages the distributed database and provides transparency so that users interact with it as if it were a single, centralized database.

**Key Dimensions of DDBMS (Özsu & Valduriez Framework):**

1. **Distribution:** Refers to whether the data and DBMS components are located on a single machine or spread across multiple networked sites. Distribution can be client-only (thin client), or full (data and processing both distributed).
2. **Heterogeneity:** The degree of diversity in hardware, operating systems, network protocols, and DBMS software (data models, query languages) across sites. A homogeneous system uses the same DBMS at all sites; a heterogeneous system uses different DBMSs.
3. **Autonomy:** The degree of independent control each local DBMS retains. It has three sub-dimensions:
   - **Design Autonomy:** Freedom to choose own data model, schema, and constraints.
   - **Communication Autonomy:** Freedom to decide when and how to share data with other sites.
   - **Execution Autonomy:** Freedom to execute local operations without external interference.

## 4.1.1 Client/Server Systems

In a client/server architecture, the system is divided into two distinct roles:

- **Server (Back-end):** Manages the database, handles query processing, optimization, transaction management, and storage. It provides data services to clients.
- **Client (Front-end):** Provides the user interface and application logic. It sends SQL queries to the server and displays results.

**How it works:** The client sends a request (query) over the network to the server. The server processes the request, accesses the database, and returns the result to the client. In a multi-server setup, multiple servers handle different portions of the database, and the client may need to contact the appropriate server.

**Advantages:**
- Centralized data management simplifies consistency and security enforcement.
- Server hardware can be powerful and optimized for database workloads.
- Clear separation of concerns between presentation and data management.

**Disadvantages:**
- The server is a single point of failure (unless replicated).
- As the number of clients grows, the server can become a performance bottleneck.
- Scaling requires upgrading server hardware (vertical scaling) or distributing data across multiple servers.

## 4.1.2 Peer-to-Peer (P2P) Systems

In a peer-to-peer architecture, there is no distinction between client and server. Every node (peer) acts as both a client and a server. Each peer can store data, process queries, and forward requests to other peers.

**How it works:** When a peer needs data that it does not have locally, it sends requests to other peers in the network. Any peer can initiate or respond to queries. Data is distributed across peers, and each peer manages its local data autonomously.

**Advantages:**
- No single point of failure; the system is inherently fault-tolerant.
- Scales horizontally by adding more peers.
- Each peer operates independently, supporting high autonomy.

**Disadvantages:**
- Maintaining global data consistency is complex because there is no central coordinator.
- Query routing and data discovery overhead increases with network size.
- Security enforcement is more difficult without a central authority.

**Client/Server vs. Peer-to-Peer:**

1. **Performance:** Client/server achieves high performance for centralized queries since the server is optimized for data processing. P2P may incur overhead from query routing and inter-peer communication.
2. **Scalability:** Client/server scales vertically (upgrade server) or requires careful horizontal partitioning. P2P scales naturally by adding peers, as each peer adds both storage and processing capacity.
3. **Data Consistency:** Client/server provides easier consistency guarantees through centralized transaction management. P2P requires distributed consensus protocols and is more prone to consistency challenges.
4. **Fault Tolerance:** Client/server has a single point of failure at the server. P2P is resilient because the failure of one peer does not bring down the system.
5. **Autonomy:** Client/server has low local autonomy as the server dictates data management. P2P has high local autonomy as each peer manages its own data.

## 4.1.3 Multidatabase Systems

A multidatabase system (MDBS) integrates multiple pre-existing, autonomous database systems into a unified framework without requiring them to give up their local autonomy. Each participating database (called a component database) may use a different data model, query language, or DBMS software.

**Types:**

1. **Federated Database System:** Each component database retains significant autonomy but agrees to participate in a federation by exporting part of its schema. A federated schema provides a unified view. There is usually a federation layer that translates queries across heterogeneous systems.
2. **Loosely Coupled Multidatabase:** No global schema exists. Users must be aware of the individual databases and construct multi-database queries manually. The system provides only basic facilities for accessing remote data.

**Challenges:**
- Schema integration across heterogeneous systems (resolving naming conflicts, structural differences).
- Query translation between different query languages.
- Managing distributed transactions across autonomous systems.

---

# 4.2 Distributed Database Architectures (Fragmentation, Replication)

> **Compare Data Fragmentation (Horizontal vs. Vertical) with Data Replication. In a globally distributed application, how would you decide which attributes to fragment and which to replicate to minimize network latency? [7 marks] (2082)**
>
> **Differentiate between horizontal and vertical fragmentation. Explain how horizontal fragmentation is achieved with real world example. [8 marks] (2080)**
>
> **What are the advantages and potential drawbacks of vertical fragmentation in distributed databases? Given a set of attributes and their access frequencies, describe the process to create vertical fragments using clustered affinity matrix. [8 marks] (2081)**

In a distributed database, the data must be distributed across multiple sites. The two primary strategies for data distribution are fragmentation and replication.

## 4.2.1 Data Fragmentation

Fragmentation is the process of breaking a relation (table) into smaller pieces called fragments, which are then stored at different sites. The goal is to place data close to where it is most frequently used, thereby reducing network traffic and improving performance.

**Rules of Fragmentation:**

1. **Completeness:** Every data item in the original relation must appear in at least one fragment. No data is lost.
2. **Reconstruction:** The original relation must be fully reconstructable from its fragments using relational operations (UNION for horizontal, JOIN for vertical).
3. **Disjointness:** Fragments should be non-overlapping (except for primary keys in vertical fragmentation) to avoid redundancy and update anomalies.

**Horizontal Fragmentation:**

Horizontal fragmentation divides a relation into subsets of tuples (rows) based on selection predicates. Each fragment contains rows that satisfy a particular condition.

Formally, a horizontal fragment is defined as: Ri = σp(R), where σ is the selection operator and p is the predicate.

The original relation is reconstructed using: R = R1 ∪ R2 ∪ ... ∪ Rn

**Example:** Consider an Employee table distributed across two regional offices:

```
Employee(eid, name, dept, city, salary)

-- Fragment 1: Employees in Kathmandu (stored at Kathmandu site)
Employee_KTM = σ(city='Kathmandu')(Employee)

-- Fragment 2: Employees in Pokhara (stored at Pokhara site)
Employee_PKR = σ(city='Pokhara')(Employee)
```

Queries originating from the Kathmandu office mostly access local employees, avoiding cross-site network transfer.

**Derived Horizontal Fragmentation:** A relation is fragmented based on the predicate of another (related) relation. For example, fragmenting the Projects table based on the department's location fragment.

**Vertical Fragmentation:**

Vertical fragmentation divides a relation into subsets of attributes (columns). Each fragment contains a subset of the columns along with the primary key (to ensure reconstruction via join).

Formally: Ri = π(Ai)(R), where π is the projection operator and Ai is a subset of attributes.

The original relation is reconstructed using: R = R1 ⋈ R2 ⋈ ... ⋈ Rn (natural join on primary key)

**Example:**

```
Employee(eid, name, dept, salary, medical_record)

-- Fragment 1: HR-related attributes (stored at HR site)
Employee_HR = π(eid, name, dept, salary)(Employee)

-- Fragment 2: Medical attributes (stored at Medical site)
Employee_Med = π(eid, medical_record)(Employee)
```

The HR site accesses name, department, and salary frequently, while the medical department accesses medical records. Each site gets only the columns it needs.

**Advantages of Vertical Fragmentation:**
- Reduces data transfer by sending only relevant columns to each site.
- Improves query performance when queries access only a subset of attributes.
- Enhances security by isolating sensitive attributes at specific sites.

**Disadvantages of Vertical Fragmentation:**
- Reconstruction requires expensive JOIN operations.
- If queries frequently need attributes from multiple fragments, performance degrades.
- The primary key must be replicated in every fragment.

**Mixed (Hybrid) Fragmentation:**

Combines both horizontal and vertical fragmentation. A relation may first be horizontally fragmented, and then each horizontal fragment may be vertically fragmented (or vice versa). This provides fine-grained control over data placement.

**Vertical Fragmentation using Clustered Affinity Matrix:**

The process of creating optimal vertical fragments involves the following steps:

**Step 1: Create the Attribute Usage Matrix.** Identify the set of queries Q = {q1, q2, ..., qm} and the set of attributes A = {A1, A2, ..., An}. For each query qi, record which attributes it accesses (1 = uses, 0 = does not use).

**Step 2: Compute the Attribute Affinity Matrix (AA).** For each pair of attributes (Ai, Aj), calculate the affinity value aff(Ai, Aj) = Σ(freq(qk)) for all queries qk that access both Ai and Aj, summed over all sites. Higher affinity means the two attributes are frequently accessed together.

**Step 3: Apply the Bond Energy Algorithm (BEA).** The BEA takes the AA matrix as input and reorders its rows and columns to cluster attributes with high affinity together. The algorithm iteratively places each attribute (column) in the position that maximizes the global affinity measure (sum of products of neighboring elements).

**Step 4: Obtain the Clustered Affinity Matrix (CA).** The output of BEA is the CA matrix where high-affinity attributes are grouped together, forming visible blocks along the diagonal.

**Step 5: Define Fragment Boundaries.** Draw boundaries around the high-affinity blocks in the CA matrix. Each block (plus the primary key) becomes a vertical fragment.

## 4.2.2 Data Replication

Replication involves maintaining multiple copies (replicas) of a relation or fragment at different sites.

**Types of Replication:**

1. **Full Replication:** The entire database is replicated at every site. Provides maximum availability and read performance but makes write operations expensive because all copies must be updated.
2. **Partial Replication:** Some relations or fragments are replicated at selected sites based on access patterns. Balances read performance with update overhead.
3. **No Replication:** Each fragment exists at exactly one site. Minimizes update cost but reduces availability and may increase query latency for remote data access.

**Advantages of Replication:**
- **Availability:** If one site fails, the data is still accessible from other sites.
- **Read Performance:** Queries can be served from the nearest replica, reducing network latency.
- **Parallelism:** Multiple sites can process read queries concurrently.

**Disadvantages of Replication:**
- **Update Overhead:** Every write must be propagated to all replicas, increasing network traffic and requiring synchronization protocols.
- **Consistency Complexity:** Keeping all replicas consistent requires distributed commit protocols (e.g., 2PC) or conflict resolution mechanisms.
- **Storage Cost:** Multiple copies consume more storage.

**Fragmentation vs. Replication:**

1. **Fragmentation** divides data into non-overlapping pieces and distributes them. It reduces data at each site but may require cross-site queries. **Replication** creates copies of the same data at multiple sites. It improves read availability but increases write complexity.
2. In practice, fragmentation and replication are used together. A relation is first fragmented, and then critical fragments are replicated at sites where they are frequently accessed.

**Design Decision for a Globally Distributed Application:**
- **Fragment** attributes that are accessed by specific regional sites to reduce network latency for local queries.
- **Replicate** small, frequently read, and rarely updated reference data (e.g., lookup tables, configuration) to all sites.
- For write-heavy attributes, minimize replication to reduce synchronization overhead.
- For read-heavy attributes accessed from multiple locations, replicate to reduce cross-site latency.

---

# 4.3 CAP Theorem and PACELC Trade-offs

> **Can a system be strongly consistent and highly available at the same time? Relate your answer to the CAP theorem. [8 marks] (2080)**

## 4.3.1 CAP Theorem

The CAP theorem (also called Brewer's theorem, proposed by Eric Brewer in 2000 and proved by Gilbert and Lynch in 2002) states that a distributed data system can provide at most two out of the following three guarantees simultaneously:

1. **Consistency (C):** Every read receives the most recent write or an error. All nodes see the same data at the same time (this refers to linearizability, not ACID consistency).
2. **Availability (A):** Every request (read or write) receives a non-error response, even if some nodes are down. The system continues to operate and serve requests.
3. **Partition Tolerance (P):** The system continues to operate despite arbitrary message loss or failure of part of the network. Network partitions are communication breakdowns between nodes.

**Why only two out of three?**

In any distributed system, network partitions are inevitable (cables break, routers fail, packets get lost). Therefore, partition tolerance is not optional — it must always be supported. This reduces the real choice to:

- **CP (Consistency + Partition Tolerance):** During a partition, the system stops serving requests from the partitioned nodes to maintain consistency. It returns errors rather than stale data. Example: HBase, MongoDB (in default config), Google Spanner.
- **AP (Availability + Partition Tolerance):** During a partition, the system continues serving requests from all nodes, even if some nodes have stale data. It prioritizes uptime over correctness. Example: Cassandra, DynamoDB, CouchDB.

**A system cannot be CA (Consistent + Available) in practice** because a real distributed system must handle network partitions. A CA system would only be possible on a single node (which is not distributed).

**Answer to "Can a system be strongly consistent and highly available at the same time?":**

No. According to the CAP theorem, during a network partition, a system must choose between consistency and availability. A strongly consistent system will reject requests (become unavailable) during a partition to ensure all nodes agree on the data. A highly available system will accept requests during a partition but may return stale or inconsistent data. Both guarantees cannot be simultaneously maintained when partitions occur.

## 4.3.2 PACELC Theorem

The PACELC theorem (proposed by Daniel Abadi, 2012) extends CAP by addressing system behavior during normal operations (when there is no partition).

**PACELC stands for:**
- **P**artition → choose between **A**vailability and **C**onsistency.
- **E**lse (no partition) → choose between **L**atency and **C**onsistency.

**Why PACELC matters:**

CAP only describes what happens during a failure (partition). But even when the system is healthy, there is a fundamental trade-off: to provide strong consistency, the system must coordinate across replicas (synchronous replication), which increases latency. To provide low latency, the system can serve reads from the nearest replica without waiting for all replicas to synchronize, which weakens consistency.

**System Classification under PACELC:**

1. **PA/EL (Availability + Low Latency):** Prioritizes availability during partitions and low latency during normal operation. Sacrifices consistency in both cases. Example: Cassandra, DynamoDB.
2. **PC/EC (Consistency + Consistency):** Prioritizes consistency always — during partitions and during normal operation. Accepts higher latency and potential unavailability. Example: Google Spanner, VoltDB.
3. **PA/EC (Availability + Consistency):** Prioritizes availability during partitions but consistency during normal operation. Example: MongoDB (in some configurations).
4. **PC/EL:** Rarely used. Prioritizes consistency during partitions but low latency during normal operation.

---

# 4.4 Consistency Models (Strong, Eventual, Causal)

> **Explain the difference between strong consistency, eventual consistency, and causal consistency with suitable examples. [8 marks] (2080)**
>
> **Discuss Consistency Models in distributed systems. Explain the trade-offs between Strong Consistency and Eventual Consistency in the context of a high-traffic social media platform. (2082)**

A consistency model defines the rules governing the order and visibility of read and write operations across multiple replicas in a distributed system. It determines what value a read operation returns after a write has been performed.

## 4.4.1 Strong Consistency (Linearizability)

Strong consistency guarantees that any read operation returns the value of the most recent completed write. The system behaves as if there is only a single copy of the data, even though it is replicated across multiple nodes.

**Formally:** Once a write completes, all subsequent reads (from any node) must return the updated value. Operations appear to occur atomically and in a globally consistent order.

**Example:** In a banking system, after a transfer of ₹5000 from Account A to Account B, any subsequent read of either account (from any ATM, any branch) must reflect the updated balance. If Account A had ₹20,000, any read must now return ₹15,000.

**Implementation:** Requires synchronous replication or consensus protocols (e.g., Paxos, Raft). The write must be acknowledged by a majority (or all) replicas before it is considered complete.

**Trade-off:** High correctness but high latency (waiting for replica synchronization) and reduced availability during partitions.

## 4.4.2 Eventual Consistency

Eventual consistency guarantees that if no new writes are made to a data item, all replicas will eventually converge to the same value. However, there is no guarantee about how soon this convergence will occur.

**Formally:** After a write, reads may temporarily return stale values. Given enough time without new writes, all replicas will return the last written value.

**Example:** In a social media platform, when a user posts a new photo, followers in different regions may not see the post immediately. One follower might see the post within seconds, while another might see it after a few minutes. Eventually, all followers will see the same post.

**Implementation:** Uses asynchronous replication. Writes are applied to one replica and propagated to others in the background. Conflict resolution mechanisms (last-write-wins, vector clocks, CRDTs) handle concurrent updates.

**Trade-off:** High availability and low latency but allows temporary inconsistency (stale reads).

## 4.4.3 Causal Consistency

Causal consistency preserves the causal ordering (happens-before relationship) between operations. If operation A causally precedes operation B (i.e., B depends on A), then all nodes must observe A before B. Concurrent operations (those with no causal relationship) may be seen in different orders at different nodes.

**Formally:** If process P1 writes value v1, and process P2 reads v1 and then writes v2 (which depends on v1), all other processes must see v1 before v2. However, two independent writes by unrelated processes may be seen in any order.

**Example:** In a social media comment thread:
- User A posts a question: "What time is the meeting?"
- User B reads the question and replies: "3 PM."

Causal consistency ensures that everyone sees A's question before B's reply. No one will see "3 PM" without the question. However, two independent posts by unrelated users (not causally related) may appear in different orders for different viewers.

**Implementation:** Uses techniques like vector clocks, version vectors, or explicit dependency tracking to record causal relationships between operations.

**Trade-off:** Provides a more intuitive user experience than eventual consistency (preserves logical ordering) without the performance penalty of strong consistency.

**Trade-offs in a High-Traffic Social Media Platform:**

A social media platform must handle millions of concurrent reads and writes globally. Strong consistency would require synchronizing every post, like, and comment across all data centers before returning a response — this creates unacceptable latency for a platform where users expect sub-second response times. Eventual consistency is preferred for posts, likes, and feeds because a small delay (a few seconds) in propagation is acceptable, and the system remains highly available and responsive. For critical operations like authentication, payments, or direct messaging delivery guarantees, stronger consistency (causal or strong) may be selectively applied.

---

# 4.5 Distributed Transactions (2PC, 3PC, Paxos, Raft)

> **Explain the Two-Phase Commit (2PC) protocol in detail. Under what specific failure conditions does 2PC lead to a "blocking" state, and how does this affect system availability? [8 marks] (2082)**
>
> **How does the Two-Phase Commit (2PC) protocol differ from the Three-Phase Commit (3PC) protocol? Provide a detailed comparison including their communication structure and state transition diagrams. [8 marks] (2081)**

A distributed transaction spans multiple nodes (sites), and all nodes must agree on whether to commit or abort the transaction. This is the atomic commitment problem: either all participants commit, or all abort.

## 4.5.1 Two-Phase Commit Protocol (2PC)

2PC is the most widely used atomic commit protocol in distributed databases. It uses a designated coordinator node to manage the commit process across participant nodes.

**Roles:**
- **Coordinator:** The node that initiates and manages the commit protocol.
- **Participants:** The nodes that execute parts of the distributed transaction.

**Phase 1: Prepare (Voting Phase)**

1. The coordinator sends a `PREPARE` message to all participants.
2. Each participant receives the message, determines if it can commit (checks local constraints, acquires locks, writes redo and undo log records to stable storage), and replies:
   - `VOTE-COMMIT` (YES): If it can commit. The participant enters a "prepared" (uncertain) state. It has promised to commit if told to do so and cannot unilaterally abort.
   - `VOTE-ABORT` (NO): If it cannot commit (e.g., constraint violation, resource unavailable). The participant aborts its local transaction.

**Phase 2: Commit/Abort (Decision Phase)**

3. If the coordinator receives `VOTE-COMMIT` from **all** participants:
   - The coordinator writes a `COMMIT` record to its log (the commit point).
   - It sends a `GLOBAL-COMMIT` message to all participants.
4. If any participant votes `VOTE-ABORT` (or a timeout expires):
   - The coordinator writes an `ABORT` record to its log.
   - It sends a `GLOBAL-ABORT` message to all participants.
5. Each participant receives the decision, executes commit or abort, writes the outcome to its log, and sends an `ACKNOWLEDGMENT` to the coordinator.
6. The coordinator collects all acknowledgments and writes an `END` record to its log, completing the protocol.

**The Blocking Problem of 2PC:**

2PC is a blocking protocol. A participant can become blocked (stuck in an uncertain state, holding locks indefinitely) under the following failure conditions:

**Condition 1: Coordinator fails after sending PREPARE but before sending the decision.** Participants that voted YES are in the prepared (uncertain) state. They have promised to commit but have not received the final decision. They cannot commit (because they don't know if all others voted YES) and cannot abort (because they already promised to commit). They must hold their locks and wait for the coordinator to recover. This blocks all resources held by the transaction.

**Condition 2: Coordinator and a participant both fail.** If the coordinator and a participant that voted YES both fail simultaneously, the remaining participants cannot determine the outcome. The failed participant might have already received and acted on the decision (commit or abort). Without knowing this, the remaining participants cannot safely decide. They remain blocked until both the coordinator and the failed participant recover.

**Effect on Availability:** During the blocking period, all resources (locks on data items) held by the uncertain participants are unavailable to other transactions, reducing system throughput and availability.

## 4.5.2 Three-Phase Commit Protocol (3PC)

3PC was designed to address the blocking problem of 2PC by adding an intermediate phase between voting and the final commit.

**Phase 1: Prepare (Voting Phase)** — Same as 2PC. The coordinator sends `PREPARE`, participants vote `YES` or `NO`.

**Phase 2: Pre-Commit**

If all participants voted YES:
- The coordinator sends a `PRE-COMMIT` message to all participants.
- Participants acknowledge the pre-commit. This phase ensures that all participants know the decision will be COMMIT (they are no longer uncertain).
- If any participant or the coordinator fails at this point, the remaining participants know that the decision was to commit and can safely proceed.

If any participant voted NO:
- The coordinator sends `ABORT` to all participants. The protocol terminates.

**Phase 3: Commit (Do-Commit)**

- The coordinator sends the final `COMMIT` message.
- Participants execute the commit and acknowledge.

**How 3PC Solves Blocking:**

The pre-commit phase ensures that before any participant reaches the "committed" state, all participants have agreed and entered the "pre-commit" state. If the coordinator fails after pre-commit, the remaining participants can elect a new coordinator and safely commit (since they know everyone agreed). The use of timeouts at each phase allows participants to make progress even if the coordinator is unresponsive.

**2PC vs. 3PC:**

1. **Phases:** 2PC has 2 phases (prepare + commit). 3PC has 3 phases (prepare + pre-commit + commit).
2. **Blocking:** 2PC can block indefinitely if the coordinator fails during the uncertain state. 3PC is non-blocking under certain failure assumptions (no network partitions).
3. **Messages:** 2PC requires fewer messages (lower communication overhead). 3PC requires additional round of messages for the pre-commit phase.
4. **Network Partitions:** 3PC can fail under network partitions — partitioned nodes might reach different decisions. 2PC handles partitions by blocking (which is safe but not live).
5. **Practical Usage:** 2PC is widely used in practice (MySQL, PostgreSQL, Oracle). 3PC is rarely used due to its complexity and failure under network partitions.
6. **Timeouts:** 2PC participants cannot timeout and decide independently. 3PC uses timeouts to allow participants to make unilateral decisions after a timeout period.

**State Transition Summary:**

```
2PC States:
  Coordinator: INITIAL → WAIT → COMMITTED/ABORTED
  Participant: INITIAL → PREPARED (uncertain) → COMMITTED/ABORTED

3PC States:
  Coordinator: INITIAL → WAIT → PRE-COMMIT → COMMITTED/ABORTED
  Participant: INITIAL → PREPARED → PRE-COMMITTED → COMMITTED/ABORTED
```

## 4.5.3 Paxos Consensus Algorithm

Paxos (proposed by Leslie Lamport, 1989) is a family of consensus protocols used to achieve agreement among a group of nodes on a single value, even if some nodes fail. Unlike 2PC/3PC which solve atomic commitment, Paxos solves the consensus problem.

**Roles in Paxos:**

1. **Proposer:** Proposes a value to be agreed upon.
2. **Acceptor:** Votes on proposals and decides which value to accept.
3. **Learner:** Learns the final decided value.

(A single node can play multiple roles.)

**Basic Paxos Protocol (Two Phases):**

**Phase 1: Prepare**
1. A proposer selects a unique proposal number n (higher than any it has used before) and sends a `PREPARE(n)` message to a majority (quorum) of acceptors.
2. Each acceptor receives `PREPARE(n)`. If n is greater than any proposal number it has already responded to, it promises not to accept any proposal with a number less than n and replies with `PROMISE(n)` along with any value it has already accepted (if any).

**Phase 2: Accept**
3. If the proposer receives `PROMISE` responses from a majority of acceptors:
   - If any acceptor reported a previously accepted value, the proposer must propose that value (the value with the highest accepted proposal number).
   - Otherwise, the proposer can propose its own value.
   - It sends `ACCEPT(n, value)` to the acceptors.
4. Each acceptor receives `ACCEPT(n, value)`. If it has not promised to a higher-numbered proposal, it accepts the value and notifies the learners.
5. Once a majority of acceptors have accepted the same proposal, consensus is reached.

**Key Properties:**
- **Safety:** Only a single value is chosen, and a node never learns a value unless it has been chosen.
- **Fault Tolerance:** The protocol works as long as a majority of acceptors are alive and can communicate. It tolerates minority failures.
- **Liveness:** The protocol may not terminate if multiple proposers continuously compete (dueling proposers). Multi-Paxos addresses this by electing a stable leader.

**Practical Usage:** Multi-Paxos (used in Google Chubby, Apache ZooKeeper's ZAB) extends basic Paxos by electing a single leader to avoid the dueling proposers problem.

## 4.5.4 Raft Consensus Algorithm

Raft (proposed by Diego Ongaro and John Ousterhout, 2014) was designed as an understandable alternative to Paxos. It provides the same consensus guarantees but is organized around a strong leader model, making it easier to implement correctly.

**Roles in Raft:**

1. **Leader:** Handles all client requests and log replication. Only one leader exists at a time.
2. **Follower:** Passive nodes that respond to requests from the leader. If they receive a client request, they redirect it to the leader.
3. **Candidate:** A follower that has not heard from the leader within a timeout period and starts an election.

**Three Sub-problems Raft Solves:**

**1. Leader Election:**
- Each node starts as a follower. If a follower does not receive a heartbeat from the leader within a random timeout period, it becomes a candidate.
- The candidate increments its term number and sends `RequestVote` RPCs to all other nodes.
- A node grants its vote to the first candidate it hears from in a given term (first-come-first-served).
- If a candidate receives votes from a majority of nodes, it becomes the leader.
- If no majority is achieved (split vote), a new election begins with incremented term numbers after random timeouts.

**2. Log Replication:**
- The leader receives client commands and appends them to its log.
- It sends `AppendEntries` RPCs to all followers to replicate the log entry.
- Once a majority of followers have stored the entry, the leader commits it and applies it to its state machine.
- The leader notifies followers of committed entries in subsequent heartbeat/AppendEntries messages.

**3. Safety:**
- Raft guarantees that if a log entry is committed, it will be present in the logs of all future leaders. This is enforced through the election restriction: a candidate cannot win an election unless its log is at least as up-to-date as a majority of the cluster.

**Practical Usage:** Raft is used in etcd (Kubernetes), Consul (HashiCorp), CockroachDB, and TiKV.

**2PC/3PC vs. Paxos/Raft:**

1. **Problem Solved:** 2PC/3PC solve atomic commitment (all-or-nothing transactions). Paxos/Raft solve distributed consensus (agreement on a value or sequence of operations).
2. **Fault Tolerance:** 2PC blocks if the coordinator fails. Paxos/Raft continue as long as a majority of nodes are alive.
3. **Use Case:** 2PC is used for distributed transactions across databases. Paxos/Raft are used for state machine replication, leader election, and distributed coordination.
4. **Modern Systems:** Many modern distributed databases combine both — using Raft/Paxos for replication and leader election, and 2PC for cross-shard transactions (e.g., Google Spanner uses Paxos groups with 2PC across groups).

---

# 4.6 Security in Distributed Database (Authentication, Authorization, Encryption, Integrity)

> **Differentiate between authentication and authorization. [5 marks] (2080)**

Securing a distributed database is more challenging than securing a centralized one because data is spread across multiple sites, transmitted over networks, and managed by potentially heterogeneous systems. The attack surface includes not only each individual node but also the communication channels between them.

## 4.6.1 Authentication

Authentication is the process of verifying the identity of a user, application, or node that is requesting access to the database system. It answers the question: "Who are you?"

**Mechanisms:**

1. **Password-based:** Traditional username/password authentication. The database stores hashed passwords and verifies credentials during login. Simple but vulnerable to brute-force attacks, phishing, and password reuse.
2. **Multi-Factor Authentication (MFA):** Requires two or more independent verification factors: something you know (password), something you have (hardware token, phone OTP), something you are (biometrics). Significantly reduces the risk of unauthorized access.
3. **Certificate-based:** Uses digital certificates issued by a trusted Certificate Authority (CA). Both the client and server present certificates to verify identity. Commonly used for inter-node authentication in distributed clusters (mutual TLS).
4. **Kerberos / LDAP:** Enterprise authentication protocols. Kerberos uses a trusted third-party Key Distribution Center (KDC) to issue time-limited tickets. LDAP provides centralized directory-based authentication.
5. **Single Sign-On (SSO):** Users authenticate once with a central identity provider and gain access to multiple distributed database nodes without re-authenticating.

**Challenge in Distributed Systems:** Authentication must be consistent across all sites. If a user authenticates at one node, other nodes must trust that authentication (through token passing, distributed ticket systems, or federated identity).

## 4.6.2 Authorization

Authorization determines what an authenticated user is allowed to do. It answers the question: "What are you permitted to do?" Authorization is enforced after authentication.

**Mechanisms:**

1. **Role-Based Access Control (RBAC):** Permissions are assigned to roles (e.g., admin, analyst, read_only), and users are assigned to roles. Simplifies management in large systems.

```sql
-- Create a role with specific privileges
CREATE ROLE analyst;
GRANT SELECT ON sales_data TO analyst;
GRANT SELECT ON customer_data TO analyst;

-- Assign a user to the role
GRANT analyst TO user_bidur;
```

2. **Discretionary Access Control (DAC):** The data owner controls access. Uses GRANT and REVOKE SQL commands to give or remove privileges on specific database objects.

```sql
GRANT SELECT, INSERT ON Employee TO user_ram;
REVOKE INSERT ON Employee FROM user_ram;
```

3. **Mandatory Access Control (MAC):** Access is controlled by the system based on security labels (e.g., Confidential, Secret, Top Secret). Users cannot override system-imposed policies. Used in military/government systems.

4. **Attribute-Based Access Control (ABAC):** Access decisions are based on attributes of the user (role, department, clearance), the resource (classification, owner), and the environment (time, location, network).

**Authentication vs. Authorization:**

1. **Purpose:** Authentication verifies identity (who you are). Authorization determines permissions (what you can do).
2. **Order:** Authentication always occurs first. Authorization follows after identity is confirmed.
3. **Mechanism:** Authentication uses credentials (passwords, certificates, biometrics). Authorization uses policies (roles, ACLs, security labels).
4. **Failure:** Authentication failure means the user cannot log in at all. Authorization failure means the user is logged in but denied access to a specific resource.
5. **Example:** Logging into a database server with a password is authentication. Being denied permission to DROP a table because your role only has SELECT privileges is authorization.

## 4.6.3 Encryption

Encryption converts data into an unreadable format (ciphertext) using cryptographic algorithms and keys. Only authorized parties with the correct decryption key can read the original data.

**Data in Transit (Network Encryption):**

Data transmitted between nodes in a distributed database travels over networks that may be intercepted. Encryption protects against eavesdropping and man-in-the-middle attacks.

- **TLS/SSL:** Transport Layer Security encrypts all data transmitted between client and server, or between database nodes. The connection is established with a handshake that authenticates the server (and optionally the client) and negotiates encryption keys.
- **IPsec:** Encrypts all IP-layer traffic between two hosts, providing network-level encryption without modifying the application.

**Data at Rest (Storage Encryption):**

Data stored on disk at each site must be protected against physical theft or unauthorized disk access.

- **Transparent Data Encryption (TDE):** The DBMS automatically encrypts data when writing to disk and decrypts when reading into memory. The application does not need to handle encryption/decryption logic.
- **Column-level Encryption:** Only specific sensitive columns (e.g., credit card numbers, medical records) are encrypted. Provides granular control but adds overhead for encrypted column access.

**Key Management:** Encryption is only as secure as the key management system. Keys must be stored separately from the encrypted data, rotated periodically, and protected against unauthorized access. Hardware Security Modules (HSMs) are often used for key storage in production systems.

## 4.6.4 Integrity

Integrity ensures that data remains accurate, consistent, and unaltered throughout its lifecycle — during storage, processing, and transmission. It answers the question: "Has the data been tampered with?"

**Threats to Integrity:**
- Unauthorized modification of data during network transmission.
- Corruption of data at rest due to hardware failure or malicious activity.
- Inconsistency between replicas due to failed synchronization.

**Mechanisms:**

1. **Checksums and Hash Functions:** A cryptographic hash (e.g., SHA-256) is computed over data before transmission or storage. The receiver recomputes the hash and compares it. Any modification, even a single bit change, produces a different hash.
2. **Digital Signatures:** The sender signs data with a private key. The receiver verifies the signature with the sender's public key. This guarantees both integrity (data not modified) and authenticity (data came from the claimed sender).
3. **Referential Integrity Constraints:** Foreign key constraints and CHECK constraints in the database schema prevent invalid data from being inserted.
4. **Distributed Commit Protocols:** Protocols like 2PC ensure that distributed transactions either fully commit or fully abort, maintaining transactional integrity across sites.
5. **Consensus Protocols:** Paxos and Raft ensure that all replicas agree on the same sequence of operations, maintaining consistency and integrity across the distributed system.
6. **Audit Trails:** Logging all data modifications (who changed what, when, and from where) allows detection of unauthorized changes and supports forensic investigation.

**Best Practices for Distributed Database Security:**

1. **Defense in Depth:** Combine authentication, authorization, encryption, and integrity mechanisms in layers. No single mechanism is sufficient.
2. **Least Privilege Principle:** Grant users and applications only the minimum privileges necessary for their tasks.
3. **Consistent Policy Enforcement:** Ensure security policies are applied uniformly across all nodes in the distributed system to prevent weak-link attacks.
4. **Regular Auditing:** Monitor and log access patterns, failed authentication attempts, and privilege escalations.
5. **Encryption Everywhere:** Encrypt data both in transit and at rest. Use mutual TLS for inter-node communication.
