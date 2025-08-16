import streamlit as st
import requests

st.set_page_config(page_title="LangChain Client", layout="centered")

st.title("📚 LangChain Client with Ollama API")

# Sidebar for API settings
st.sidebar.header("⚙️ API Settings")
api_url = st.sidebar.text_input("API URL", "http://localhost:8000")

# User input
st.subheader("Enter a Topic")
topic = st.text_input("Topic", "Artificial Intelligence")

# Dropdown to choose API endpoint
endpoint = st.radio(
    "Choose what you want to generate:",
    ("Essay (50 words)", "Poem for kids (50 words)")
)

# Map endpoint names to paths
endpoint_map = {
    "Essay (50 words)": "/essay/invoke",
    "Poem for kids (50 words)": "/poem/invoke"
}

if st.button("Generate Response"):
    if not topic.strip():
        st.warning("⚠️ Please enter a topic!")
    else:
        try:
            url = api_url + endpoint_map[endpoint]
            payload = {"input": {"topic": topic}}
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                result = response.json()
                st.success("✅ Response:")
                st.write(result["output"])
            else:
                st.error(f"❌ Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"⚠️ Failed to connect to API: {e}")
