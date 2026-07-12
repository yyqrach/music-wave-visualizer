import io
import numpy as np
import streamlit as st
import librosa
import matplotlib.pyplot as plt

st.set_page_config(page_title="Music Wave Visualizer", layout="wide")

st.title("Music Wave Visualizer")
st.write("Upload or select a short musical sound to see the wave physics behind it.")

uploaded_file = st.file_uploader("Upload a short WAV file", type=["wav"])

if uploaded_file is not None:
    audio_bytes = uploaded_file.read()
    st.audio(audio_bytes, format="audio/wav")

    audio_buffer = io.BytesIO(audio_bytes)
    y, sr = librosa.load(audio_buffer, sr=None, mono=True, duration=10)

    time = np.arange(len(y)) / sr

    st.subheader("Waveform: Amplitude vs. Time")
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.plot(time, y)
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Amplitude")
    ax.set_title("Waveform")
    st.pyplot(fig)

    st.info("Physics connection: larger amplitude generally corresponds to a louder sound. Faster oscillations correspond to higher frequencies and higher perceived pitch.")
else:
    st.warning("Upload a short WAV clip to begin.")
