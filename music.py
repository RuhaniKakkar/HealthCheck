from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stophere):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        b=input()
        if b==stophere:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg}{datetime.now()}\n")

if __name__ == '__main__':
    twater = time()
    teyes = time()
    texercise = time()
    watersecs=5
    exsecs=10
    eyesecs=20

    while True:
        if time() - twater > watersecs:
            print("water drinking time. enter 'drank' to stop")
            musiconloop('water.mp3', 'drank')
            twater=time()
            log_now("Drank water at")

        if time() - teyes > eyesecs:
            print("eye exercise time. enter 'doneeyes' to stop")
            musiconloop('ocean_eyes.mp3', 'doneeyes')
            teyes = time()
            log_now("eyes relaxed at")

        if time() - texercise > exsecs:
            print("physical exercise time. enter 'donewithit' to stop")
            musiconloop('john_cena_theme.mp3', 'donewithit')
            texercise = time()
            log_now("physical exercise at")



