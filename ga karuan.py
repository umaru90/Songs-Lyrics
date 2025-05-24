import time
import streamlit as st
import base64
import os
import uuid

AUDIO_FILE = os.path.join("songs", "gak karuan.mp3")

def get_audio_html(file_path, autoplay=False):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        audio_id = "audioPlayer"
        auto_attr = "autoplay" if autoplay else ""
        return f"""
        <audio id="{audio_id}" controls {auto_attr}>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """

def inject_audio_control_script():
    return """
    <script>
    function replayAudio() {
        var audio = document.getElementById("audioPlayer");
        if (audio) {
            audio.pause();
            audio.currentTime = 0;
            audio.play();
        }
    }
    </script>
    """

def typewriter_effect(text, container, speed=0.05):
    typed = ""
    for char in text:
        typed += char
        container.markdown(f"<p style='font-size:22px; font-weight:500'>{typed}</p>", unsafe_allow_html=True)
        time.sleep(speed)

def display_lyrics():
    lyrics = [
        ("Lama-lama bosan tiap malam telfonan", 0.08, 0.3),
        ("Aduh-aduh kapan kita ketemuan", 0.09, 4.0),
        ("Lama-lama makin lama makin sayang", 0.08, 8.0),
        ("Kok jadi gini rasanya aku gak karuan", 0.09, 10.0),
        ("", 0.5, 14.0),
        ("Sekarang udah malam", 0.15, 15.0),
        ("Masih sama seperti kemaren", 0.09, 18.5),
        ("Kamu dan aku udah saling ngerti", 0.08, 22.5),
        ("Ku tak mau lama-lama", 0.12, 26.0)
    ]

    st.markdown("## 🎤 Lirik:")
    containers = [st.empty() for _ in lyrics]
    start_time = time.time()

    for i, (lyric, speed, delay) in enumerate(lyrics):
        time.sleep(max(0, delay - (time.time() - start_time)))
        typewriter_effect(lyric, containers[i], speed)

# UI setup
st.set_page_config(page_title="Lirik Gak Karuan", layout="centered", initial_sidebar_state="collapsed")
st.title("🎶 Lirik Lagu: Gak Karuan")

if os.path.exists(AUDIO_FILE):
    st.markdown(get_audio_html(AUDIO_FILE, autoplay=False), unsafe_allow_html=True)
    st.markdown(inject_audio_control_script(), unsafe_allow_html=True)

    # Tombol untuk play ulang audio + lirik
    if st.button("🔁 Putar Ulang Lagu dan Lirik"):
        st.experimental_rerun()

    display_lyrics()
else:
    st.warning("File lagu tidak ditemukan di folder 'songs/'. Harap upload 'gak karuan.mp3'.")
