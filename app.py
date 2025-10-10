import streamlit as st

st.title("Back2U - Chat with Your Future Self 🚀")

user_input = st.text_input("Type your message to future you:")

if st.button("Send"):
    st.write(f"Your message: {user_input}")
    st.write("Future you says: …(LLM response will go here)")