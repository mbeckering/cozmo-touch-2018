#!/usr/bin/env python3
import cozmo
from cozmo.util import degrees, distance_inches, speed_mmps

########## Utility Functions ##########
def driveInches(robot, inches):
    robot.drive_straight(distance_inches(inches), speed_mmps(50)).wait_for_completed()

def turnDegrees(robot, nDegrees):
    robot.turn_in_place(degrees(nDegrees)).wait_for_completed()

def turnRight(robot):
    turnDegrees(robot, -90)

def turnLeft(robot):
    turnDegrees(robot, 90)

########## Main ##########
def main(robot: cozmo.robot.Robot):
    driveInches(robot, 9)
    turnRight(robot)
    driveInches(robot, 10)
    turnLeft(robot)
    driveInches(robot, 10)

########## Run Program ##########
cozmo.run_program(main)
