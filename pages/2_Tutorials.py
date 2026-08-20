import streamlit as st
from utils.styles import inject_styles

st.set_page_config(page_title="Tutorials — Music Wave Visualizer", layout="wide")
inject_styles()

st.title("Tutorials")
st.markdown(
    '<p class="muted">Short lessons on the physics behind what you see in the Visualizer.</p>',
    unsafe_allow_html=True,
)

def embed_video(youtube_id: str) -> None:
    st.markdown(
        f"""
        <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;
                    border-radius:8px;border:1px solid #2A2A4A;margin-top:0.75rem;">
            <iframe
                src="https://www.youtube.com/embed/{youtube_id}"
                style="position:absolute;top:0;left:0;width:100%;height:100%;"
                frameborder="0"
                allowfullscreen>
            </iframe>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# ── Section 1 ──────────────────────────────────────────────────────────────
st.subheader("1. What is a Sound Wave?")
st.markdown(
    """
    Sound is a **longitudinal wave** — a disturbance that travels through air by
    alternately compressing and spreading out the molecules around it. Unlike a wave
    on the surface of water, sound waves move in the same direction they travel.
    When that wave reaches your ear, the pressure changes vibrate your eardrum,
    and your brain interprets the signal as sound.
    """
)
embed_video("Placeholder")

st.markdown("<br>", unsafe_allow_html=True)

# ── Section 2 ──────────────────────────────────────────────────────────────
st.subheader("2. Amplitude & Loudness")
st.markdown(
    """
    **Amplitude** is the maximum displacement of the wave from its resting position —
    the height of the peaks and depth of the troughs on a waveform diagram.
    A larger amplitude means more energy is being transferred, which we perceive as
    a **louder sound**. Decibels (dB) are a logarithmic measure of amplitude:
    every 10 dB roughly doubles the perceived loudness.
    """
)
embed_video("Placeholder")

st.markdown("<br>", unsafe_allow_html=True)

# ── Section 3 ──────────────────────────────────────────────────────────────
st.subheader("3. Frequency & Pitch")
st.markdown(
    """
    **Frequency** is how many complete wave cycles occur per second, measured in
    Hertz (Hz). The higher the frequency, the higher the **pitch** we perceive.
    Humans can hear roughly 20 Hz to 20,000 Hz. Middle C on a piano is 262 Hz;
    concert A is 440 Hz. In a frequency spectrum plot, each spike corresponds to a
    frequency that is present in the sound.
    """
)
embed_video("Placeholder")

st.markdown("<br>", unsafe_allow_html=True)

# ── Section 4 ──────────────────────────────────────────────────────────────
st.subheader("4. Harmonics & Timbre")
st.markdown(
    """
    When an instrument plays a note, it doesn't produce just one frequency —
    it produces a **fundamental** frequency plus a series of **harmonics**
    (integer multiples of the fundamental). The specific mix of harmonics is what
    gives each instrument its unique sound character, called **timbre**. That's why
    a violin and a flute playing the same A440 sound completely different.
    In the frequency spectrum, you can literally see these harmonic peaks lined up.
    """
)
embed_video("Placeholder")
