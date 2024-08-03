import streamlit as st
import os
import google.generativeai as genai

st.title("my_bot")

os.environ['GOOGLE_API_KEY'] = "AIzaSyAzpDv1-GfqI-yckMPPe4Vef1qElaAizDg"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')

if "message" not in st.session_state:
    st.session_state.message = [
        {
            "role": "assistant",
            "content": "Ask me anything"
        }
    ]

    for message in st.session_state.message:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def llm_function(query):
    response=model.generative_content(query)

    with st.chat_message("assistant"):
        st.markdown(response.text)

    st.session_state.messages.append(
        {
            "role": "user",
             "content": query
        }
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.text
        }
    )

    query = st.chat_input("what's up ")

    if query:
        with st.chat_message("user"):
            st.markdown(query)

        llm_function(query)
