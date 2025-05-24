import streamlit as st
import time
import base64
import os

AUDIO_FILE = os.path.join("songs", "gak karuan.mp3")

# Audio base64 embed
def get_audio_html():
    with open(AUDIO_FILE, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        return f"""
        <audio id="audioPlayer" controls>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        <script>
        function playAudio() {{
            var audio = document.getElementById("audioPlayer");
            audio.currentTime = 0;
            audio.play();
        }}
        </script>
        """

# Ketikan animasi per baris
def typewriter_effect(text, container, speed=0.05):
    typed = ""
    for char in text:
        typed += char
        container.markdown(f"<p style='font-size:22px; font-weight:500'>{typed}</p>", unsafe_allow_html=True)
        time.sleep(speed)

# Lirik
def display_lyrics():
    lyrics = [
        ("Lama-lama bosan tiap malam telfonan", 0.08, 0.3),
        ("Aduh-aduh kapan kita ketemuan", 0.09, 4.0),
        ("Lama-lama makin lama makin sayang", 0.08, 7.5),
        ("Kok jadi gini rasanya aku gak karuan", 0.09, 10.0),
        ("", 0.5, 14.0),
        ("Sekarang udah malam", 0.15, 14.0),
        ("Masih sama seperti kemaren", 0.09, 17.5),
        ("Kamu dan aku udah saling ngerti", 0.08, 21.5),
        ("Ku tak mau lama-lama", 0.12, 25.0)
    ]

    st.markdown("## 🎤 Lirik:")
    containers = [st.empty() for _ in lyrics]
    start_time = time.time()
    for i, (lyric, speed, delay) in enumerate(lyrics):
        time.sleep(max(0, delay - (time.time() - start_time)))
        typewriter_effect(lyric, containers[i], speed)

# Streamlit UI
st.set_page_config(page_title="Lirik Gak Karuan", layout="centered")
st.title("🎶 Gak Karuan - RYO 🎶")

if os.path.exists(AUDIO_FILE):
    st.markdown(get_audio_html(), unsafe_allow_html=True)

    if st.button("▶ Mulai"):
        # Jalankan JS play audio
        st.markdown("<script>playAudio()</script>", unsafe_allow_html=True)
        display_lyrics()
else:
    st.warning("File gak karuan.mp3 belum ditemukan di folder 'songs/'.")
