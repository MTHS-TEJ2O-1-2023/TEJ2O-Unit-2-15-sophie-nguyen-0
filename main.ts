/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Sophie
 * Created on: Nov 2023
 * This program moves a sprite around the edge of the microbit.
*/

// variables
let stepCounter: number = 0
let turningCounter: number = 0
let sprite: game.LedSprite = null

// setup
basic.clearScreen()
// snowflake
basic.showLeds(`
    # . # . #
    . # # # .
    # # . # #
    . # # # .
    # . # . #
`)

// when button A is pressed, move sprite around edge
input.onButtonPressed(Button.A, function () {
  // prep screen
  basic.clearScreen()
  sprite = game.createSprite(0, 0)

  turningCounter = 0
  while (turningCounter <= 3) {
    stepCounter = 0
    while (stepCounter <= 4) {
      basic.pause(500)
      sprite.move(1)
      stepCounter++
      }
    sprite.turn(Direction.Right, 90)
    turningCounter++
  }

  sprite.delete()
  basic.pause(500)

  // snowflake
  basic.showLeds(`
    # . # . #
    . # # # .
    # # . # #
    . # # # .
    # . # . #
  `)
})

