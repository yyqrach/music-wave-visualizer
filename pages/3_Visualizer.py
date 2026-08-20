import io
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import librosa
from utils.styles import inject_styles
from utils.charts import plot_waveform, plot_fft, plot_spectrogram

st.set_page_config(page_title="Visualizer — Music Wave Visualizer", layout="wide")
inject_styles()

st.title("Visualizer")
st.markdown(
    '<p class="muted">Upload an audio file to see its wave physics — waveform, frequency spectrum, and spectrogram.</p>',
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader(
    "Upload an audio file (WAV, MP3, or OGG)",
    type=["wav", "mp3", "ogg"],
)

if uploaded_file is not None:
    audio_bytes = uploaded_file.read()
    st.audio(audio_bytes, format=f"audio/{uploaded_file.name.split('.')[-1]}")

    with st.spinner("Analysing audio..."):
        y, sr = librosa.load(
            io.BytesIO(audio_bytes), sr=None, mono=True, duration=30
        )

    # ── Waveform ───────────────────────────────────────────────────────────
    st.subheader("Waveform")
    fig = plot_waveform(y, sr)
    st.pyplot(fig)
    plt.close(fig)
    with st.expander("Physics: Amplitude & Time"):
        st.markdown(
            """
            The waveform shows how the **amplitude** (air pressure) of your sound
            changes over time. Tall peaks mean louder moments; flat sections mean
            silence or near-silence. The denser the oscillations, the higher the
            frequency (and pitch) of that part of the sound. Compare a sustained
            guitar note (regular repeating wave) to a snare hit (sharp spike then
            silence).
            """
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Frequency Spectrum ─────────────────────────────────────────────────
    st.subheader("Frequency Spectrum (FFT)")
    fig = plot_fft(y, sr)
    st.pyplot(fig)
    plt.close(fig)
    with st.expander("Physics: Frequency & Harmonics"):
        st.markdown(
            """
            The **Fast Fourier Transform (FFT)** decomposes the sound into its
            individual frequency components. Each bar shows how much of that
            frequency is present. A pure sine wave would show a single spike.
            A real instrument shows a **fundamental frequency** (the tallest spike)
            plus a series of **harmonics** at integer multiples — those are the
            overtones that give the instrument its characteristic sound.
            """
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Spectrogram ────────────────────────────────────────────────────────
    st.subheader("Spectrogram")
    fig = plot_spectrogram(y, sr)
    st.pyplot(fig)
    plt.close(fig)
    with st.expander("Physics: Reading a Spectrogram"):
        st.markdown(
            """
            A **spectrogram** is a time-frequency heatmap. The x-axis is time,
            the y-axis is frequency, and the colour shows how loud each frequency
            is at each moment (brighter/orange = louder, darker/purple = quieter).
            It's like stacking many FFT snapshots side by side. You can see melodies
            moving up and down, harmonics as horizontal bands, and the difference
            between sustained tones and percussive sounds at a glance.
            """
        )
else:
    st.info("Upload a WAV, MP3, or OGG file above to get started.")
