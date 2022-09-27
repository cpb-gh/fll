from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
import hub  

color_sensor_one = ColorSensor('C')
color_sensor_two = ColorSensor('D')
 
def sesnsed_black():
   color_one = color_sensor_one.get_color()
   color_two = color_sensor_two.get_color()
   if color_one = 'black' and color_two = 'black':
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
    motor_pair.start_tank(start_power, start_power)
    motor_left = get_motor_by_letter(left_motor_letter)
    motor_right = get_motor_by_letter(right_motor_letter)
    speed, relative_degrees, absolute_degrees, pwm = motor_left.get()
    while True:
        speed, relative_degrees, absolute_degrees, pwm = motor_right.get()
        print(relative_degrees)
        if relative_degrees >= degrees:
            motor_pair.stop()
            return
        wait_for_seconds(.1)
gyro_straight(start_power= 50000 ,degrees = 5000)
