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
        ("'Cause you could be the one that I love", 0.08),
        ("I could be the one that you dream of", 0.08),
        ("Message in a bottle is all I can do", 0.08),
        ("Standin' here, hopin' it gets to you", 0.08),
        ("You could be the one that I keep, and I", 0.08),
        ("Could be the reason you can't sleep at night", 0.08),
        ("Message in a bottle is all I can do", 0.08),
        ("Standin' here, hopin' it gets to you", 0.08)
    ]
    
    delays = [0.0, 3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0]

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