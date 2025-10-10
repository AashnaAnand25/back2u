# app.py
import streamlit as st
from backend.llm_response import generate_response

st.set_page_config(page_title="Back2U: Chat with Your Future Self")

st.title("🤖 Back2U — Chat with Your Future Self")

st.write("Talk to your future self and get guidance on your goals, career, and growth 🚀")

user_query = st.text_area("What would you like to ask your future self?", height=150)

if st.button("Ask"):
    if user_query.strip():
        with st.spinner("Thinking..."):
            response = generate_response(user_query)
        st.markdown(f"**Future You says:**\n\n{response}")
    else:
        st.warning("Please type something first!")
