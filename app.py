import streamlit as st
from transformers import pipeline

# Load the text generation model
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

# Career guidance logic
career_paths = {
    "coding": "You might enjoy Software Development or Data Science.",
    "design": "Consider UI/UX Design or Product Design.",
    "robotics": "Explore Robotics Engineering or Mechatronics.",
    "ai": "Machine Learning, Deep Learning, or AI Research could be great for you.",
    "management": "You might be interested in Product Management or Business Analysis.",
}

# Streamlit UI
st.set_page_config(page_title="Career Chatbot", page_icon="🎓")
st.title("🎓 Career Guidance Chatbot")
st.write("Ask me about your career options based on your interests!")

user_input = st.text_input("Your question:")

if user_input:
    response = chatbot(user_input, max_length=100, do_sample=True, top_k=50)
    st.write("🤖", response[0]['generated_text'])

    # Keyword-based suggestion
    for keyword in career_paths:
        if keyword in user_input.lower():
            st.write("💡 Suggestion:", career_paths[keyword])
