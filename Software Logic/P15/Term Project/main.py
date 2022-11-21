from sense_hat import SenseHat
from time import sleep
import pygame
from threading import Thread

sense = SenseHat()

sense.clear()
pygame.init()
pygame.mixer.music.load("beep.wav")
count = 0
warning = False
# sense.set_rotation(180)

r = [255, 0, 0]
g = [0, 255, 0]
b = [0, 0, 0]

image_smile = [
    b, b, g, g, g, g, b, b,
    b, g, b, b, b, b, g, b,
    g, b, g, b, b, g, b, g,
    g, b, b, b, b, b, b, g,
    g, b, g, b, b, g, b, g,
    g, b, b, g, g, b, b, g,
    b, g, b, b, b, b, g, b,
    b, b, g, g, g, g, b, b
]

image_angry = [
    b, b, r, r, r, r, b, b,
    b, r, b, b, b, b, r, b,
    r, b, r, b, b, r, b, r,
    r, b, b, b, b, b, b, r,
    r, b, b, r, r, b, b, r,
    r, b, r, b, b, r, b, r,
    b, r, b, b, b, b, r, b,
    b, b, r, r, r, r, b, b, 
]

try:
    while True:
        if warning is True and count is not 0:
            sense.set_pixels(image_angry)
            pygame.mixer.music.play(-1)
            count = 0
        elif warning is False:
            sense.set_pixels(image_smile)
            pygame.mixer.music.stop()
            
        for event in sense.stick.get_events():
            if warning is False and event.action == "held" and event.direction == "middle":
                warning = True
                count += 1
            if warning is True and event.action == "pressed" and event.direction == "middle":
                warning = False
except KeyboardInterrupt:
    sense.clear()
    print("Program Stopped")
