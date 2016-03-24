from gpiozero import LED, Button
from psonic import *
import time

red = LED(5)
yellow = LED(6)
green = LED(13)

button1 = Button(2)
button2 = Button(3)
button3 = Button(4)

while True:
    if button1.is_pressed:
        time.sleep(0.1)
        print("Button 1 Pressed")
        red.on()
        play(c)
    elif button2.is_pressed:
        time.sleep(0.1)
        print("Button 2 is Pressed")
        yellow.on()
        play(g)
    elif button3.is_pressed:
        time.sleep(0.1)
        print("Button 3 is Pressed")
        green.on()
        play(d)
    else:
        red.off()
        yellow.off()
        green.off()
        
