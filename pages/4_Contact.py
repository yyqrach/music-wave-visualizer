import streamlit as st
from utils.styles import inject_styles

st.set_page_config(page_title="Contact — Music Wave Visualizer", layout="wide")
inject_styles()

st.title("Contact")
st.markdown(
    """
    Have a question, suggestion, or just want to say hello? Reach out below.
    """
)

st.markdown("---")

st.subheader("Get in Touch")
st.markdown(
    """
    **Name:** Shun Akiyama

    **Email:** [akanie6222@gmail.com](mailto:akanie6222@gmail.com)

    **GitHub:** [github.com/shunakiya](https://github.com/shunakiya)
    """,
    unsafe_allow_html=False,
)
