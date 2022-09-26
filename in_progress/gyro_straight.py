from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
import hub  

def gyro_straight( left_motor_letter='B', right_motor_letter='A', degrees=9000, start_power=100, end_power=50, easing='LINEAR', motor_stop_mode='BRAKE', also_stop_if = None ):
    motor_pair = MotorPair(left_motor_letter, right_motor_letter)
    motor_pair.start_tank(start_power, start_power)
    speed, relative_degrees, absolute_degrees, pwm = hub.port.A.motor.get()
    while True:
        speed, relative_degrees, absolute_degrees, pwm = hub.port.A.motor.get()
        print(relative_degrees)
        if relative_degrees >= degrees:
            motor_pair.stop()
            return
        wait_for_seconds(.1)
gyro_straight(start_power= 50000 ,degrees = 5000)
