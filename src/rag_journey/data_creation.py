from pathlib import Path

Path("data/notes.txt").write_text(
    "My Learning Notes\n"
    "----------------\n"
    "1. Python is a programming language.\n"
    "2. FastAPI is used to build APIs.\n"
    "3. RAG stands for Retrieval-Augmented Generation.\n"
    "4. ChromaDB stores vector embeddings.\n"
    "5. LLMs generate responses using the provided context.\n",
    encoding="utf-8"
)

print("Data written successfully!")