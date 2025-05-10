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
        ("saat pertama kulihat senyum mu", 0.08),
        ("jantung ini berdetak tak karuan", 0.08),
        ("andai saja ku bisa katakan", 0.08),
        ("tapi tuk mendekat ku rasa malu", 0.08),
        ("oh tapi tak mungkin ku rasa tak mungkin", 0.08),
        ("kau balik suka rasanya mustahil", 0.08),
        ("kau dan aku hanyalah mimpi", 0.08),
        ("biarkan-biarkan aku terus begini", 0.08)
    ]
    
    delays = [0.0, 4.0, 6.5, 11.0, 15.0, 18.0, 22.0, 26.0]

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
