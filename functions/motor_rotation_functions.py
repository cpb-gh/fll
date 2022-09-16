from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
import hub
### FUNCTION START
def motor_to_degrees(degrees=90, power=100, port='A'):
    hub_motor = get_motor_by_letter(port)
    hub_motor.preset(0)
    hub_motor.pwm(power)
    degrees_wanted = degrees

    keep_spinning = True
    while keep_spinning:
        speed, relative_degrees, absolute_degrees, pwm = hub_motor.get()
        if relative_degrees >= degrees_wanted:
            keep_spinning = False 
        if keep_spinning == False:
            hub_motor.brake()
### FUNCTION END
