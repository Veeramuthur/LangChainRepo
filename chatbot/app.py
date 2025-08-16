# Import required LangChain libraries
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# LangSmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "Question: {question}"),
    ]
)

## Streamlit UI
st.title("LangChain Chatbot Demo with Ollama (Local LLM)")
user_input = st.text_input("Enter your question here:")

## LLM (Ollama)
# Make sure Ollama is installed and running locally
# Example: ollama pull llama2
llm = ChatOllama(
    model="llama2",  # change to any local model you have pulled
    temperature=0
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if st.button("Send") and user_input:
    response = chain.invoke({"question": user_input})
    st.text_area("Bot:", value=response, height=300)