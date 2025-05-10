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
        ("Nineteen, but you act twenty-five now", 0.07),
        ("Knees weak, but you talk pretty fly, wow", 0.07),
        ("Ripped jeans and a cup that you just downed", 0.06),
        ("Take me where the music ain't too loud", 0.07),
        ("Trade drinks, but you don't even know her", 0.07),
        ("Save me 'til the party is over", 0.07),
        ("Kiss me in the seat of your Rover", 0.07),
        ("Real sweet, but I wish you were sober", 0.07)
    ]
    
    delays = [0.3, 2.7, 5.3, 8.0, 10.0, 13.3, 16.0, 18.5]

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