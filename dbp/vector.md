---
marp: true
theme: default
paginate: true
math: mathjax
style: |
  * {
    box-sizing: border-box;
  }
  /* Slide container */
  section {
    background-color: #fff;
    font-family: 'Times New Roman', Times, serif;
    font-size: 28pt;
    color: black;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    padding: 0;
    padding-bottom: 10pt;
  }

  /* Heading banner */
  section h1 {
    background-color: rgb(25, 107, 36);
    color: white;
    font-family: 'Times New Roman', Times, serif;
    font-size: 30pt;
    margin: 0;
    padding: 8pt;
    text-align: center;
    width: 100%;
  }

  /* Body content fills remaining space */
  section p,
  section ul,
  section ol,
  section pre {
    font-family: 'Times New Roman', Times, serif;
    font-size: 28pt;
    color: black;
    margin: 0;
  }

  section ul {
    text-align: left;
    list-style-type: disc;
    list-style-position: inside;
    padding: 0;
  }

  section ol {
    text-align: left;
    list-style-type: decimal;
    list-style-position: inside;
    padding: 0;
  }

  section ol li::marker {
    font-weight: bold;
  }

  section ul li::marker {
    margin-right: 10pt;
    content: "•  ";
  }

  section pre {
    font-size: 20pt;
  }

  section::after {
    bottom: 5px;
  }

  h1 {
    margin-bottom: 10pt;
  }

  h1 ~ * {
    margin: 0 10pt;
  }

  /* Title slide - no green banner */
  section.title-slide {
    justify-content: center;
    align-items: center;
    padding: 40pt 100pt;
  }

  section.title-slide h1 {
    background-color: transparent;
    color: black;
    font-size: 60pt;
    font-weight: bold;
    text-align: center;
    padding: 0;
    margin-bottom: 30pt;
  }

  section.title-slide p {
    text-align: right;
    font-size: 28pt;
    width: 100%;
    margin: 0;
    line-height: 1.6;
  }

  section p:has(img) {
    display: flex;
    justify-content: center;
    align-items: center;
    flex: 1 1 0;
    min-height: 0;
    margin: 0;
  }

  img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
  }

  marp-pre {
    margin: 10pt;
  }

  blockquote {
    margin-bottom: 20pt;
  }

  section h3 {
    margin-top: 15pt;
    margin-bottom: 15pt;
  }

  section h4 {
    margin-top: 10pt;
    margin-bottom: 10pt;
  }

  table {
    margin: 0;
    padding: 0 10pt;
  }

  th, td {
    border: 1px solid black !important;
  }

  tr {
    background: white !important;
  }

  th img, td img {
    max-height: 390pt;
  }

  hr {
    margin: 30pt 0 20pt 0;
  }
---

<!-- _class: title-slide -->

# Vector Database

By Bidur Sapkota

---

# Introducing Vector Databases

A vector database is a specialized database designed to store, index, and query high-dimensional vectors (embeddings). Unlike traditional databases that search by exact matches or keyword lookups, vector databases find results based on semantic similarity. They answer the question "what is most similar to this?" rather than "what exactly matches this?".

Traditional databases store structured data in rows and columns and retrieve records using exact-match queries like SQL `WHERE` clauses. Vector databases store numerical representations of data (vectors) and retrieve records using mathematical distance calculations. This makes them essential for AI applications where meaning matters more than exact keywords.

---

# Introducing Vector Databases

Common use cases for vector databases are:

- **Semantic Search**: Finding documents by meaning rather than keyword matching. A search for "happy dog" can return results about "joyful puppy" because their vector representations are similar.
- **Recommendation Systems**: Suggesting products, songs, or articles similar to ones a user already likes by comparing their vector representations.
- **Retrieval-Augmented Generation (RAG)**: Feeding relevant context to large language models (LLMs) by retrieving semantically similar documents from a vector store before generating a response.

---

# Introducing Vector Databases

- **Image & Audio Search**: Finding visually or acoustically similar media by comparing their embedding vectors.
- **Anomaly Detection**: Identifying data points that are far from any cluster in vector space, signaling unusual behavior.

---

# Understanding Embeddings

An embedding is a numerical representation of data (text, images, audio) as a list of floating-point numbers called a vector. Embedding models convert unstructured data into dense vectors that capture semantic meaning. Similar concepts end up close together in vector space, while dissimilar concepts are far apart.

For example, the sentence "The cat sat on the mat" might be represented as a vector like `[0.12, -0.45, 0.78, ..., 0.33]` with hundreds or thousands of dimensions. The sentence "A kitten rested on the rug" would produce a vector that is numerically close to the first one because the meanings are similar.

---

# Generating Embeddings with Open-Source Models

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
    "The stock market crashed today"
]

embeddings = model.encode(sentences)
print(embeddings[0][:5])                    # First 5 dimensions
print(embeddings.shape)                     # (2, 384)
```

---

# Generating Embeddings with Open-Source Models

`SentenceTransformer` loads a pre-trained model that runs entirely on your machine. `all-MiniLM-L6-v2` produces 384-dimensional vectors and is fast enough for most applications. `model.encode()` accepts a single string or a list of strings and returns a NumPy array of embeddings.

---

# How Vector Search Works

Vector search (also called nearest neighbor search) finds the vectors in a database that are closest to a given query vector. The process has three main steps: embed the query, compute distances, and return the top results.

### Step-by-Step Process

1. **Embed the query**: Convert the user's query (text, image, etc.) into a vector using the same embedding model that was used to embed the stored data.
2. **Compare against stored vectors**: Calculate the distance or similarity between the query vector and every stored vector.
3. **Return top-k results**: Sort by distance and return the k nearest vectors along with their associated metadata and documents.

---

# How Vector Search Works

### Brute-Force Search

`np.linalg.norm(..., axis=1)` calculates the Euclidean distance between the query and each stored vector. `np.argmin` returns the index of the smallest distance. Brute-force search compares the query against every vector in the database. This is accurate but slow for large datasets because the time grows linearly with the number of vectors.

---

# How Vector Search Works

### Approximate Nearest Neighbor (ANN) Search

Brute-force becomes impractical when you have millions of vectors. Approximate Nearest Neighbor (ANN) algorithms trade a small amount of accuracy for a large gain in speed. Instead of comparing against every vector, ANN algorithms use data structures like graphs, trees, or hashed indices to narrow the search space. The result may not always be the absolute nearest neighbor, but it is close enough and orders of magnitude faster.

---

# Similarity Metrics

A similarity metric defines how "closeness" between two vectors is measured. The choice of metric affects search results and should match the embedding model's training objective.

---

# Similarity Metrics

## Euclidean Distance (L2)

Measures the straight-line distance between two points in vector space. Smaller values mean more similar.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

distance = np.linalg.norm(a - b)
print(distance)                              # 5.196
```

`np.linalg.norm(a - b)` computes the square root of the sum of squared differences: √((4-1)² + (5-2)² + (6-3)²) = √27 ≈ 5.196. Euclidean distance works well when the magnitude of vectors matters.

---

# Similarity Metrics

### Cosine Similarity

Measures the angle between two vectors, ignoring their magnitude. Values range from -1 (opposite) to 1 (identical direction). Higher values mean more similar.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

cosine_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(cosine_sim)                            # 0.9746
```

---

# Similarity Metrics

`np.dot(a, b)` computes the dot product. Dividing by the product of the norms normalizes the result. Cosine similarity is the most common metric for text embeddings because it focuses on the direction (meaning) rather than the length (magnitude) of vectors.

---

# Getting Started with ChromaDB

ChromaDB is an open-source, embedded vector database that runs directly in your Python process. It handles embedding generation, storage, indexing, and querying with minimal configuration.

### Installation

```bash
pip install chromadb
```

---

# Getting Started with ChromaDB

### Creating a Client

```python
import chromadb

# Persistent client (data saved to disk, sqlite)
client = chromadb.PersistentClient(path="./chroma_data")
```

`chromadb.Client()` creates an ephemeral in-memory database, useful for testing. `PersistentClient` saves data to the specified directory so it survives process restarts. The `path` parameter specifies where ChromaDB stores its data files.

---

# Getting Started with ChromaDB

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

print(collections)
```

---

# Getting Started with ChromaDB

`get_or_create_collection` returns an existing collection or creates a new one if it does not exist. `metadata={"hnsw:space": "cosine"}` configures the collection to use cosine similarity for distance calculations. Other options are `l2` (Euclidean, the default) and `ip` (inner product).

---

# CRUD Operations in ChromaDB

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

---

# CRUD Operations in ChromaDB

`ids` must be unique strings for each document. `documents` are the raw text strings. ChromaDB automatically generates embeddings from the documents using its default embedding model (`all-MiniLM-L6-v2`). `metadatas` are optional key-value pairs attached to each document for filtering.

---

# CRUD Operations in ChromaDB

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

---

# CRUD Operations in ChromaDB

### Updating Documents

```python
collection.update(
    ids=["doc1"],
    documents=["Python is a versatile programming language"],
    metadatas=[{"source": "wiki", "category": "python", "updated": True}]
)
```

`update` replaces the document, metadata, and embedding for the specified IDs. ChromaDB re-generates the embedding from the new document text.

---

# CRUD Operations in ChromaDB

### Deleting Documents

```python
# Delete by IDs
collection.delete(ids=["doc1", "doc2"])

# Delete by filter
collection.delete(where={"category": "devops"})
```

`delete` removes documents by their IDs or by a metadata filter. Deleting by filter removes all documents that match the condition.
