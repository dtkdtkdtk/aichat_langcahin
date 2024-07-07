import streamlit as st
import openai

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    st.write("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")
