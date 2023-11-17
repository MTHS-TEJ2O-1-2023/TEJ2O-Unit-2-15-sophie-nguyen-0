"""
Created by: sophie
Created on: Nov 2023
This module is a Micro:bit MicroPython program makes LED light go around the edge of Microbit
"""

from microbit import *


# variables
x_counter = 0
y_counter = 0
loop_counter = 0

# setup
display.clear()
display.show(Image.HEART)
sleep(1000)

# loop
while True:
    if button_a.is_pressed():
        # setup
        display.clear()
        y_counter = 0
        x_counter = 0

        while loop_counter <= 2:
            while x_counter < 5:
                sleep(500)
                display.set_pixel(x_counter, y_counter, 9)
                x_counter += 1

            while y_counter < 5:
