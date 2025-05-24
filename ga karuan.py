import time
import streamlit as st
import base64
import os

# Lokasi file mp3 di folder songs
AUDIO_FILE = os.path.join("songs", "gak karuan.mp3")

# Fungsi untuk meng-embed audio ke dalam Streamlit
def get_audio_html(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        return f"""
        <audio controls autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """

# Fungsi menampilkan lirik secara bertahap (semua ditampilkan, bukan overwrite)
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
    container = st.container()
    start_time = time.time()

    for lyric, speed, delay in lyrics:
        sleep_time = max(0, delay - (time.time() - start_time))
        time.sleep(sleep_time)
        container.markdown(f"<p style='font-size:22px; font-weight:500'>{lyric}</p>", unsafe_allow_html=True)

# Streamlit UI
st.set_page_config(page_title="Lirik Gak Karuan", layout="centered", initial_sidebar_state="collapsed")
st.title("🎶 Gak Karuan - RYO 🎶")

# Tampilkan player
if os.path.exists(AUDIO_FILE):
    st.markdown(get_audio_html(AUDIO_FILE), unsafe_allow_html=True)
    display_lyrics()
else:
    st.warning("File lagu tidak ditemukan di folder 'songs/'. Harap upload 'gak karuan.mp3'.")
