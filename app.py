import streamlit as st
from src.pipeline import output_result

if 'message history' not in st.session_state:
    st.session_state['message history']=[]

for message in st.session_state['message history']:
    with st.chat_message(message["role"]):
        st.text(message["content"])

 
st.title("Fine-Tuned RAG Chatbot with Streaming Responses")

Query=st.chat_input('Type here')
#Response=output_result(Query)


if Query:

    Response=output_result(Query) 
    st.session_state['message history'].append({"role":"user","content":Query})
    with st.chat_message('user'):
        st.text(Query)


    st.session_state['message history'].append({"role":"assistant","content":Response})
    with st.chat_message('assistant'):
        st.text(Response)

















