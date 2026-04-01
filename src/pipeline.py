from src.generator import llm
from src.retriever import similar_docs


#a=input("How may i help you: ")

def output_result(Query):
   model =llm()
   
   context = similar_docs(Query)

   prompt = f"""
   You are a helpfull assistant, use the context given below and answer the user's query 
   and also provide the procedure if the user wants
   Context:                                                   
   {context}
   Question: {Query}
   """
   result = model.invoke(prompt)

   return result.content
