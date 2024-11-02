# Customer Support Manual Chatbot 🤖📚

An intelligent chatbot application that transforms any customer support manual or documentation into an interactive chat assistant. Built with Streamlit, LlamaIndex, and OpenAI's GPT-3.5-turbo, this tool helps organizations provide 24/7 customer support by automatically answering questions based on their support documentation.

## Purpose

This application solves a common customer support challenge: making product manuals and documentation more accessible and interactive. Instead of reading through lengthy PDF manuals, customers can simply ask questions and get immediate, accurate responses based on the official documentation.

Key Benefits:
- 24/7 availability for customer support
- Consistent answers based on official documentation
- Reduced load on human support staff
- Easy to update by simply replacing the source PDF
- Cost-effective scaling of support operations

## Features

- PDF Manual Integration: Automatically processes and indexes any customer support PDF manual
- Interactive Chat Interface: User-friendly chat interface for asking questions
- Context-Aware Responses: Maintains conversation context for natural interactions
- Accurate Information: Responses are strictly based on the provided manual content
- Easy Setup: Simple configuration for any organization's documentation

## Prerequisites

Before running this application, you need:

- Python 3.7+
- OpenAI API key
- Your customer support manual in PDF format
- The required Python packages:
  ```bash
  pip install streamlit llama_index openai nltk
  ```

## Installation

1. Clone this repository:
   ```bash
   git clone [your-repository-url]
   cd [repository-name]
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a `.streamlit/secrets.toml` file
   - Add your OpenAI API key:
     ```toml
     openai_key = "your-api-key-here"
     ```

4. Add your support manual:
   - Create a 'data' directory in your project folder
   - Place your PDF manual(s) in the data directory
   - Update the path in the code if necessary:
     ```python
     reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
     ```

## Usage

1. Start the application:
   ```bash
   streamlit run app.py
   ```

2. Access the chatbot:
   - Open your web browser
   - Navigate to the provided URL (typically `http://localhost:8501`)
   - Start asking questions about your product or service

Example Questions:
- "How do I reset my password?"
- "What are the system requirements?"
- "Can you explain the installation process?"

## How It Works

1. **Document Processing**:
   - The system loads your PDF manual(s)
   - LlamaIndex processes and indexes the content for efficient searching
   - Creates a searchable knowledge base from your documentation

2. **Query Handling**:
   - User asks a question through the chat interface
   - The system searches the indexed documentation
   - GPT-3.5-turbo generates a natural, accurate response based on the manual content

3. **Response Generation**:
   - Maintains conversation context
   - Provides specific, documented answers
   - Citations to relevant manual sections (if configured)

## Customization

You can customize the chatbot by:
- Adjusting the OpenAI model parameters (temperature, system prompt)
- Modifying the chat interface appearance
- Adding custom preprocessing for your specific documentation format
- Implementing response templates for common queries

## Best Practices

1. **Documentation Preparation**:
   - Ensure PDFs are text-searchable
   - Use clear, consistent formatting
   - Update documentation regularly

2. **User Experience**:
   - Add example questions for users
   - Include a feedback mechanism
   - Monitor common queries for documentation improvements

## Troubleshooting

Common issues and solutions:
- **PDF Not Loading**: Ensure PDF is text-searchable and not scanned
- **Memory Issues**: Reduce chunk size in the document processing
- **Slow Responses**: Check internet connection and API rate limits

## Contact
Aniket Shirsat

Email: ashirsat96@gmail.com


---
