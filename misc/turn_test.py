from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
motor_pair = MotorPair('A','B')

def spin_test (degrees=90, power=100, stop_action='coast'):
    hub.motion_sensor.reset_yaw_angle()
    motor_pair.set_stop_action(stop_action)
    spinning = True
    our_degrees = hub.motion_sensor.get_yaw_angle()
    motor_pair.start_tank_at_power(power, -1 * power)
    while spinning:
        our_degrees = hub.motion_sensor.get_yaw_angle()
        if our_degrees >= degrees:
            spinning = False
            motor_pair.stop()
            wait_for_seconds(0.1)
    our_degrees = hub.motion_sensor.get_yaw_angle()
    print("test_power:{}, test_degrees: {}, our_degrees: {}, error: {}".format(power, degrees,our_degrees, our_degrees-degrees))

powers = range(20,100,5)
degs = range(5,80,5)
for power in powers:
    for d in degs:
        spin_test(degrees=d,power=power)
