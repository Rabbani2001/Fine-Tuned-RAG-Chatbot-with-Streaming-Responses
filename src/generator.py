from langchain_openai import ChatOpenAI
api ="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"

def llm():
    chatmodel= ChatOpenAI(model="gpt-4.1-mini", stream_usage=True,api_key=api)
    return chatmodel

