from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama

app = FastAPI(
    title="Langchain Server", version="1.0", description="A simple API Server"
)

# Define prompts
prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 50 words"
)
prompt2 = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} for a 5 years child with 50 words"
)

# Use Ollama (LLaMA 3)
llm = Ollama(model="llama3")

# Create chains
essay_chain = prompt1 | llm
poem_chain = prompt2 | llm

# Add LangServe routes
add_routes(app, essay_chain, path="/essay")
add_routes(app, poem_chain, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
