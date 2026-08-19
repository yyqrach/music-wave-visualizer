import streamlit as st
from utils.styles import inject_styles

st.set_page_config(page_title="Extra Resources — Music Wave Visualizer", layout="wide")
inject_styles()

st.title("Extra Resources")
st.markdown(
    '<p class="muted">A curated collection of links to deepen your understanding of sound physics and music acoustics.</p>',
    unsafe_allow_html=True,
)

st.markdown("---")

st.subheader("Physics of Sound")
st.markdown(
    """
- [**The Physics of Sound** — The Physics Classroom](https://www.physicsclassroom.com/class/sound) — Comprehensive text-based lessons on wave properties, resonance, and the Doppler effect.
- [**Sound Waves** — Khan Academy](https://www.khanacademy.org/science/physics/mechanical-waves-and-sound) — Free video lessons and exercises on mechanical waves and sound, great for exam prep.
- [**Acoustics and Vibrations Animations** — Dan Russell, Penn State](https://www.acs.psu.edu/drussell/demos.html) — Animated visualizations of longitudinal and transverse waves, standing waves, and more.
    """
)

st.markdown("---")

st.subheader("Music Theory & Acoustics")
st.markdown(
    """
- [**Musicacoustics.edu** — University of New South Wales](https://www.musicacoustics.unsw.edu.au/) — In-depth articles on how specific instruments produce sound, including diagrams and audio samples.
- [**How Musical Instruments Work** — HyperPhysics](http://hyperphysics.phy-astr.gsu.edu/hbase/Music/musinscon.html) — Concise physics explanations for strings, wind, and percussion instruments.
- [**Music and Mathematics** — Plus Magazine](https://plus.maths.org/content/music-mathematics) — Accessible articles on the maths behind scales, tuning systems, and harmonics.
    """
)

st.markdown("---")

st.subheader("Tools & Further Exploration")
st.markdown(
    """
- [**Audacity**](https://www.audacityteam.org/) — Free, open-source audio editor. Record your own instrument, export as WAV, and upload it here.
- [**Chrome Music Lab — Spectrogram**](https://musiclab.chromeexperiments.com/Spectrogram/) — Interactive in-browser spectrogram; sing or play into your microphone and see your voice in real time.
- [**Desmos Graphing Calculator**](https://www.desmos.com/calculator) — Plot sine waves and explore how changing amplitude and frequency affects the wave shape.
- [**Hearing Range Test**](https://www.youtube.com/watch?v=qNf9nzvnd1k) — YouTube video that sweeps from 20 Hz to 20 kHz so you can find the edges of your own hearing range.
    """
)
