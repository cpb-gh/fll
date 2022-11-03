from spike import PrimeHub, MotionSensor, Motor, MotorPair, ColorSensor
from spike.control import wait_for_seconds, wait_until, Timer
import math
import hub


def BounceEaseIn(t):
    return 1 - BounceEaseOut(1 - t)

def BounceEaseOut(t):
    if t < 4 / 11:
        return 121 * t * t / 16
    elif t < 8 / 11:
        return (363 / 40.0 * t * t) - (99 / 10.0 * t) + 17 / 5.0
    elif t < 9 / 10:
        return (4356 / 361.0 * t * t) - (35442 / 1805.0 * t) + 16061 / 1805.0
    return (54 / 5.0 * t * t) - (513 / 25.0 * t) + 268 / 25.0

def BounceEaseInOut(t):
    if t < 0.5:
        return 0.5 * BounceEaseIn(t * 2)
    return 0.5 * BounceEaseOut(t * 2 - 1) + 0.5


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

def LinearInOut(t):
    return t

def ExponentialEaseIn(t):
    if t == 0:
        return 0
    return math.pow(2, 10 * (t - 1))



### FUNCTION START

def coast(motor_pair):
    motor_pair.set_stop_action('coast')
    motor_pair.stop()

def hold(motor_pair):
    motor_pair.set_stop_action('hold')
    motor_pair.stop()

def brake(motor_pair):
    motor_pair.set_stop_action('brake')
    motor_pair.stop()


def sensed_black(letter_one = 'C', letter_two = 'D'):
    color_sensor_one = ColorSensor(letter_one)
    color_sensor_two = ColorSensor(letter_two)
    color_one = color_sensor_one.get_color()
    color_two = color_sensor_two.get_color()
    if color_one == 'black' and color_two == 'black':
        return True
    else:
        return False

# NOTE - default parameters are evaluated at compile time so we need to set easing to "None" by default and then if it is "None" set our actual default "LinearInOut"
def gyro_straight( left_motor_letter='A', right_motor_letter='B', degrees=9000, start_power=100, end_power=50, easing = None, motor_stop_mode = brake, kp = 0.5, also_stop_if = lambda: False ):
    # if the user did not specify what easing function they wanted to use then it will just do LinerInOut; a straight line 
    if easing is None:
        easing = LinearInOut

    #swap letters if going backwards
    go_fwd = degrees > 0
    left_motor_fwd_letter = left_motor_letter
    right_motor_fwd_letter = right_motor_letter
    if not go_fwd:
        left_motor_fwd_letter = right_motor_letter
        right_motor_fwd_letter = left_motor_letter

    motor_pair = MotorPair(left_motor_fwd_letter, right_motor_fwd_letter)
    motor_left = get_motor_by_letter(left_motor_fwd_letter)
    motor_right = get_motor_by_letter(right_motor_fwd_letter)
    # motor_right.preset(0) will reset the relative degrees because otherwise the second time you run this function the relative degrees will start where it left off last time
    motor_right.preset(0)
    motor_left.preset(0)
    pct_degrees = 0

    #resetting things, setting up hub
    my_hub = PrimeHub()
    my_hub.motion_sensor.reset_yaw_angle()
    #right here we start our motor
    motor_pair.start_tank(start_power, start_power)

    # while true is the same as a forever loop and we just say "return" when we want to exit   
    while True:
        speed_right, relative_degrees_right, absolute_degrees_right, pwm_right = motor_right.get()
        speed_left, relative_degrees_left, absolute_degrees_left, pwm_left = motor_left.get()
        speed = (speed_right + speed_left) / 2
        relative_degrees = (abs(relative_degrees_right) + abs(relative_degrees_left)) / 2
        pct_degrees = relative_degrees / degrees
        pct_power = easing(pct_degrees)
        act_power = int(pct_power * (end_power - start_power) + start_power)
        # right now we are getting our yaw angle (our left and right) to see if we have veered off course then we correct our motors to turn.
        # we only turn slighty by kp (how much our robot reacts to being off course) of what we are of by as to not overshoot and then have to correct agian.
        yaw = my_hub.motion_sensor.get_yaw_angle()
        correction = int(yaw * kp)
        motor_pair.start_tank(act_power - correction, act_power + correction)
        # when we arive at our destination we need to stop and exit the loop.
        if also_stop_if() == True or relative_degrees >= abs(degrees):
            motor_stop_mode(motor_pair)
            #return overshoot
            return relative_degrees - abs(degrees)
### FUNCTION END
gyro_straight(degrees = 2500, start_power = 100, end_power = 50, easing = LinearInOut ,  left_motor_letter = 'A', right_motor_letter ='B')
