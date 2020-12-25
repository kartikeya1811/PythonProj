from datetime import datetime
from pygame import mixer
import time
import schedule

# 9am - 5pm
# Water - water.mp3(3.5 litres) - Drank - log - every 40 mins
mixer.init()


def playwater():
    mixer.music.load("water.mp3")
    mixer.music.play()
    while True:
        dra = input("Enter response to log (Drank)\n ")
        if dra == "drank":
            mixer.music.stop()
            f = open("Log.txt", "a")
            f.write("[" + str(datetime.now()) + "] :" + " Drank \n")
            f.close()
        else:
            print("Invalid input")
            continue
        time.sleep(2)
        break


# Eyes - eyes.mp3 - every 30 min -- Eydone--log
def playeyes():
    mixer.music.load("eyes.mp3")
    mixer.music.play()
    while True:
        dra = input("Enter response to log (eydone)\n ")
        if dra == "eydone":
            mixer.music.stop()
            f = open("Log.txt", "a")
            f.write("[" + str(datetime.now()) + "] :" + " Eyes exercise done \n")
            f.close()
        else:
            print("Invalid input")
            continue
        time.sleep(2)
        break


schedule.every(40).minutes.do(playwater)
schedule.every(30).minutes.do(playeyes)
while True:
    schedule.run_pending()
