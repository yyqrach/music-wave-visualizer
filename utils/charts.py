import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import librosa
import librosa.display

BG = "#0D0D1A"
SURFACE = "#1A1A2E"
ORANGE = "#E47028"
PURPLE = "#7530BF"
GRID = "#2A2A4A"
TEXT = "#F0EAF8"
MUTED = "#9B8BB4"


def _base_fig(figsize=(10, 3)):
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(SURFACE)
    ax.tick_params(colors=MUTED)
    ax.xaxis.label.set_color(MUTED)
    ax.yaxis.label.set_color(MUTED)
    ax.title.set_color(TEXT)
    for spine in ax.spines.values():
        spine.set_edgecolor(GRID)
    ax.grid(color=GRID, linewidth=0.5)
    return fig, ax


def plot_waveform(y: np.ndarray, sr: int) -> plt.Figure:
    time = np.arange(len(y)) / sr
    fig, ax = _base_fig()
    ax.plot(time, y, color=ORANGE, linewidth=0.8)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title("Waveform — Amplitude vs. Time")
    fig.tight_layout()
    return fig


def plot_fft(y: np.ndarray, sr: int) -> plt.Figure:
    n = len(y)
    freqs = np.fft.rfftfreq(n, d=1 / sr)
    magnitudes = np.abs(np.fft.rfft(y)) / n

    # Limit to 0–8000 Hz for readability
    mask = freqs <= 8000
    freqs = freqs[mask]
    magnitudes = magnitudes[mask]

    # Purple→orange gradient: map each bar by its position
    norm = mcolors.Normalize(vmin=0, vmax=len(freqs))
    cmap = mcolors.LinearSegmentedColormap.from_list(
        "synth", [PURPLE, ORANGE]
    )
    colors = [cmap(norm(i)) for i in range(len(freqs))]

    fig, ax = _base_fig()
    ax.bar(freqs, magnitudes, width=freqs[1] - freqs[0] if len(freqs) > 1 else 1,
           color=colors, linewidth=0)
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Magnitude")
    ax.set_title("Frequency Spectrum (FFT)")
    fig.tight_layout()
    return fig


def plot_spectrogram(y: np.ndarray, sr: int) -> plt.Figure:
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    S_db = librosa.power_to_db(S, ref=np.max)

    synth_cmap = mcolors.LinearSegmentedColormap.from_list(
        "synth_spec", [BG, PURPLE, ORANGE]
    )

    fig, ax = _base_fig(figsize=(10, 4))
    img = librosa.display.specshow(
        S_db, sr=sr, x_axis="time", y_axis="mel", ax=ax, cmap=synth_cmap
    )
    fig.colorbar(img, ax=ax, format="%+2.0f dB",
                 label="Power (dB)").ax.yaxis.label.set_color(MUTED)
    ax.set_title("Spectrogram — Frequency over Time")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Frequency (Hz, mel scale)")
    fig.tight_layout()
    return fig
