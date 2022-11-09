from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
 
LEFT_COLOR_SENSOR = 'D'
RIGHT_COLOR_SENSOR = 'C'
LEFT_WHEEL = 'A'
RIGHT_WHEEL = 'B'
FRONT_ATTACHMENT_MOTOR = 'F'
BACK_ATTACHMENT_MOTOR = 'E'
my_hub = PrimeHub()

def port_finder():
    # for this function please put your robot with the right side colorsensor on black and left on a different color.          
    for port in ['A', 'B', 'C', 'D', 'E', 'F']:
        try:
            found_colorsensor_port = True
            orange_smoothie = ColorSensor(port)
        except RuntimeError as error:
            #print(error)
            if str(error)  == "There is not a color sensor connected to port {}".format(port):
                found_colorsensor_port = False
        try:
            found_motor_port = True
            purple_potato = Motor(port)
        except RuntimeError as error:
            #print(error)
            if str(error) == "There is not a motor connected to port {}".format(port):
                found_motor_port = False
        if found_colorsensor_port:
            color = None
            while color is None:
                color = orange_smoothie.get_color()
            if color == 'black' and port == RIGHT_COLOR_SENSOR:
                print("found correct right side color sensor at port {}".format(RIGHT_COLOR_SENSOR))
            elif port == LEFT_COLOR_SENSOR and color !=  'black':
                print("found correct left side color sensor at port {}".format(LEFT_COLOR_SENSOR))
            else:
                print("Found colorsensor at incorrect port {}, seeing {}".format(port, color))
        elif found_motor_port:
            # print("found motor on port {}".format(port))
            my_hub.motion_sensor.reset_yaw_angle()
            if port == LEFT_WHEEL:
                print("should spin left wheel")
            if port == RIGHT_WHEEL:
                print("should spin right wheel")
            if port == FRONT_ATTACHMENT_MOTOR:
                print("should spin front attachment motor")
            if port == BACK_ATTACHMENT_MOTOR:
                print("should spin back attachment motor")
            wait_for_seconds(2)
            purple_potato.run_for_seconds(0.5, -30)
            yaw = my_hub.motion_sensor.get_yaw_angle()
            if yaw != 0:
                print("found wheel motor at port {}".format(port))
            else:
                print("found attachment motor at port {}".format(port))
            

port_finder()
