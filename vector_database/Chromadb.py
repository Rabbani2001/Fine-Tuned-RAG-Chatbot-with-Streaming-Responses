from langchain_openai import OpenAIEmbeddings
from chunks.embedded_text import document_loader 
from langchain_community.vectorstores import Chroma


api="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"

embeddings=OpenAIEmbeddings(model="text-embedding-3-large",api_key=api)


def Vector_store(path):
    docs= document_loader(path=path)
    vector_store=Chroma.from_documents(
                documents=docs,
                 embedding=embeddings
            )
    return vector_store

print("_____2_____")


#"/Users/rabbanisaifi/Desktop/Amlgo project/data/AI_Training_Document.pdf"