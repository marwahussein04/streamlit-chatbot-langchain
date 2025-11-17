)
🤖 Streamlit Q&A Chatbot with LangChain
This project is an interactive Q&A chatbot web application built using the Streamlit library for the user interface. The application integrates the capabilities of the GPT Large Language Model (LLM) from OpenAI via the LangChain framework. This setup allows users to conduct dynamic conversations and receive accurate, professional responses.

📝 Detailed Description and Key Features
Project Title: Intelligent Q&A Chat Application using Streamlit and LangChain
Overview:
This is a complete, full-stack chat web application designed to serve as a "professional assistant" for handling user inquiries. The project strategically combines the latest AI application development tools:

Frontend Interface: Fully developed using Streamlit to provide a clean, dark, and user-friendly interface that supports displaying an interactive chat history.

Backend Logic: Utilizes the LangChain framework to orchestrate the communication process with the Large Language Models (LLMs), simplifying the management of the prompt template and model invocation.

AI Model: Relies on OpenAI's GPT models to ensure high-quality, fast, and reliable responses.

Key Features:
Secure API Key Input: The OpenAI API key is entered securely via a Sidebar using a type="password" input field.

Model Selection: Allows the user to select the desired OpenAI model (e.g., gpt-4o, gpt-3.5-turbo) for flexibility in usage and cost management.

LangChain Processing Chain: A processing "Chain" is created using ChatPromptTemplate, ChatOpenAI, and StrOutputParser, and it's cached using @st.cache_resource for enhanced performance and faster response times.

Modern Design: Custom CSS styling is applied to create a dark theme similar to GitHub's aesthetic, which elevates the user experience.

Robust Error Handling: Includes clear handling for critical errors such as insufficient quota or an invalid API key.

How to Run Locally (For the Reader):
Clone: git clone https://github.com/marwahussein04/streamlit-chatbot-langchain.git

Install: pip install -r requirements.txt

Run: streamlit run app.py

Use: Enter your OpenAI API key in the sidebar to begin chatting.
