from gpiozero import LED, Button
from psonic import *
import time
from random import uniform

red = LED(5)
yellow = LED(6)
green = LED(13)

button1 = Button(2)
button2 = Button(3)
button3 = Button(4)

while True:
    if button1.is_pressed:
        time.sleep(0.3)
        print("Button 1 Pressed")
        red.on()
        sample(LOOP_AMEN, rate=uniform(0.5,2))
    elif button2.is_pressed:
        time.sleep(0.1)
        print("Button 2 is Pressed")
        yellow.on()
        play(G5)
    elif button3.is_pressed:
        time.sleep(0.1)
        print("Button 3 is Pressed")
        green.on()
        play(D5)
    else:
        red.off()
        yellow.off()
        green.off()
        
