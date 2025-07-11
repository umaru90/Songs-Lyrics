import streamlit as st
import time
import base64
import os

AUDIO_FILE = os.path.join("songs", "calon mantu terbaik mamamu.mp3")

# Fungsi untuk meng-embed audio player
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

# Efek ketikan karakter per karakter
def typewriter_effect(text, container, speed=0.05):
    typed = ""
    for char in text:
        typed += char
        container.markdown(
            f"<p style='font-size:22px; font-weight:500'>{typed}</p>",
            unsafe_allow_html=True
        )
        time.sleep(speed)

# Menampilkan lirik dengan animasi ketikan
def display_lyrics():
    lyrics = [
        ("But do you feel it too? 🤔", 0.07, 0.5),
        ("Like the way I do? 💭", 0.07, 2.8),
        ("Aku calon mantu terbaik mamamu 👨‍💼💍", 0.06, 4.9),
        ("Walaupun hatimu ❤️‍🔥", 0.08, 7.7),
        ("Sekeras batu 🪨", 0.08, 9.5),
        ("Still got you on mind 🧠❤️", 0.06, 11.2),
        ("No matter what you do 🙅‍♂️✅", 0.06, 13.2),
        ("But do you feel it too? 🤔", 0.07, 15.1),
        ("Like the way I do? 💭", 0.07, 17.2),
        ("Aku calon mantu terbaik mamamu 💍👔", 0.06, 19.1),
        ("Walaupun hatimu 💘🧱", 0.08, 21.9),
        ("Sekeras batu 🪨😤", 0.08, 23.7)
    ]

    st.markdown("## 🎤 Lirik:")
    containers = [st.empty() for _ in lyrics]
    start_time = time.time()

    for i, (lyric, speed, delay) in enumerate(lyrics):
        time.sleep(max(0, delay - (time.time() - start_time)))
        typewriter_effect(lyric, containers[i], speed)

# Konfigurasi halaman
st.set_page_config(page_title="Lirik Calon Mantu", layout="centered")
st.title("🎶 Calon Mantu Terbaik Mamamu 🎶")

# Cek file dan tampilkan UI
if os.path.exists(AUDIO_FILE):
    st.markdown(get_audio_html(), unsafe_allow_html=True)

    if st.button("▶ Mulai"):
        st.markdown("<script>playAudio()</script>", unsafe_allow_html=True)
        display_lyrics()
else:
    st.warning("File 'calon mantu terbaik mamamu.mp3' belum ditemukan di folder 'songs/'.")
