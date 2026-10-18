from langchain_community.document_loaders import (
    TextLoader
)

data=TextLoader("data/notes.txt",encoding="utf-8").load()

print(data[0].page_content)
print(data[0].metadata)
print(len(data))