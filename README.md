# Customer Support Chatbot

A Streamlit-based chatbot application that answers questions about Portage Bill and Master's Cash System using OpenAI and LlamaIndex for document processing and retrieval.This chatbot can help ask any questions that are asked with regards to any customer support manual or any other document

## Prerequisites

- Python (version not specified in code)
- Streamlit
- LlamaIndex
- OpenAI
- NLTK

## Installation

Install the required packages using pip:

```bash
pip install streamlit llama_index openai nltk
```

## Configuration

1. OpenAI API Key:
   - Store your OpenAI API key in Streamlit secrets
   - The application accesses it using: `st.secrets.openai_key`

2. Data Directory:
   - Place your documents in the following directory:
   ```
   C:/Users/Aniket/Documents/MyPythonProjects/Chatbot_UsingPrivateData/data
   ```

3. Page Configuration:
   - Title: "Aniket Solutions Chatbot"
   - Logo Path: "C:/Users/Aniket/Documents/Aniket Solutions/AS-logos/AS-logos_transparent.png"
   - Layout: Centered
   - Initial Sidebar State: Auto

## Features

1. Document Processing:
   - Loads and indexes documents from the specified directory
   - Uses LlamaIndex's SimpleDirectoryReader for document loading
   - Implements caching for improved performance

2. Chat Interface:
   - Interactive chat input
   - Message history tracking
   - Real-time response generation
   - Loading spinners for better user experience

3. AI Configuration:
   - Uses GPT-3.5-turbo model
   - Temperature: 0.5
   - Custom system prompt for technical responses
   - Specialized in Portage Bill and Master's Cash System information

## Code Structure

```python
# Main components:
1. Page Configuration
2. OpenAI API Setup
3. Chat History Initialization
4. Data Loading and Indexing
5. Chat Engine Initialization
6. User Input Processing
7. Message Display
8. Response Generation
```

## Usage

The chatbot:
1. Loads with an initial welcome message
2. Accepts user questions through the chat input
3. Processes questions against the indexed documents
4. Provides technical answers based on the document content
5. Maintains conversation history within the session

## LlamaIndex Configuration

```python
settings = Settings(
    llm=OpenAI(
        model="gpt-3.5-turbo",
        temperature=0.5,
        system_prompt="You are an expert on the User Guide and your job is to answer technical questions. Assume that all questions are related to the User Guide. Keep your answers technical and based on facts – do not hallucinate features."
    )
)
```

## Chat Engine Features

- Mode: "condense_question"
- Verbose output enabled
- Response caching implemented
- Real-time query processing
