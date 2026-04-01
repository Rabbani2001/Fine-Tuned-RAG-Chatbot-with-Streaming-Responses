from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader  


#api="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"


def document_loader(path):
    document = PyPDFLoader(path)
    doc = document.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap=20)
    texts = text_splitter.split_documents(doc)
    return texts


print("_____1_____")

'''                      1                      '''