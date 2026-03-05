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


### 6. Configure CCR (Claude Code Router) with Erez's guide

---


---

### 7. Install Elastic MCP server

## Installed globally via:

```bash
npm install -g @elastic/mcp-server-elasticsearch zod
```

## Config Location

```
%USERPROFILE%\.claude.json
```

## The Final Working Config

```json
{
  "mcpServers": {
    "elasticsearch": {
      "command": "mcp-server-elasticsearch",
      "args": [],
      "env": {
        "ES_URL": "http://127.0.0.1:9200",
        "ES_SSL_SKIP_VERIFY": "true"
      }
    }
  }
}
```
---


---

### 8. Verification

Run:

```bash
claude mcp list
```

You should see a green checkmark (✓) next to the Elasticsearch server.
---


---

### 9. Start using it

To ensure Claude does not get confused by local files, use explicit prompts such as:

```
Search the readme-index using the elasticsearch__search tool...
```

This ensures Claude uses the MCP Elasticsearch tool instead of attempting to read local files.

---