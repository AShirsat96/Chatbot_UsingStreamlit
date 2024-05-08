!pip install streamlit llama_index openai nltk
# Importing the necessary libraries
import streamlit as st
import openai
from llama_index.llms.openai import OpenAI
try:
    from llama_index import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
except ImportError:
    from llama_index.core import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader

st.set_page_config(
    page_title="Chat with the User Guide, powered by LlamaIndex",
    page_icon="🦙",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

openai.api_key = st.secrets.openai_key
st.title("Chat with the User Guide, powered by LlamaIndex 💬🦙")

# Initialize the chat messages history
messages = st.session_state.get("messages", [
    {"role": "assistant", "content": "Ask me a question about PBMCAS!"}
])

# Load and index data
@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the User Guide – hang tight! This should take 1-2 minutes."):
        reader = SimpleDirectoryReader(input_dir=r"C:/Users/Aniket/Documents/MyPythonProjects/Chatbot_UsingPrivateData/data", recursive=True)
        docs = reader.load_data()
        # llm = OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert o$
        # index = VectorStoreIndex.from_documents(docs)
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert on the User Guide and your job is to answer technical questions. Assume that all questions are related to the User Guide. Keep your answers technical and based on facts – do not hallucinate features."))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()

 # Initialize the chat engine
if "chat_engine" not in st.session_state.keys():
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

# Prompt for user input and display message history
if prompt := st.chat_input("Your question"): 
    messages.append({"role": "user", "content": prompt})

# Display the prior chat messages
for message in messages: 
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Pass query to chat engine and display response
if messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            messages.append(message) # Add response to message history
