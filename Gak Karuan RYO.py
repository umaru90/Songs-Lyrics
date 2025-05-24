import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.08):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Lama-lama bosan tiap malam telfonan", 0.08),
        ("Aduh-aduh kapan kita ketemuan", 0.09),
        ("Lama-lama makin lama makin sayang", 0.08),
        ("Kok jadi gini rasanya aku gak karuan", 0.09),
        ("", 0.5),  # Spasi antar bait
        ("Sekarang udah malam", 0.15),
        ("Masih sama seperti kemaren", 0.09),
        ("Kamu dan aku udah saling ngerti", 0.08),
        ("Ku tak mau lama-lama", 0.12)
    ]
    
    delays = [0.3, 4.0, 8.0, 10.0, 14.0, 15.0, 18.5, 22.5, 26.0]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
