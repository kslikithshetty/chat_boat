import streamlit as st
from transformers import pipeline

# Force PyTorch framework to avoid TensorFlow errors
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium", framework="pt")

st.set_page_config(page_title="Career Chatbot", page_icon="🤖")
st.title("🎓 Career Chatbot")
st.markdown("Ask me anything about your career path, interests, or future goals!")

# Session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message here...")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate response
    response = chatbot(user_input, max_length=1000, pad_token_id=50256)[0]["generated_text"]
    reply = response[len(user_input):].strip()

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
