from langchain_openai import OpenAIEmbeddings 
from langchain_community.vectorstores import Chroma
from vector_database.Chromadb import Vector_store

api="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"

embeddings=OpenAIEmbeddings(model="text-embedding-3-large",api_key=api)


def similar_docs(Query):
    vector = Vector_store(path="/Users/rabbanisaifi/Desktop/Amlgo project/data/AI_Training_Document.pdf")
    text= vector.similarity_search(Query)
    context = "\n\n".join([doc.page_content for doc in text])
    return context 



print("_____3_____")
