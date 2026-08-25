# 8. Emerging Trends

# 8.1 Cloud Database

> **Write short notes on: Cloud Database [5 marks] (2080)**

A cloud database is a database that is deployed, delivered, and accessed through a cloud computing platform rather than running on local, on-premises hardware. The cloud provider manages the underlying infrastructure — servers, storage, networking, backups, patching, and scaling — while the user interacts with the database through APIs, management consoles, or standard connection protocols.

**Deployment Models:**

1. **Virtual Machine-Based:** The user provisions a virtual machine on a cloud platform (e.g., AWS EC2, Azure VM) and installs and manages the database software manually. The user retains full control over configuration but is responsible for maintenance, patching, and backups.

2. **Database-as-a-Service (DBaaS):** The cloud provider fully manages the database engine. The user only interacts with the database through queries and a management interface. The provider handles provisioning, scaling, replication, backups, and failover automatically. This is the dominant model in modern cloud computing.

**Types of Cloud Databases:**

1. **Cloud Relational Databases:** Traditional SQL databases offered as managed services. They support ACID transactions, SQL queries, and structured schemas. Examples: Amazon RDS (supports MySQL, PostgreSQL, Oracle, SQL Server), Azure SQL Database, Google Cloud SQL.

2. **Cloud NoSQL Databases:** Managed NoSQL services offering flexible schemas and horizontal scalability. Examples: Amazon DynamoDB (key-value), Azure Cosmos DB (multi-model: document, key-value, graph, column-family), Google Cloud Firestore (document).

3. **Cloud Data Warehouses:** Designed for analytical workloads (OLAP) with massive parallelism and columnar storage. Examples: Amazon Redshift, Google BigQuery, Snowflake.

**Key Characteristics of Cloud Databases:**

1. **Elastic Scalability:** Resources (compute, storage) can be scaled up or down on demand without downtime. Horizontal scaling (adding more nodes) and vertical scaling (upgrading instance size) are both supported.

2. **High Availability:** Cloud providers offer built-in replication across multiple availability zones (AZs) or regions. If one data center fails, traffic is automatically routed to a replica in another zone, achieving uptimes of 99.99% or higher.

3. **Pay-as-You-Go Pricing:** Users pay only for the resources consumed (compute hours, storage GB, I/O operations) rather than investing in upfront hardware. This shifts database costs from capital expenditure (CapEx) to operational expenditure (OpEx).

4. **Managed Operations:** The provider automates routine administration tasks: automated backups with point-in-time recovery, automatic software patching, monitoring and alerting, and security updates.

5. **Global Distribution:** Multi-region replication allows data to be placed physically closer to users worldwide, reducing read latency. Azure Cosmos DB, for instance, supports automatic multi-region writes with tunable consistency levels.

**Cloud Database vs. On-Premises Database:**

| Aspect | On-Premises | Cloud Database |
|---|---|---|
| Infrastructure | Self-managed hardware | Provider-managed |
| Scaling | Manual (buy and install hardware) | Elastic (on-demand) |
| Cost Model | High upfront CapEx | Pay-as-you-go OpEx |
| Maintenance | DBA handles patching, backups | Automated by provider |
| Availability | Requires custom HA setup | Built-in multi-AZ replication |
| Latency | Low for co-located apps | Depends on region; can be optimized |
| Control | Full control | Limited to provider's options |

---

# 8.2 Serverless Databases

> **Explain the concepts of vector databases, edge databases, and serverless databases. Compare their architectures, use cases, and advantages, and discuss how they differ from traditional database systems. [8 marks] (2082)**

A serverless database is a cloud database that automatically provisions, scales, and manages compute resources based on actual workload demand, without requiring the user to configure, manage, or pay for idle server capacity. The user interacts only with the database endpoint; the infrastructure is entirely abstracted away.

**How Serverless Databases Work:**

In a traditional managed database (e.g., Amazon RDS), the user must choose an instance size (e.g., 4 vCPUs, 16 GB RAM) and pays for that instance whether it is fully utilized or completely idle. In a serverless database, the system automatically allocates compute capacity when queries arrive and releases it when the workload drops. Some serverless databases can even scale to zero during periods of inactivity, meaning no compute charges are incurred when there is no traffic.

**Architecture:**

Serverless databases decouple compute from storage. Storage is typically provisioned independently and persists regardless of compute activity. When a query arrives, the serverless layer spins up the necessary compute resources, executes the query, and then scales down. This decoupling allows compute and storage to scale independently.

```
Client Request → API Gateway / Endpoint
    → Serverless Compute Layer (auto-scales)
        → Persistent Storage Layer (independent)
```

**Examples:**

1. **Amazon Aurora Serverless v2:** A MySQL/PostgreSQL-compatible relational database that auto-scales compute in Aurora Capacity Units (ACUs). It scales in fractions of a second based on real-time load. Minimum capacity is 0.5 ACU (does not scale to zero). Pricing is per ACU-hour plus storage and I/O.

2. **CockroachDB Serverless (Basic):** A distributed SQL database built on Raft consensus. It can scale to zero during idle periods. Pricing is based on Request Units (RUs) that bundle CPU, I/O, and network usage. Includes a free tier.

3. **Google Cloud Firestore:** A serverless, document-oriented NoSQL database that auto-scales to handle millions of concurrent connections. Pricing is per document read, write, and delete plus storage.

4. **Azure Cosmos DB Serverless:** A consumption-based mode for Cosmos DB where charges are based on the Request Units consumed by database operations.

**Advantages:**

1. **Zero Infrastructure Management:** No server provisioning, capacity planning, or manual scaling. The developer focuses entirely on application logic.
2. **Cost Efficiency:** Pay only for actual usage. Ideal for applications with unpredictable or intermittent traffic patterns (e.g., development environments, event-driven applications, startups).
3. **Automatic Scaling:** Handles traffic spikes seamlessly without manual intervention or pre-provisioning.
4. **Faster Time-to-Market:** Eliminates the operational overhead of setting up and managing database infrastructure.

**Limitations:**

1. **Cold Start Latency:** After a period of inactivity (especially if scaled to zero), the first request may experience higher latency as compute resources are provisioned.
2. **Limited Control:** Users have less control over the underlying hardware, network configuration, and fine-tuned performance parameters.
3. **Cost at Scale:** For consistently high workloads, serverless pricing can become more expensive than provisioned (reserved) capacity.
4. **Connection Limits:** Some serverless databases impose limits on concurrent connections or maximum compute capacity.

**Serverless vs. Traditional Database:**

| Aspect | Traditional (Provisioned) | Serverless |
|---|---|---|
| Capacity Planning | Manual (choose instance size) | Automatic |
| Scaling | Manual or auto-scaling with rules | Instant, automatic |
| Idle Cost | Pays for idle capacity | Zero or minimal |
| Cold Start | None (always running) | Possible latency |
| Best For | Steady, predictable workloads | Variable, bursty workloads |

---

# 8.3 Vector Databases for AI/ML

> **Write short notes on: Vector Database [5 marks] (2081, 2080)**
>
> **Explain the concepts of vector databases, edge databases, and serverless databases. [8 marks] (2082)**

A vector database is a specialized database system designed to store, index, and efficiently query high-dimensional vector embeddings. Unlike traditional databases that match data based on exact values or keywords, vector databases find data based on semantic similarity — how close two pieces of data are in meaning.

**Vector Embeddings:**

An embedding is a numerical representation of data (text, image, audio, video) as a dense array of floating-point numbers (a vector). Machine learning models (e.g., transformers like BERT, GPT, or CLIP) convert unstructured data into embeddings such that semantically similar items are represented by vectors that are geometrically close to each other in a high-dimensional space.

Example: The sentences "The cat sat on the mat" and "A kitten rested on the rug" would have embedding vectors that are very close to each other, while "Stock prices rose sharply" would have a distant vector.

```
"The cat sat on the mat"       → [0.12, 0.85, 0.33, ..., 0.67]  (768 dimensions)
"A kitten rested on the rug"   → [0.11, 0.84, 0.35, ..., 0.65]  (close)
"Stock prices rose sharply"    → [0.91, 0.04, 0.78, ..., 0.12]  (far)
```

**Similarity Search and Distance Metrics:**

Vector databases find the k most similar vectors to a given query vector using distance metrics:

1. **Cosine Similarity:** Measures the angle between two vectors, ignoring their magnitude. Two vectors pointing in the same direction have high cosine similarity regardless of length. Best for text/NLP where document length varies.
2. **Euclidean Distance (L2):** Measures the straight-line distance between two points in vector space. Smaller distance means higher similarity. Best when absolute differences between coordinates matter.
3. **Dot Product:** Considers both direction and magnitude. Equivalent to cosine similarity when vectors are L2-normalized. Best when magnitude carries meaning (e.g., user engagement levels).

**Approximate Nearest Neighbor (ANN) Search:**

Computing exact distances between a query vector and every vector in a database of millions or billions of vectors is computationally infeasible. Vector databases use ANN algorithms that trade a small amount of accuracy for orders-of-magnitude speed improvement.

**Indexing Algorithms:**

1. **HNSW (Hierarchical Navigable Small World):** A graph-based algorithm that organizes vectors into a multi-layer graph. Higher layers contain fewer, widely-spaced nodes for fast coarse navigation; lower layers contain more nodes for fine-grained search. Provides very fast query times with high recall. Memory-intensive because the entire graph must reside in memory.

2. **IVF (Inverted File Index):** A clustering-based algorithm that partitions the vector space into clusters (Voronoi cells) using k-means. At query time, only the nearest clusters are searched instead of the entire dataset. Memory-efficient and effective for very large datasets, but requires a training step to build clusters.

3. **Product Quantization (PQ):** Compresses vectors by splitting them into sub-vectors and quantizing each independently. Dramatically reduces memory usage at the cost of some accuracy. Often combined with IVF (IVF-PQ) for large-scale deployments.

**Popular Vector Databases:**

1. **Pinecone:** Fully managed, serverless vector database. Easiest to deploy (no infrastructure management). Suitable for teams wanting rapid integration.
2. **Milvus:** Open-source, distributed vector database designed for billion-scale datasets. Kubernetes-native, highly modular. Suitable for large-scale production deployments.
3. **Weaviate:** Open-source, supports hybrid search (combining vector similarity with keyword filtering). Includes built-in vectorization modules.
4. **Qdrant:** Open-source, written in Rust, optimized for performance. Supports filtering and payload-based search alongside vector similarity.
5. **ChromaDB:** Lightweight, open-source, designed for AI application prototyping and development.

**Use Cases in AI/ML:**

1. **Retrieval-Augmented Generation (RAG):** In a RAG pipeline, a user's query is converted to a vector, and the vector database retrieves the most semantically relevant documents. These documents are then fed to a large language model (LLM) as context to generate an accurate, grounded response.
2. **Semantic Search:** Searching by meaning rather than exact keywords. A query for "affordable electric vehicles" can retrieve documents about "budget-friendly EVs" even if those exact words do not appear.
3. **Recommendation Systems:** Finding items (products, music, videos) similar to a user's preferences by comparing embedding vectors.
4. **Image and Audio Retrieval:** Converting images or audio clips to embeddings and finding visually or acoustically similar content.
5. **Anomaly Detection:** Identifying data points whose embeddings are far from all cluster centers, indicating outliers.

**Vector Database vs. Traditional Database:**

| Aspect | Traditional (Relational/NoSQL) | Vector Database |
|---|---|---|
| Data Type | Structured rows/columns, documents | High-dimensional vectors |
| Query Type | Exact match, range, join | Similarity search (nearest neighbors) |
| Indexing | B-tree, hash, bitmap | HNSW, IVF, PQ |
| Primary Use | Transactional (OLTP), analytical (OLAP) | AI/ML, semantic search, recommendations |
| Search Basis | Keyword or value matching | Semantic meaning (distance in vector space) |

---

# 8.4 Edge Databases (IoT Applications)

> **Write short notes on: Edge Database [5 marks] (2081)**
>
> **Explain the concepts of vector databases, edge databases, and serverless databases. [8 marks] (2082)**

An edge database is a lightweight database deployed at or near the physical location where data is generated — on IoT devices, gateways, factory floors, vehicles, or local servers — rather than in a centralized cloud data center. The goal is to enable real-time data processing, reduce latency, conserve bandwidth, and maintain functionality even when the network connection to the cloud is unreliable or unavailable.

**Why Edge Databases Are Needed:**

In traditional architectures, all data from IoT sensors and devices is transmitted to a centralized cloud database for storage and processing. This creates several problems:

1. **Latency:** Round-trip time to a distant cloud data center can be tens to hundreds of milliseconds — unacceptable for time-critical applications like autonomous vehicles or industrial safety systems.
2. **Bandwidth Cost:** IoT devices generate massive volumes of data. Transmitting all raw data to the cloud is expensive and often unnecessary.
3. **Connectivity:** Edge devices may operate in environments with intermittent, unreliable, or no internet connectivity (e.g., remote oil rigs, underground mines, moving vehicles).
4. **Privacy and Sovereignty:** Regulations may require sensitive data (e.g., medical records, surveillance footage) to remain within a specific geographic boundary.

**Edge-Fog-Cloud Architecture:**

Edge databases typically operate within a three-tier architecture:

1. **Edge Layer (Perception):** IoT sensors and devices collect raw data (temperature, vibration, images, GPS coordinates). An embedded edge database stores this data locally for immediate processing.
2. **Fog Layer (Gateway):** Local gateway servers aggregate data from multiple edge devices, perform filtering, pre-processing, and time-sensitive analytics. They run a more capable edge database that stores aggregated results.
3. **Cloud Layer:** Receives only summarized, filtered, or critical data from the fog layer. Performs long-term storage, complex analytics, model training, and dashboard visualizations.

```
[IoT Sensors] → [Edge DB on Device/Gateway] → [Fog Layer] → [Cloud DB]
       ↑                    ↑                       ↑              ↑
  Raw data          Local processing          Aggregation    Long-term storage
  collected         & immediate action        & filtering    & global analytics
```

**Characteristics of Edge Databases:**

1. **Lightweight Footprint:** Designed to run on resource-constrained hardware (limited CPU, memory, and storage). Examples include SQLite (embedded relational), LiteDB (embedded document store), and CouchDB Lite (mobile/edge sync).
2. **Offline-First Operation:** The database operates independently even without a network connection. Data is stored locally and synchronized with the cloud when connectivity is restored.
3. **Data Synchronization:** Edge databases support bidirectional sync with a central cloud database. Conflict resolution strategies (last-write-wins, merge, or custom rules) handle concurrent updates from multiple edge nodes.
4. **Low Latency:** Queries execute locally against data stored on the device itself, eliminating network round-trip time. Response times are typically sub-millisecond.
5. **Data Filtering and Reduction:** Only relevant, aggregated, or anomalous data is transmitted to the cloud, reducing bandwidth consumption by orders of magnitude.

**Edge Database Technologies:**

1. **SQLite:** The most widely deployed embedded relational database. Zero-configuration, serverless, single-file storage. Used in mobile devices, IoT gateways, and embedded systems.
2. **CouchDB Lite / PouchDB:** Document-oriented edge databases with built-in sync capabilities to a central CouchDB or Cloudant instance.
3. **InfluxDB Edge:** A time-series database optimized for IoT sensor data at the edge.
4. **Azure SQL Edge:** A containerized SQL engine optimized for IoT and edge deployments, with built-in streaming and time-series capabilities.

**Use Cases:**

1. **Autonomous Vehicles:** On-board databases process LiDAR, camera, and radar data in real time for navigation decisions that cannot tolerate cloud latency.
2. **Industrial IoT (Predictive Maintenance):** Edge databases on factory machines store vibration and temperature data locally. Anomaly detection algorithms run on the gateway to trigger immediate shutdowns before equipment failure.
3. **Smart Retail:** Point-of-sale systems and inventory trackers run local databases to ensure operations continue during network outages, syncing with the central system when connectivity returns.
4. **Healthcare Monitoring:** Wearable devices store patient vitals locally, enabling continuous monitoring in remote areas and syncing with hospital systems periodically.

**Edge Database vs. Cloud Database:**

| Aspect | Cloud Database | Edge Database |
|---|---|---|
| Location | Centralized data center | Near data source (device/gateway) |
| Latency | Higher (network round-trip) | Very low (local access) |
| Connectivity | Requires stable internet | Works offline |
| Compute Resources | Abundant | Constrained |
| Data Volume | Full dataset | Subset / recent data |
| Analytics | Complex, global | Simple, real-time, local |
| Sync | N/A | Syncs with cloud periodically |

---

# 8.5 Ethical Considerations in Database Engineering

Ethical considerations in database engineering address the responsibilities of database professionals to design, implement, and manage data systems in ways that respect individual rights, prevent harm, and comply with legal and societal norms.

## 8.5.1 Data Privacy

Data privacy is the right of individuals to control how their personal information is collected, stored, used, and shared. Database engineers must design systems that protect this right by default.

**Key Privacy Principles:**

1. **Data Minimization:** Collect and store only the data that is strictly necessary for the stated purpose. Avoid retaining data "just in case" it might be useful later.
2. **Purpose Limitation:** Data collected for one purpose must not be used for a different, incompatible purpose without explicit consent.
3. **Consent and Transparency:** Users must be informed about what data is collected and how it is used, and must provide meaningful consent.

**Privacy-by-Design Techniques:**

1. **Encryption:** Data must be encrypted both at rest (stored on disk) and in transit (transmitted over a network). This prevents unauthorized access even if physical storage or network traffic is intercepted.
2. **Anonymization:** Removing or obfuscating personally identifiable information (PII) so that individuals cannot be re-identified from the data. Used for analytics and research datasets.
3. **Pseudonymization:** Replacing direct identifiers (name, ID) with artificial identifiers (pseudonyms). The mapping between pseudonyms and real identities is stored separately and protected. Unlike anonymization, pseudonymization is reversible with the mapping key.
4. **Access Control:** Implementing role-based access control (RBAC) to ensure that users can only access the data they are authorized to see. The principle of least privilege grants users the minimum permissions necessary for their role.
5. **Audit Logging:** Maintaining detailed logs of who accessed what data, when, and why. Audit trails support accountability and regulatory compliance.

**GDPR (General Data Protection Regulation):**

GDPR is a European Union regulation that imposes strict rules on how organizations handle personal data of EU residents. Key requirements relevant to database engineering:

1. **Right to Access:** Individuals can request a copy of all personal data an organization holds about them.
2. **Right to Erasure (Right to be Forgotten):** Individuals can request deletion of their personal data. The database system must be able to locate and permanently delete all records associated with a specific individual, including from backups and replicas.
3. **Data Breach Notification:** Organizations must notify the relevant authority within 72 hours of discovering a data breach.
4. **Data Portability:** Individuals can request their data in a machine-readable format for transfer to another service.

## 8.5.2 Bias and Fairness

Databases that feed into machine learning models or automated decision-making systems can perpetuate or amplify societal biases if the underlying data is unrepresentative or historically skewed.

**Sources of Bias:**

1. **Historical Bias:** The data reflects past discriminatory practices. For example, a hiring database that underrepresents women in engineering roles can train a model that penalizes female applicants.
2. **Sampling Bias:** The data collection process systematically excludes certain groups. For example, a health database built primarily from urban hospitals may not represent rural populations.
3. **Measurement Bias:** The way data is recorded differs across groups. For example, certain medical conditions may be under-diagnosed in specific demographics.

**Mitigation Strategies:**

1. **Representative Data Collection:** Ensuring that training datasets include proportional representation of all relevant demographic groups.
2. **Bias Auditing:** Regularly analyzing database contents and query results for disparate impact on protected attributes (race, gender, age, disability).
3. **Fairness Constraints:** Incorporating fairness metrics into systems that use the data for automated decisions, ensuring that outcomes do not disproportionately disadvantage any group.

## 8.5.3 Data Sovereignty

Data sovereignty is the principle that data is subject to the laws and governance structures of the country or region where it is physically stored or processed. This is a critical concern for globally distributed database systems.

**Challenges:**

1. **Conflicting Regulations:** Different countries have different (and sometimes contradictory) data protection laws. Data stored in one jurisdiction may be subject to government access requests that conflict with the privacy laws of another jurisdiction.
2. **Cross-Border Transfers:** Transferring data between regions may violate local regulations. For example, GDPR restricts transferring EU residents' data to countries without "adequate" data protection laws.
3. **Cloud Provider Jurisdiction:** Data stored in a cloud provider's data center is subject to the laws of the country where that data center is located, which may differ from the laws applicable to the data's owner or subjects.

**Engineering Responses:**

1. **Geographic Data Sharding:** Partitioning data so that records belonging to users in a specific region are stored exclusively in data centers within that region.
2. **Data Residency Policies:** Configuring database replication to ensure that replicas do not cross jurisdictional boundaries.
3. **Customer-Managed Encryption Keys:** Allowing customers to control their own encryption keys so that the cloud provider cannot decrypt the data, even if compelled by a government request.

## 8.5.4 Accountability and Transparency

1. **Data Lineage:** Tracking where data originates, how it has been transformed, and where it flows. This enables organizations to trace errors or biases back to their source.
2. **Explainability:** When databases feed automated decision-making systems, the decisions must be explainable. Database engineers should ensure that the data supporting a decision can be retrieved and audited.
3. **Retention Policies:** Defining and enforcing how long data is retained before it is automatically deleted. Retaining data indefinitely increases risk and may violate regulations.
