import streamlit as st
from utils.styles import inject_styles

st.set_page_config(
    page_title="Music Wave Visualizer",
    page_icon="🎵",
    layout="wide",
)

inject_styles()

st.markdown(
    """
    <div style="padding: 3rem 0 2rem 0; text-align: center;">
        <h1 style="font-size: 3rem; margin-bottom: 0.5rem;">
            Music Wave Visualizer
        </h1>
        <p style="font-size: 1.15rem; color: #9B8BB4; max-width: 680px; margin: 0 auto 2rem auto;">
            The Music Wave Visualizer converts audio files to wave diagrams,
            explains the physics, and shows how the waves vary depending on the
            instrument (including voice). So if you enjoy either physics or music,
            or even both, this app is a great place for you to explore!
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

col_cta, _ = st.columns([1, 3])
with col_cta:
    if st.button("Try the Visualizer →", type="primary", use_container_width=True):
        st.switch_page("pages/3_Visualizer.py")

st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        """
        <div class="feature-card">
            <h3>📁 Upload</h3>
            <p class="muted">Drop in any WAV, MP3, or OGG file from your instrument or voice.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        """
        <div class="feature-card">
            <h3>📊 Visualize</h3>
            <p class="muted">Instantly see your sound as a waveform, frequency spectrum, and spectrogram.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        """
        <div class="feature-card">
            <h3>🔬 Learn</h3>
            <p class="muted">Each chart comes with a physics explainer connecting the diagram to real science.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
