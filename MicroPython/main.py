"""
Created by: sophie
Created on: Nov 2023
This module is a Micro:bit MicroPython program that moves a pixel around the edge.
"""

from microbit import *


# variables
y_coordiante = 0
x_coordiante = 0

# setup
display.clear()
display.show(Image.HEART)
sleep(1000)

# loop
while True:
    if button_a.is_pressed():
        # setup
        display.clear()

        # reset variables
        y_coordiante = 0
        x_coordiante = 0

        # loop that moves pixel down
        while y_coordiante <= 3:
            # loop that moves pixel right
            while x_coordiante <= 3:
                sleep(500)

                display.set_pixel(x_coordiante, y_coordiante, 9)
                sleep(500)
                display.clear()

                x_coordiante += 1
            sleep(500)
            display.clear()
            display.set_pixel(x_coordiante, y_coordiante, 9)
            y_coordiante += 1
        # delete pixel after it reaches (4, 3)
        display.clear()

        # loop that moves pixel up
        while y_coordiante >= 0:
            # loop that moves pixel left
            while x_coordiante >= 1:
                sleep(500)

                display.set_pixel(x_coordiante, y_coordiante, 9)
                sleep(500)
                display.clear()

                x_coordiante -= 1

            sleep(500)
            display.clear()
            display.set_pixel(x_coordiante, y_coordiante, 9)
            y_coordiante -= 1
        # when full turn is completed
        sleep(500)
        display.clear()
        display.show(Image.HEART_SMALL)
