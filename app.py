import streamlit as st
import openai # لا يزال مطلوبًا إذا كنت تستخدمينه بشكل مباشر ولكن LangChain تتولى الأمر غالبًا
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage


# -----------------
# 1. Configuration and Aesthetics
# -----------------

st.set_page_config(
    page_title="Enhanced Q&A Chatbot",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Chatbot powered by OpenAI and LangChain!"
    }
)

# Apply a clean, modern style
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117; /* Dark background similar to GitHub */
        color: #c9d1d9;
    }
    .st-emotion-cache-p5mxx6 { /* Main container padding */
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .st-emotion-cache-1aeo0hr { /* Chat message padding */
        background-color: #161b22;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .st-emotion-cache-10qadp {
        border-radius: 10px;
        padding: 10px;
        background-color: #161b22;
    }
    </style>
    """, unsafe_allow_html=True)


# -----------------
# 2. LangChain Logic
# -----------------

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful and professional assistant. Please respond to the user queries concisely and accurately."),
        # Note: We don't use the simple "Question:{question}" here because Streamlit's chat elements handle history better.
        ("user", "{question}")
    ]
)

@st.cache_resource
def get_chain(api_key, model_name):
    """Initializes and caches the LangChain setup."""
    # Note: api_key is passed to ChatOpenAI constructor
    llm = ChatOpenAI(model=model_name, api_key=api_key, temperature=0.7)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    return chain

# -----------------
# 3. Streamlit Interface
# -----------------

st.title("🤖 Enhanced Q&A Chatbot")
st.markdown("---")

## Sidebar for settings
with st.sidebar:
    st.title("🔑 Configuration")
    
    # Use st.secrets or environment variables for key management in production!
    api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    
    # Select the OpenAI model
    engine = st.selectbox("Select OpenAI Model", ["gpt-4o", "gpt-4-turbo", "gpt-4", "gpt-3.5-turbo"])
    st.markdown("---")
    st.markdown("*(Note: Temperature/Max Tokens are managed internally by the LLM component for simplicity in this Streamlit flow.)*")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [AIMessage(content="Hello! I'm ready to answer your questions. Please enter your OpenAI API key to begin.")]


# Display chat messages from history
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# Main interface for user input
if user_input := st.chat_input("Ask me anything..."):
    
    if not api_key:
        st.warning("Please enter your OpenAI API Key in the sidebar to start the conversation.")
        st.stop()
    
    # 1. Add user message to history and display it
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # 2. Generate response
    with st.chat_message("assistant"):
        # Display a placeholder while loading
        with st.spinner("Thinking..."):
            try:
                # Retrieve the chain (cached function)
                chain = get_chain(api_key, engine)
                
                # We only pass the latest question, as the prompt template is simple
                # For a true conversational flow, you would pass the entire history
                response = chain.invoke({'question': user_input})
                
                # Display the response
                st.markdown(response)
                
                # 3. Add assistant response to history
                st.session_state.messages.append(AIMessage(content=response))

            except Exception as e:
                error_message = f"An error occurred: {e}"
                if "API_KEY" in str(e).upper():
                     st.error("Error: The provided API Key is invalid or expired. Please check your key in the sidebar.")
                else:
                    st.error(error_message)
