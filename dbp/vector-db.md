# Vector Database Complete Guide

![Bidur Sapkota](https://www.bidursapkota.com.np/images/gravatar.webp "Bidur Sapkota - Developer")&nbsp;[Bidur Sapkota](https://www.bidursapkota.com.np/)

![Vector Database Complete Guide by Bidur Sapkota](vector-db-1200.webp "Vector Database Complete Guide – Blog by Bidur Sapkota")

## Table of Contents

1. [Introducing Vector Databases](#introducing-vector-databases)
2. [Understanding Embeddings](#understanding-embeddings)
3. [How Vector Search Works](#how-vector-search-works)
4. [Similarity Metrics](#similarity-metrics)
5. [Indexing Algorithms](#indexing-algorithms)
6. [Popular Vector Databases](#popular-vector-databases)
7. [Getting Started with ChromaDB](#getting-started-with-chromadb)
8. [CRUD Operations in ChromaDB](#crud-operations-in-chromadb)
9. [Querying & Filtering](#querying--filtering)
10. [Integrating with LLMs (RAG)](#integrating-with-llms-rag)
11. [Getting Started with Pinecone](#getting-started-with-pinecone)
12. [CRUD Operations in Pinecone](#crud-operations-in-pinecone)
13. [Performance & Optimization](#performance--optimization)
14. [Vector Database vs Traditional Database](#vector-database-vs-traditional-database)

---

## Introducing Vector Databases

A vector database is a specialized database designed to store, index, and query high-dimensional vectors (embeddings). Unlike traditional databases that search by exact matches or keyword lookups, vector databases find results based on semantic similarity. They answer the question "what is most similar to this?" rather than "what exactly matches this?".

Traditional databases store structured data in rows and columns and retrieve records using exact-match queries like SQL `WHERE` clauses. Vector databases store numerical representations of data (vectors) and retrieve records using mathematical distance calculations. This makes them essential for AI applications where meaning matters more than exact keywords.

Common use cases for vector databases are:

- **Semantic Search**: Finding documents by meaning rather than keyword matching. A search for "happy dog" can return results about "joyful puppy" because their vector representations are similar.
- **Recommendation Systems**: Suggesting products, songs, or articles similar to ones a user already likes by comparing their vector representations.
- **Retrieval-Augmented Generation (RAG)**: Feeding relevant context to large language models (LLMs) by retrieving semantically similar documents from a vector store before generating a response.
- **Image & Audio Search**: Finding visually or acoustically similar media by comparing their embedding vectors.
- **Anomaly Detection**: Identifying data points that are far from any cluster in vector space, signaling unusual behavior.

---

## Understanding Embeddings

An embedding is a numerical representation of data (text, images, audio) as a list of floating-point numbers called a vector. Embedding models convert unstructured data into dense vectors that capture semantic meaning. Similar concepts end up close together in vector space, while dissimilar concepts are far apart.

For example, the sentence "The cat sat on the mat" might be represented as a vector like `[0.12, -0.45, 0.78, ..., 0.33]` with hundreds or thousands of dimensions. The sentence "A kitten rested on the rug" would produce a vector that is numerically close to the first one because the meanings are similar.

### How Embeddings Are Generated

First, install the OpenAI package and set your API key:

```bash
pip install openai
export OPENAI_API_KEY="your-api-key-here"
```

```python
# Using OpenAI's embedding model
from openai import OpenAI

client = OpenAI()

response = client.embeddings.create(
    input="The cat sat on the mat",
    model="text-embedding-3-small"           # 1536-dimensional vectors
)

vector = response.data[0].embedding          # List of 1536 floats
print(len(vector))                           # 1536
print(vector[:5])                            # First 5 dimensions
```

`client.embeddings.create()` sends text to OpenAI's API and returns its vector representation. `text-embedding-3-small` produces 1536-dimensional vectors. Each dimension captures some aspect of the text's meaning. The full vector is a list of floating-point numbers.

### Using Open-Source Models

Install the sentence-transformers library:

```bash
pip install sentence-transformers
```

```python
# Using sentence-transformers (runs locally, no API key needed)
from sentence_transformers import SentenceTransformer

# all-MiniLM-L6-v2 is a great, lightweight model (384 dimensions)
model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "The cat sat on the mat",
    "A kitten rested on the rug",
    "The stock market crashed today"
]

embeddings = model.encode(sentences)

vector = embeddings[0]
print(len(vector))                          # 384
print(vector[:5])                           # First 5 dimensions
print(embeddings.shape)                     # (3, 384)
```

`SentenceTransformer` loads a pre-trained model that runs entirely on your machine. `all-MiniLM-L6-v2` produces 384-dimensional vectors and is fast enough for most applications. `model.encode()` accepts a single string or a list of strings and returns a NumPy array of embeddings.

### Key Properties of Embeddings

| Property         | Description                                                        |
| ---------------- | ------------------------------------------------------------------ |
| Dimensionality   | The number of values in each vector (e.g., 384, 768, 1536)         |
| Semantic Meaning | Similar meanings produce vectors that are close together in space  |
| Model-Dependent  | Different models produce different embeddings for the same input   |
| Fixed Length     | Every input produces a vector of the same length for a given model |

---

## How Vector Search Works

Vector search (also called nearest neighbor search) finds the vectors in a database that are closest to a given query vector. The process has three main steps: embed the query, compute distances, and return the top results.

### Step-by-Step Process

1. **Embed the query**: Convert the user's query (text, image, etc.) into a vector using the same embedding model that was used to embed the stored data.
2. **Compare against stored vectors**: Calculate the distance or similarity between the query vector and every stored vector.
3. **Return top-k results**: Sort by distance and return the k nearest vectors along with their associated metadata and documents.

### Brute-Force Search

Install NumPy for fast mathematical operations:

```bash
pip install numpy
```

```python
import numpy as np

# Stored vectors (imagine thousands of these)
database_vectors = np.array([
    [0.1, 0.3, 0.5],
    [0.9, 0.1, 0.2],
    [0.15, 0.28, 0.48],
])

query_vector = np.array([0.12, 0.30, 0.50])

# Calculate Euclidean distance to every vector
distances = np.linalg.norm(database_vectors - query_vector, axis=1)

# Find the index of the closest vector
nearest_index = np.argmin(distances)
print(f"Nearest vector index: {nearest_index}")    # 0
print(f"Distance: {distances[nearest_index]:.4f}") # 0.0200
```

`np.linalg.norm(..., axis=1)` calculates the Euclidean distance between the query and each stored vector. `np.argmin` returns the index of the smallest distance. Brute-force search compares the query against every vector in the database. This is accurate but slow for large datasets because the time grows linearly with the number of vectors.

### Approximate Nearest Neighbor (ANN) Search

Brute-force becomes impractical when you have millions of vectors. Approximate Nearest Neighbor (ANN) algorithms trade a small amount of accuracy for a large gain in speed. Instead of comparing against every vector, ANN algorithms use data structures like graphs, trees, or hashed indices to narrow the search space. The result may not always be the absolute nearest neighbor, but it is close enough and orders of magnitude faster.

---

## Similarity Metrics

A similarity metric defines how "closeness" between two vectors is measured. The choice of metric affects search results and should match the embedding model's training objective.

### Euclidean Distance (L2)

Measures the straight-line distance between two points in vector space. Smaller values mean more similar.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

distance = np.linalg.norm(a - b)
print(distance)                              # 5.196
```

`np.linalg.norm(a - b)` computes the square root of the sum of squared differences: √((4-1)² + (5-2)² + (6-3)²) = √27 ≈ 5.196. Euclidean distance works well when the magnitude of vectors matters.

### Cosine Similarity

Measures the angle between two vectors, ignoring their magnitude. Values range from -1 (opposite) to 1 (identical direction). Higher values mean more similar.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

cosine_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(cosine_sim)                            # 0.9746
```

`np.dot(a, b)` computes the dot product. Dividing by the product of the norms normalizes the result. Cosine similarity is the most common metric for text embeddings because it focuses on the direction (meaning) rather than the length (magnitude) of vectors.

### Dot Product (Inner Product)

Measures both the angle and magnitude of two vectors. Larger values mean more similar. Often used with normalized vectors where it becomes equivalent to cosine similarity.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot = np.dot(a, b)
print(dot)                                   # 32
```

When vectors are normalized (unit length), dot product and cosine similarity produce the same ranking.

### Comparison

| Metric            | Range   | Best When                                |
| ----------------- | ------- | ---------------------------------------- |
| Euclidean (L2)    | [0, ∞)  | Magnitude matters; spatial data          |
| Cosine Similarity | [-1, 1] | Only direction matters; text embeddings  |
| Dot Product       | (-∞, ∞) | Vectors are normalized; fast computation |

---

## Indexing Algorithms

Indexing algorithms organize vectors for fast retrieval. Without an index, every query requires comparing against all stored vectors (brute-force). Indexes create data structures that drastically reduce the number of comparisons needed.

### HNSW (Hierarchical Navigable Small World)

HNSW builds a multi-layered graph where each vector is a node connected to its nearest neighbors. The top layer has few nodes and long-range connections for fast navigation. Lower layers have more nodes and short-range connections for precision. Searching starts at the top layer and moves down, narrowing the search at each level.

HNSW offers excellent query speed and high recall (accuracy). It is the most popular index for in-memory vector databases. The trade-off is higher memory usage because the graph structure must be stored alongside the vectors.

### IVF (Inverted File Index)

IVF partitions the vector space into clusters using k-means clustering. Each cluster has a centroid. During a search, the query is compared to the centroids first, and then only the vectors in the closest clusters are searched. The parameter `nprobe` controls how many clusters to search.

IVF uses less memory than HNSW but requires a training step to build the clusters. Increasing `nprobe` improves accuracy but slows the search.

### PQ (Product Quantization)

PQ compresses vectors by splitting each vector into sub-vectors and quantizing each sub-vector independently. This dramatically reduces memory usage at the cost of some accuracy. PQ is often combined with IVF (IVF-PQ) for large-scale deployments where memory is constrained.

### Comparison

| Algorithm | Speed     | Memory   | Accuracy  | Best For                        |
| --------- | --------- | -------- | --------- | ------------------------------- |
| Flat      | Slow      | Low      | Exact     | Small datasets (< 10k vectors)  |
| IVF       | Fast      | Medium   | High      | Medium datasets with training   |
| HNSW      | Very Fast | High     | Very High | Real-time applications          |
| IVF-PQ    | Fast      | Very Low | Moderate  | Billions of vectors, low memory |

---

## Popular Vector Databases

| Database | Type        | Hosting      | Key Feature                                    |
| -------- | ----------- | ------------ | ---------------------------------------------- |
| ChromaDB | Embedded    | Local / Self | Lightweight, easy to start, Python-native      |
| Pinecone | Managed     | Cloud        | Fully managed, serverless, no infra to manage  |
| Weaviate | Open Source | Self / Cloud | GraphQL API, built-in vectorizers              |
| Milvus   | Open Source | Self / Cloud | High performance, distributed, billion-scale   |
| Qdrant   | Open Source | Self / Cloud | Rust-based, fast, rich filtering               |
| pgvector | Extension   | Self / Cloud | Vector search inside PostgreSQL                |
| FAISS    | Library     | Local        | Facebook's library, research-grade performance |

**ChromaDB** is the easiest way to get started. It runs embedded in your Python process with no server setup required. It is ideal for prototyping, small to medium applications, and learning vector database concepts.

**Pinecone** is a fully managed cloud service. You do not need to worry about infrastructure, scaling, or maintenance. It is ideal for production applications where you want to focus on building features rather than managing databases.

---

## Getting Started with ChromaDB

ChromaDB is an open-source, embedded vector database that runs directly in your Python process. It handles embedding generation, storage, indexing, and querying with minimal configuration.

### Installation

```bash
pip install chromadb
```

### Creating a Client

```python
import chromadb

# In-memory client (data lost when process ends)
client = chromadb.Client()

# Persistent client (data saved to disk)
client = chromadb.PersistentClient(path="./chroma_data")
```

`chromadb.Client()` creates an ephemeral in-memory database, useful for testing. `PersistentClient` saves data to the specified directory so it survives process restarts. The `path` parameter specifies where ChromaDB stores its data files.

### Collections

A collection in ChromaDB is like a table in a traditional database. Each collection stores vectors along with their associated documents and metadata.

```python
# Create or get a collection
collection = client.get_or_create_collection(
    name="my_documents",
    metadata={"hnsw:space": "cosine"}        # Use cosine similarity
)

# List all collections
collections = client.list_collections()

# Delete a collection
client.delete_collection(name="my_documents")
```

`get_or_create_collection` returns an existing collection or creates a new one if it does not exist. `metadata={"hnsw:space": "cosine"}` configures the collection to use cosine similarity for distance calculations. Other options are `l2` (Euclidean, the default) and `ip` (inner product).

---

## CRUD Operations in ChromaDB

### Adding Documents

```python
collection.add(
    ids=["doc1", "doc2", "doc3"],
    documents=[
        "Python is a programming language",
        "JavaScript runs in the browser",
        "Docker containers package applications"
    ],
    metadatas=[
        {"source": "wiki", "category": "python"},
        {"source": "docs", "category": "javascript"},
        {"source": "blog", "category": "devops"}
    ]
)
```

`ids` must be unique strings for each document. `documents` are the raw text strings. ChromaDB automatically generates embeddings from the documents using its default embedding model (`all-MiniLM-L6-v2`). `metadatas` are optional key-value pairs attached to each document for filtering.

### Adding Pre-Computed Embeddings

```python
collection.add(
    ids=["vec1", "vec2"],
    embeddings=[
        [0.1] * 1536,                       # 1536-dimensional vector
        [0.2] * 1536                        # Another vector
    ],
    documents=["First document", "Second document"],
    metadatas=[{"type": "manual"}, {"type": "manual"}]
)
```

If you generate embeddings yourself (using OpenAI, sentence-transformers, etc.), pass them via the `embeddings` parameter. When both `documents` and `embeddings` are provided, ChromaDB stores the documents but uses your provided embeddings instead of generating its own.

### Updating Documents

```python
collection.update(
    ids=["doc1"],
    documents=["Python is a versatile programming language"],
    metadatas=[{"source": "wiki", "category": "python", "updated": True}]
)
```

`update` replaces the document, metadata, and embedding for the specified IDs. ChromaDB re-generates the embedding from the new document text.

### Upserting Documents

```python
collection.upsert(
    ids=["doc1", "doc4"],
    documents=[
        "Python is widely used in data science",
        "Rust is a systems programming language"
    ],
    metadatas=[
        {"source": "wiki", "category": "python"},
        {"source": "docs", "category": "rust"}
    ]
)
```

`upsert` updates existing documents (matched by ID) and inserts new ones that do not exist. It is a combination of update and insert.

### Getting Documents by ID

```python
results = collection.get(
    ids=["doc1", "doc2"],
    include=["documents", "metadatas", "embeddings"]
)

print(results["documents"])                  # List of document texts
print(results["metadatas"])                  # List of metadata dicts
```

`get` retrieves documents by their exact IDs. The `include` parameter specifies which fields to return. By default, `get` returns documents and metadatas but not embeddings.

### Deleting Documents

```python
# Delete by IDs
collection.delete(ids=["doc1", "doc2"])

# Delete by filter
collection.delete(where={"category": "devops"})
```

`delete` removes documents by their IDs or by a metadata filter. Deleting by filter removes all documents that match the condition.

### Counting Documents

```python
count = collection.count()
print(f"Total documents: {count}")
```

---

## Querying & Filtering

### Semantic Query

```python
results = collection.query(
    query_texts=["What programming language is good for data science?"],
    n_results=3,
    include=["documents", "metadatas", "distances"]
)

print(results["documents"][0])               # Top 3 matching documents
print(results["distances"][0])               # Distance scores
print(results["metadatas"][0])               # Metadata of matches
```

`query_texts` is the search query. ChromaDB embeds it and finds the closest stored vectors. `n_results` specifies how many results to return. `distances` contains the similarity scores; lower values mean more similar when using L2 or cosine distance. The results are nested lists because `query_texts` can contain multiple queries at once.

### Metadata Filtering

```python
# Filter by exact match
results = collection.query(
    query_texts=["programming language"],
    n_results=5,
    where={"category": "python"}
)

# Filter with operators
results = collection.query(
    query_texts=["programming"],
    n_results=5,
    where={"source": {"$in": ["wiki", "docs"]}}
)

# Combine multiple conditions
results = collection.query(
    query_texts=["language"],
    n_results=5,
    where={
        "$and": [
            {"category": {"$ne": "devops"}},
            {"source": "wiki"}
        ]
    }
)
```

`where` filters results by metadata before ranking by similarity. `$in` matches any value in the list. `$ne` means "not equal". `$and` requires all conditions to be true. Other operators include `$gt`, `$gte`, `$lt`, `$lte`, and `$or`.

### Document Content Filtering

```python
results = collection.query(
    query_texts=["programming"],
    n_results=5,
    where_document={"$contains": "Python"}
)
```

`where_document` filters by the actual text content of stored documents. `$contains` checks if the document text contains the specified substring. This is a keyword filter applied after the semantic search.

---

## Integrating with LLMs (RAG)

Retrieval-Augmented Generation (RAG) combines vector search with LLMs. Instead of relying solely on the LLM's training data, RAG retrieves relevant documents from a vector database and includes them as context in the prompt. This reduces hallucinations, keeps responses grounded in your data, and lets you update knowledge without retraining the model.

### RAG Architecture

The RAG pipeline has two phases:

1. **Ingestion**: Split documents into chunks, generate embeddings, and store them in a vector database.
2. **Retrieval & Generation**: Embed the user's query, retrieve relevant chunks from the vector database, and pass them as context to the LLM along with the query.

### Complete RAG Example

First, get an API key from Moonshot AI (Kimi) and export it. Kimi provides a generous free usage tier and uses the same API structure as OpenAI.

```bash
export MOONSHOT_API_KEY="your-kimi-api-key"
```

```python
import chromadb
from openai import OpenAI

# Step 1: Set up vector database
chroma_client = chromadb.PersistentClient(path="./rag_data")
collection = chroma_client.get_or_create_collection(name="knowledge_base")

# Step 2: Ingest documents
documents = [
    "FastAPI is a modern Python web framework for building APIs. It is built on Starlette and Pydantic.",
    "Docker containers package applications with their dependencies for consistent deployment.",
    "PostgreSQL is an advanced open-source relational database with ACID compliance.",
    "Redis is an in-memory data store used for caching, session management, and message queuing.",
    "Kubernetes orchestrates containerized applications across a cluster of machines."
]

collection.add(
    ids=[f"doc_{i}" for i in range(len(documents))],
    documents=documents
)

# Step 3: Query and retrieve relevant context
query = "How do I deploy a Python web application?"

results = collection.query(
    query_texts=[query],
    n_results=3
)

context = "\n".join(results["documents"][0])

# Step 4: Generate response with LLM (Using Moonshot AI / Kimi)
import os

openai_client = OpenAI(
    api_key=os.environ.get("MOONSHOT_API_KEY", "your-kimi-api-key"),
    base_url="https://api.moonshot.cn/v1"
)

response = openai_client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=[
        {
            "role": "system",
            "content": f"Answer the question based on the following context:\n\n{context}"
        },
        {
            "role": "user",
            "content": query
        }
    ]
)

print(response.choices[0].message.content)
```

The ingestion phase adds documents to ChromaDB, which automatically generates embeddings. The retrieval phase embeds the user's query and finds the 3 most similar documents. The generation phase sends the retrieved documents as context in the system message to the LLM, which generates an answer grounded in the provided context. This approach lets the LLM answer questions about your specific data without fine-tuning or retraining.

### Chunking Strategies

Large documents should be split into smaller chunks before embedding. A single embedding for an entire book would be too generic. Smaller chunks capture more specific information and produce better search results.

```python
# Simple chunking by character count with overlap
def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

document = "Your very long document text here..."
chunks = chunk_text(document, chunk_size=500, overlap=50)

# Add chunks to collection
collection.add(
    ids=[f"chunk_{i}" for i in range(len(chunks))],
    documents=chunks,
    metadatas=[{"source": "document.pdf", "chunk_index": i} for i in range(len(chunks))]
)
```

`chunk_size` controls how many characters each chunk contains. `overlap` ensures that sentences at chunk boundaries are not cut off and lost. Each chunk is stored with metadata indicating its source and position, so you can trace results back to the original document.

---

## Getting Started with Pinecone

Pinecone is a fully managed, cloud-native vector database. You do not need to set up servers, configure indexes, or manage infrastructure. Pinecone handles scaling, replication, and maintenance automatically.

### Installation

```bash
pip install pinecone
```

### Connecting to Pinecone

First, sign up at [pinecone.io](https://www.pinecone.io/) and get your API key. Then set it as an environment variable:

```bash
export PINECONE_API_KEY="your-api-key-here"
```

```python
import os
from pinecone import Pinecone

# Automatically uses PINECONE_API_KEY environment variable
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
```

`Pinecone()` initializes the client with your API key. You can get a free API key by signing up at [pinecone.io](https://www.pinecone.io/). The free tier includes enough resources for development and small projects.

### Creating an Index

```python
import os
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

pc.create_index(
    name="my-index",
    dimension=1536,                          # Must match your embedding model
    metric="cosine",                         # cosine, euclidean, or dotproduct
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)

index = pc.Index("my-index")
```

`dimension` must match the output dimension of your embedding model (e.g., 1536 for OpenAI's `text-embedding-3-small`). `metric` defines the distance function. `ServerlessSpec` configures the cloud provider and region. Serverless indexes scale automatically and you pay only for what you use.

### Listing and Deleting Indexes

```python
# List all indexes
indexes = pc.list_indexes()
print(indexes)

# Delete an index
pc.delete_index("my-index")
```

### Index Statistics

```python
stats = index.describe_index_stats()
print(stats)                                 # Total vectors, dimension, namespaces
```

`describe_index_stats()` returns information about the index including the total number of vectors and the breakdown by namespace.

---

## CRUD Operations in Pinecone

### Upserting Vectors

```python
index.upsert(
    vectors=[
        {
            "id": "doc1",
            "values": [0.1] * 1536,             # 1536-dimensional vector
            "metadata": {"source": "wiki", "category": "python"}
        },
        {
            "id": "doc2",
            "values": [0.2] * 1536,             # 1536-dimensional vector
            "metadata": {"source": "docs", "category": "javascript"}
        }
    ],
    namespace="my-namespace"
)
```

`upsert` inserts new vectors or updates existing ones (matched by ID). `values` is the embedding vector. `metadata` is a dictionary of key-value pairs for filtering. `namespace` acts like a partition within an index; vectors in different namespaces are isolated from each other.

### Batch Upserting

```python
# For large datasets, upsert in batches
import itertools

def chunks(iterable, batch_size=100):
    it = iter(iterable)
    chunk = list(itertools.islice(it, batch_size))
    while chunk:
        yield chunk
        chunk = list(itertools.islice(it, batch_size))

# Generate 500 dummy embeddings for demonstration
all_embeddings = [[0.1] * 1536 for _ in range(500)]

vectors = [
    {"id": f"vec_{i}", "values": embedding, "metadata": {"index": i}}
    for i, embedding in enumerate(all_embeddings)
]

for batch in chunks(vectors, batch_size=100):
    index.upsert(vectors=batch, namespace="my-namespace")
```

Pinecone recommends upserting in batches of 100 vectors to avoid request size limits and improve throughput. The `chunks` helper function splits the list into smaller batches.

### Querying Vectors

```python
results = index.query(
    vector=[0.1] * 1536,                     # Query embedding
    top_k=5,                                 # Number of results
    include_metadata=True,
    include_values=False,
    namespace="my-namespace"
)

for match in results["matches"]:
    print(f"ID: {match['id']}, Score: {match['score']:.4f}")
    print(f"Metadata: {match['metadata']}")
```

`vector` is the query embedding. `top_k` specifies how many results to return. `include_metadata=True` returns the metadata along with the results. `include_values=False` omits the stored vector values from the response to reduce payload size. `score` is the similarity score; higher is more similar when using cosine or dot product.

### Querying with Metadata Filters

```python
results = index.query(
    vector=[0.1] * 1536,                     # Query embedding
    top_k=5,
    filter={
        "category": {"$eq": "python"},
        "source": {"$in": ["wiki", "docs"]}
    },
    include_metadata=True,
    namespace="my-namespace"
)
```

`filter` narrows results by metadata before ranking by similarity. Supported operators include `$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`, `$in`, and `$nin`.

### Fetching Vectors by ID

```python
results = index.fetch(
    ids=["doc1", "doc2"],
    namespace="my-namespace"
)

for id, vector in results["vectors"].items():
    print(f"ID: {id}")
    print(f"Values: {vector['values'][:5]}...")
    print(f"Metadata: {vector['metadata']}")
```

`fetch` retrieves vectors by their exact IDs without performing a similarity search.

### Deleting Vectors

```python
# Delete by IDs
index.delete(
    ids=["doc1", "doc2"],
    namespace="my-namespace"
)

# Delete by metadata filter
index.delete(
    filter={"category": "devops"},
    namespace="my-namespace"
)

# Delete all vectors in a namespace
index.delete(
    delete_all=True,
    namespace="my-namespace"
)
```

`delete` removes vectors by ID, by metadata filter, or all vectors in a namespace. Deleting by filter removes every vector whose metadata matches the condition. `delete_all=True` clears the entire namespace.

---

## Performance & Optimization

### Dimensionality

Higher-dimensional embeddings capture more nuance but require more storage and slower distance calculations. For most applications, 384 to 1536 dimensions provide a good balance between quality and performance.

| Model                  | Dimensions | Use Case                      |
| ---------------------- | ---------- | ----------------------------- |
| all-MiniLM-L6-v2       | 384        | Fast, good for prototyping    |
| text-embedding-3-small | 1536       | High quality, general purpose |
| text-embedding-3-large | 3072       | Highest quality, more compute |

### Batching

Always insert and query vectors in batches rather than one at a time. Batching reduces network overhead and improves throughput.

```python
# Bad: one at a time
for doc in documents:
    collection.add(ids=[doc.id], documents=[doc.text])

# Good: batch insert
collection.add(
    ids=[doc.id for doc in documents],
    documents=[doc.text for doc in documents]
)
```

### Metadata Design

Keep metadata values simple and filterable. Use strings, numbers, and booleans. Avoid nesting complex objects in metadata. Design your metadata schema around the filters you will use in queries.

```python
# Good metadata design
metadata = {
    "source": "documentation",
    "language": "python",
    "version": 3.14,
    "is_deprecated": False
}

# Avoid complex nested structures
metadata = {
    "info": {"nested": {"deeply": "value"}}    # Hard to filter
}
```

### Chunking Best Practices

- **Chunk size**: 200 to 1000 characters is typical. Smaller chunks are more precise but produce more vectors. Larger chunks capture more context but may dilute the meaning.
- **Overlap**: 10% to 20% overlap prevents information loss at chunk boundaries.
- **Respect boundaries**: Split at sentence or paragraph boundaries rather than mid-sentence whenever possible.

---

## Vector Database vs Traditional Database

| Feature        | Traditional Database (SQL)     | Vector Database                         |
| -------------- | ------------------------------ | --------------------------------------- |
| Data Model     | Tables with rows and columns   | Vectors with metadata                   |
| Query Type     | Exact match (WHERE, JOIN)      | Similarity search (nearest neighbor)    |
| Search Method  | B-tree, hash indexes           | ANN indexes (HNSW, IVF)                 |
| Best For       | Structured, transactional data | Unstructured data (text, images, audio) |
| Query Language | SQL                            | SDK / API calls                         |
| Scalability    | Vertical (scale up)            | Horizontal (scale out)                  |
| Example Query  | "Find user with ID 42"         | "Find documents similar to this text"   |

Traditional databases answer "give me exactly this record." Vector databases answer "give me the most similar records." In practice, modern applications often use both: a traditional database for transactional data and a vector database for semantic search and AI features.
