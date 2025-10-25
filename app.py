import streamlit as st
from transformers import pipeline, Conversation

# Force PyTorch framework to avoid TensorFlow errors
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium", framework="pt")

st.set_page_config(page_title="Career Chatbot", page_icon="🤖")
st.title("🎓 Career Chatbot")
st.markdown("Ask me anything about your career path, interests, or future goals!")

# Initialize conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = None
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

    # Create or continue conversation
    if st.session_state.conversation is None:
        st.session_state.conversation = Conversation(user_input)
    else:
        st.session_state.conversation.add_user_input(user_input)

    # Generate response
    response = chatbot(st.session_state.conversation)
    reply = response.generated_responses[-1]

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
