import streamlit as st
from backend.llm_response import generate_response
from streamlit_lottie import st_lottie
import requests

# ----------------------
# Page config and theme
# ----------------------
st.set_page_config(
    page_title="🌌 Back2U: Chat with Your Future Self",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ----------------------
# Starry background via CSS
# ----------------------
st.markdown(
    """
    <style>
    .stApp {
        background: url('https://static.vecteezy.com/system/resources/previews/000/834/435/non_2x/beautiful-space-background-vector.jpg') no-repeat center center;
        background-size: cover;
        color: white;
    }
    .stButton>button {
        background-color: #7FDBFF;
        color: black;
        font-weight: bold;
    }
    textarea {
        background-color: #1c1e2a;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------
# Lottie animation helper
# ----------------------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_stars = load_lottie("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")
if lottie_stars:
    st_lottie(lottie_stars, height=200)

# ----------------------
# App header
# ----------------------
st.title("🌌 Back2U — Chat with Your Future Self")
st.subheader("🚀 Talk to your future self and get guidance on your goals, career, and growth")

# ----------------------
# User input
# ----------------------
user_query = st.text_area("💬 What would you like to ask your future self?", height=150)

# ----------------------
# Generate response
# ----------------------
if st.button("✨ Ask"):
    if user_query.strip():
        with st.spinner("Thinking..."):
            response = generate_response(user_query)
        st.markdown(f"**Future You says:**\n\n{response}")
    else:
        st.warning("Please type something first!")