import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load env
load_dotenv()

# configure gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Page Config 
st.set_page_config(page_title="AI Chatbot",page_icon="🤖",layout="centered")

# Title
st.title("AI Chatbot")
st.write("Chat with Gemini")

# Session State for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# user input
user_input = st.chat_input("Type your message... ")

if user_input:

    # show user input
    st.chat_message("user").markdown(user_input)

    # Save user input
    st.session_state.messages.append({
        "role":"user",
        "content":user_input
    })

    # Generate AI response
    response = model.generate_content(user_input)

    ai_response = response.text

    # show ai response
    st.chat_message("assistant").markdown(ai_response)
    
    # Save AI response
    st.session_state.messages.append({
        "role":"assistant",
        "content":ai_response
    })