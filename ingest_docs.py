from elasticsearch import Elasticsearch
import os

# 1. Connect with Compatibility Mode
# meta_header=False prevents the 'Accept version must be 8 or 7' error
es = Elasticsearch(
    "http://localhost:9200",
    meta_header=False 
)

files = ["README1.md", "README2.md", "README3.md"]

def ingest_readme(filename):
    if not os.path.exists(filename):
        print(f"Skipping {filename}: File not found.")
        return

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    document = {
        "filename": filename,
        "content": content 
    }

    try:
        # This will now trigger the 'semantic_text' logic automatically
        response = es.index(index="readme-index", document=document)
        print(f"Successfully indexed {filename}. Result: {response['result']}")
    except Exception as e:
        print(f"Error indexing {filename}: {e}")

for file in files:
    ingest_readme(file)

es.indices.refresh(index="readme-index")
print("\nIngestion complete! You are ready to search.")