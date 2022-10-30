

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
    #setting primehub and resseting the gyro
    hub = PrimeHub()
    hub.motion_sensor.reset_yaw_angle()
    # tweak this value for better straighness
    kp = 0.3
    # if no ease, set easing to linier 
    if easing is None:
        easing = LinearInOut
    #get a motor pair
    motor_pair = MotorPair(left_motor_letter, right_motor_letter)
    motor_left = get_motor_by_letter(left_motor_letter)
    motor_right = get_motor_by_letter(right_motor_letter)
    #we are going to count rotations and preset function is resetting the counter 
    motor_right.preset(0)
    motor_left.preset(0)
    #how far we've moved. increment pct degrees as we roll
    pct_degrees = 0
    #get moving
    motor_pair.start_tank(start_power, start_power)
    keep_moving=true
    while keep_moving is True:
        #get information from each motor
        #relative degree's are reset by preset above
        speed_right, relative_degrees_right = motor_right.get()
        speed_left, relative_degrees_left = motor_left.get()
        #how far have we moved? average the left and right
        relative_degrees = (abs(relative_degrees_right) + abs(relative_degrees_left)) / 2
        # how far in pct have we traveled??
        pct_degrees = relative_degrees / degrees
        #pipe our pct through to get an eased pct through
        pct_power = easing(pct_degrees)
        # we are calculating the change of the power and then 
        # finding how far we are from our start power to our end power
        pwrchange = end_power - start_power
        act_power = int( start_power + pct_power * pwrchange )
        # getting the yaw angle
        yaw = hub.motion_sensor.get_yaw_angle()
        # scaling it with kp
        correction = yaw*kp
        # keep moving with the correction adustment
        motor_pair.start_tank(int(act_power+correction), int(act_power-correction))
        if also_stop_if() == True or relative_degrees >= degrees:
            motor_stop_mode(motor_pair)
            keep_moving = False
### FUNCTION END
gyro_straight(degrees = 2000, start_power = 20, end_power = 100, easing = LinearInOut)
