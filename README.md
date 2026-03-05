# Elastic MCP Server

This project tests and sets up the Elastic MCP server.

---

## Setup

### 1. Start the Environment

Run:

```bash
docker-compose up -d
```

---

### 2. Setup the "AI Brain" (Inference Model)

Go to http://localhost:5601 to Management > Dev Tools and Create the sparse embedding inference endpoint:

```json
PUT _inference/sparse_embedding/my-embedding-model
{
  "service": "elser",
  "service_settings": {
    "num_allocations": 1,
    "num_threads": 1
  }
}
```
Check if a json response with 200 status code returned:

```json
GET _inference/sparse_embedding/my-embedding-model
```

---

### 3. Create the "Smart" Index

Create the semantic index:

```json
PUT readme-index
{
  "mappings": {
    "properties": {
      "filename": { 
        "type": "keyword" 
      },
      "content": {
        "type": "semantic_text",
        "inference_id": "my-embedding-model"
      }
    }
  }
}
```

---

### 4. Ingest README Files

Run the Python script to ingest the 3 `README<index>.md` files into the index.

```python .\ingest_docs.py ```

---

### 5. Verify It Works

Run a semantic search with highlighting (this example should return README3.md as the most close):

```json
GET readme-index/_search
{
  "query": {
    "semantic": {
      "field": "content",
      "query": "How do I set up the cloud infrastructure?"
    }
  },
  "highlight": {
    "fields": {
      "content": {}
    }
  }
}
```

---


---
