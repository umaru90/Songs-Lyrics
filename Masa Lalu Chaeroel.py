import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
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
        ("Kau-kau-kau tak pernah katakan apa kurangnya ku untukmu", 0.08),
        ("Namun, ku tak sebanding meskipun aku di sampingmu", 0.08),
        ("Dan kau masih cinta yang lalu, dia pergi, kaumenunggu", 0.08),
        ("Baik kaupergi, berhenti bebani diriku", 0.08),
        ("Lihatlah aku, ku menunggumu", 0.08),
        ("Namun, kau s'lalu pikir masa lalu", 0.08),
        ("Lihatlah aku, ku menunggumu", 0.08),
        ("Namun, kau s'lalu pikir masa lalu", 0.08)
    ]
    
    delays = [0.0, 3.5, 7.0, 10.5, 14.0, 17.5, 21.0, 24.5]

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