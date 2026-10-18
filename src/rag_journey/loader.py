from langchain_community.document_loaders import (
    TextLoader ,PyPDFLoader
)

# Text Loader
# data=TextLoader("data/notes.txt",encoding="utf-8").load()

# print(data[0].page_content)
# print(data[0].metadata)
# print(len(data))

# PDF-Loader

data=PyPDFLoader("data/AI.pdf").load()
# for i,page in enumerate(data):
#     print(f"Page {i+1}")
#     print(page.page_content)
#     print("--"*50)

print(data[0].metadata)