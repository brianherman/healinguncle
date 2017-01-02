#!/usr/bin/env python

import colorsys
import time
from sys import exit

try:
    import numpy
except ImportError:
    exit("This script requires the numpy module\nInstall with: sudo pip install numpy")

import unicornhat as unicorn


print("""Random Blinky

Blinks random yellow-orange-red LEDs.

If you're using a Unicorn HAT and only half the screen lights up, 
edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
""")

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()


while True:
    for y in range(height):
        for x in range(width):
            unicorn.set_pixel(x, y, 255, 255, 255)
    unicorn.show()
    time.sleep(0.025)
    for y in range(height):
        for x in range(width):
            unicorn.set_pixel(x, y, 0, 0, 0)
    unicorn.show()
    time.sleep(0.025)
