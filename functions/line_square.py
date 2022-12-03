
from spike import PrimeHub, MotionSensor, Motor, MotorPair, ColorSensor
from spike.control import wait_for_seconds, wait_until, Timer
import math
import hub
from spike.control import wait_until

### FUNCTION START

def line_square ( speed=40, color_to_hit='black', sensorletterleft='D', sensorletterright='C', motorletterleft='A', motorletterright='B', overshoot_seconds = 0 ):
    print("=== line squaring")
    motors = MotorPair(motorletterleft, motorletterright)
    motors.set_stop_action('brake')
    sensorL = ColorSensor ( sensorletterleft )
    sensorR = ColorSensor ( sensorletterright )
    sensor_left_color = sensorL.get_color()
    sensor_right_color = sensorR.get_color()

    if sensor_right_color != color_to_hit and sensor_left_color != color_to_hit:
        print("neither sensor on color_to_hit, returning...")
        return

    if sensor_right_color == color_to_hit and sensor_left_color == color_to_hit:
        print("both sensors on color_to_hit, returning...")
        return

    if sensor_left_color == color_to_hit:
        leftfirst = True
    else:
        leftfirst = False

    def hit_colorL():
        # print( 'left', sensorL.get_color() )
        return sensorL.get_color() == color_to_hit

    def hit_colorR():
        # print( 'right', sensorR.get_color() )
        return sensorR.get_color() == color_to_hit

    if (leftfirst == True):
        if not hit_colorL ():
            motors.start_tank (speed, 0)
            wait_until (hit_colorL)
        if not hit_colorR ():
            motors.start_tank (0, speed)
            wait_until (hit_colorR)
    else:
        if not hit_colorR ():
            print('A')
            motors.start_tank (0, speed)
            wait_until (hit_colorR)
        if not hit_colorL ():
            print( 'B' )
            motors.start_tank (speed, 0)
            wait_until (hit_colorL)
    ### depending on what angle you hit a black line you have to overshoot with the second sensor to square it
    wait_for_seconds(overshoot_seconds)
    motors.stop()

### FUNCTION END
