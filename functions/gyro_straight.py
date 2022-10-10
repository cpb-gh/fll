from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math
import hub

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
def gyro_straight( left_motor_letter='B', right_motor_letter='A', degrees=9000, start_power=100, end_power=50, easing = None, motor_stop_mode = brake, also_stop_if = lambda: False ):
    if easing is None:
        easing = LinearInOut
    motor_pair = MotorPair(left_motor_letter, right_motor_letter)
    color = ColorSensor('C')
    motor_left = get_motor_by_letter(left_motor_letter)
    motor_right = get_motor_by_letter(right_motor_letter)
    # motor_right.preset(0) will reset the relative degrees because otherwise the second time you run this function the relative degrees will start where it left off last time
    motor_right.preset(0)
    speed, relative_degrees, absolute_degrees, pwm = motor_right.get()
    #easing stuff.
    pct_degrees = 0
    print("Start:", speed, relative_degrees, absolute_degrees, pwm)
    motor_pair.start_tank(start_power, start_power)
    #motor stop mode
    while True:
        speed, relative_degrees, absolute_degrees, pwm = motor_right.get()
        pct_degrees = relative_degrees / degrees
        pct_power = easing(pct_degrees)
        act_power = int(pct_power * (end_power - start_power) + start_power)
        motor_pair.start_tank(act_power, act_power)
        if also_stop_if() == True or relative_degrees >= degrees:
            # FIXME: look at the line_follow function and use those braking methods instead so we are consistent - we can use a MotorPair object here
            motor_stop_mode(motor_pair)
            return
### FUNCTION END
gyro_straight(degrees = 2000, start_power = 20, end_power = 100, easing = LinearInOut)
