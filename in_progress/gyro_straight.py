from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
import hub

def sensed_black(letter_one = 'C', letter_two = 'D'):
    color_sensor_one = ColorSensor(letter_one)
    color_sensor_two = ColorSensor(letter_two)
    color_one = color_sensor_one.get_color()
    color_two = color_sensor_two.get_color()
    if color_one == 'black' and color_two == 'black':
        return True
    else:
        return False

def get_motor_by_letter(port):
    if port =='A':
        return hub.port.A.motor
    if port == 'B':
        return hub.port.B.motor
    if port == 'C':
        return hub.port.C.motor
    if port == 'D':
        return hub.port.D.motor
    if port == 'E':
        return hub.port.E.motor
    if port == 'F':
        return hub.port.F.motor

def gyro_straight( left_motor_letter='B', right_motor_letter='A', degrees=9000, start_power=100, end_power=50, easing='LINEAR', motor_stop_mode='BRAKE', also_stop_if = None ):
    motor_pair = MotorPair(left_motor_letter, right_motor_letter)
    motor_left = get_motor_by_letter(left_motor_letter)
    motor_right = get_motor_by_letter(right_motor_letter)
    # motor_right.preset(0) will reset the relative degrees because otherwise the second time you run this function the relative degrees will start where it left off last time 
    motor_right.preset(0)
    speed, relative_degrees, absolute_degrees, pwm = motor_right.get()
    print("Start:", speed, relative_degrees, absolute_degrees, pwm)
    motor_pair.start_tank(start_power, start_power)
    while True:
        speed, relative_degrees, absolute_degrees, pwm = motor_right.get()
        #print(speed, relative_degrees, absolute_degrees, pwm)
        if also_stop_if() == True or relative_degrees >= degrees:
            motor_pair.stop()
            return
        #wait_for_seconds(.5)
