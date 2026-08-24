import streamlit as st
from utils.styles import inject_styles

st.set_page_config(page_title="Contact — Music Wave Visualizer", layout="wide")
inject_styles()

st.title("Contact")
st.markdown(
    """
    Any questions, suggestions, or just want to say hi? Feel free to reach out below!
    """
)

st.markdown("---")

st.subheader("Get in Touch")
st.markdown(
    """
    **Name:** Rachel Yiqiao Yang

    **Email:** musicwavesvisualizer@gmail.com

    **GitHub:** @yyqrach
    """,
    unsafe_allow_html=False,
)
