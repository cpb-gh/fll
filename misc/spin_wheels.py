# script for spinning wheels for cleaning
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')

motor_pair = MotorPair('A', 'B')
motor_pair.start_tank(70, 70)
wait_for_seconds(20)
motor_pair.stop()
