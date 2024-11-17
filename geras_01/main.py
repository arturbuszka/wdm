#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *


# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)
pen_in3 = Pen(INPUT_1)
motorC = LargeMotor(OUTPUT_C) # Magnet


#Hereis where your code starts

#POMOC:

speed = 30

print("Start")
#first letter
pen_in3.down()
motorC.on(100)
steering_drive.on_for_rotations(0, speed, 3.5)
steering_drive.on_for_rotations(100, speed, 0.70)
steering_drive.on_for_rotations(0, speed, 2)
steering_drive.on_for_rotations(100, speed, 0.70)
steering_drive.on_for_rotations(0, speed, 3.5)
pen_in3.up()
steering_drive.on_for_rotations(100, speed, 1.4)
steering_drive.on_for_rotations(0, speed, 1.75)
steering_drive.on_for_rotations(-100, speed, 0.70)
pen_in3.down()
steering_drive.on_for_rotations(0, speed, 2)
pen_in3.up()
steering_drive.on_for_rotations(100, speed, 1.4)
steering_drive.on_for_rotations(0, speed, 2.5)
steering_drive.on_for_rotations(100, speed, 0.70)
steering_drive.on_for_rotations(0, speed, 1.6)
#second letter
steering_drive.on_for_rotations(-100, speed, 0.70)
motorC.on(0)
steering_drive.on_for_rotations(0, speed, 1)
steering_drive.on_for_rotations(-100, speed, 0.70)
pen_in3.down()
steering_drive.on_for_rotations(0, speed, 3.5)
steering_drive.on_for_rotations(100, speed, 0.70)
steering_drive.on_for_rotations(0, speed, 2)
steering_drive.on_for_rotations(100, speed, 0.70)
steering_drive.on_for_rotations(0, speed, 3.5)
steering_drive.on_for_rotations(100, speed, 0.70)
steering_drive.on_for_rotations(0, speed, 2)
pen_in3.up()
steering_drive.on_for_rotations(100, speed, 0.70)
steering_drive.on_for_rotations(0, speed, 2)
steering_drive.on_for_rotations(100, speed, 0.70)
pen_in3.down()
steering_drive.on_for_rotations(0, speed, 2)
pen_in3.up()
steering_drive.on_for_rotations(0, speed, 2)


#print("Turn")
#steering_drive.on_for_rotations(100, speed, 2)
#motorC.on(0)
#pen_in3.up()
#steering_drive.on_for_rotations(0, speed, 2)


