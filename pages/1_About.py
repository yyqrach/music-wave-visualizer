import streamlit as st
from utils.styles import inject_styles

st.set_page_config(page_title="About — Music Wave Visualizer", layout="wide")
inject_styles()

st.title("About")

st.markdown(
    """
    **Music Wave Visualizer** is an educational web app that bridges two disciplines
    students often keep separate: physics and music. By uploading a short audio clip,
    you can see the mathematical structure hidden inside every sound — and understand
    why a guitar and a flute playing the same note look completely different as waves.
    """
)

st.markdown("---")

st.subheader("Who is this for?")
st.markdown(
    """
    This app is built for **high school and middle school students** who are curious
    about either physics, music, or both. No prior knowledge is required — every chart
    comes with a plain-English explanation of the physics concept it illustrates.
    """
)

st.markdown("---")

st.subheader("Physics Concepts Covered")

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
        **Amplitude**
        The height of a wave, which corresponds to how loud a sound is. A bigger
        amplitude means more energy — and a louder sound.

        **Frequency**
        How many times a wave oscillates per second (measured in Hertz). Higher
        frequency = higher pitch. A concert A is 440 Hz.
        """
    )
with col2:
    st.markdown(
        """
        **Harmonics & Timbre**
        Real instruments don't produce a single frequency — they produce a
        fundamental plus a series of overtones called harmonics. The mix of
        harmonics is what gives each instrument its unique "colour" (timbre).

        **Spectrograms**
        A time-frequency heatmap that shows how the frequencies in a sound
        change over time. Great for comparing instruments or seeing a melody
        play out note by note.
        """
    )
