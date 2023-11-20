"""
Created by: sophie
Created on: Nov 2023
This module is a Micro:bit MicroPython program that moves a pixel around the edge.
"""

from microbit import *


# variables
y_coordinate = 0
x_coordinate = 0

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
        y_coordinate = 0
        x_coordinate = 0

        # loop that moves pixel down
        while y_coordinate <= 3:
            # loop that moves pixel right
            while x_coordinate <= 3:
                sleep(500)

                display.set_pixel(x_coordinate, y_coordinate, 9)
                sleep(500)
                display.clear()

                x_coordinate += 1
            sleep(500)
            display.clear()
            display.set_pixel(x_coordinate, y_coordinate, 9)
            y_coordinate += 1
        # delete pixel after it reaches (4, 3)
        display.clear()

        # loop that moves pixel up
        while y_coordinate >= 0:
            # loop that moves pixel left
            while x_coordinate >= 1:
                sleep(500)

                display.set_pixel(x_coordinate, y_coordinate, 9)
                sleep(500)
                display.clear()

                x_coordinate -= 1

            sleep(500)
            display.clear()
            display.set_pixel(x_coordinate, y_coordinate, 9)
            y_coordinate -= 1
        # when full turn is completed
        sleep(500)
        display.clear()
        display.show(Image.HEART)
