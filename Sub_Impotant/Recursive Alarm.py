# Error in every lap code taker 0.0151238441sec extra time
import time
from pygame import mixer

mixer.init()
mixer.music.load('Alarm Sound.mp3')
print("Start")
i = 0
x = 3600  # 1 hour
# a = time.time()
while True:
    time.sleep(x-26-0.0151238441)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
    i += 1
    print(f"Lap:-{i}")

# print(time.time()-a)