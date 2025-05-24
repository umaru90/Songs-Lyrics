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

# Fungsi menampilkan lirik dengan animasi ketik
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
    
    placeholder = st.empty()
    for lyric, speed, delay in lyrics:
        # Tunggu sampai waktu lirik sesuai delay
        time.sleep(delay - (time.time() - start_time))
        animated_text = ""
        for char in lyric:
            animated_text += char
            placeholder.markdown(f"### {animated_text}")
            time.sleep(speed)

# Streamlit UI
st.title("🎶 Lirik Lagu: Gak Karuan")
if os.path.exists(AUDIO_FILE):
    st.markdown(get_audio_html(AUDIO_FILE), unsafe_allow_html=True)
else:
    st.warning("File lagu tidak ditemukan di folder 'songs/'. Harap upload 'gak karuan.mp3'.")

if st.button("Mulai Tampilkan Lirik"):
    start_time = time.time()
    display_lyrics()
