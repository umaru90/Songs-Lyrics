import sys
import time
import threading

lock = threading.Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay_before, speed):
    time.sleep(delay_before)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("kau tak pernah katakan apa kurangnya ku untukmu", 0.0, 0.09),
        ("namun ku tak sebanding meskipun aku di sampingmu", 0.5, 0.07),
        ("dan kau masih cinta yang lalu",1.0, 0.08),
        ("dia pergi kau menunggu", 1.3, 0.07),
        ("baik kau pergi berhenti bebani diriku", 1.5, 0.1),
        ("lihatlah aku, ku menunggu mu", 1.9, 0.16),
        ("namun kau s'lalu pikir masa lalu", 2.6, 0.12),
        ("lihatlah aku, ku menunggu mu", 3.2, 0.16),
        ("namun kau s'lalu pikir masa lalu", 3.8, 0.12),
    ]

    threads = []
    for lyric, delay_before, speed in lyrics:
        t = threading.Thread(target=sing_lyric, args=(lyric, delay_before, speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
