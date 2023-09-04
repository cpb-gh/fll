from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

def get_speed( low_speed, high_speed, pct ):
    return low_speed+((high_speed-low_speed)*pct)


### FUNCTION START
def line_follow( Sspeed=40, Espeed=20, sensorLetter="D", stopIf=None, stopMode='brake', degrees=1000, motorLeftletter = 'A', motorRightletter='B', kp=0.4):

    motor_pair = MotorPair(motorLeftletter, motorRightletter)
    motor1 = Motor(motorLeftletter)
    motor2 = Motor(motorRightletter)

    color = ColorSensor(sensorLetter)
    stop = False
    integral = 0
    lastError = 0

    motor1.set_degrees_counted(0)
    motor2.set_degrees_counted(0)
    if stopMode is not None:
        motor_pair.set_stop_action(stopMode)
    while stop == False:
        # if we've gone as far as we need to go, then stop
        mdeg1 = motor1.get_degrees_counted()
        mdeg2 = motor2.get_degrees_counted()
        motordeg = (abs(mdeg1) + abs(mdeg2))/ 2
        if motordeg >= degrees:
            stop = True

        # this is how close to the final distance (degrees) we are,
        # then we set "speed" to the speed we want to be at
        # based on how close to the end we are.
        pct = motordeg/degrees
        speed = get_speed( Sspeed, Espeed, pct )

        # now we calculate P_fix, I_fix, and D_fix for our PID function
        # Proportional, Integral, Derivative

        # error should be negative if we need to turn one direction or positive the other direction
        # get_reflected_light is a number 0 (black) - 100 (white) so subtracting 50 gets us -50 - 50
        error = color.get_reflected_light() - 50
        
        P_fix = error * kp # P_fix is the error above times a factor - it's a snapshot/point in time correction

        # integral starts at 0 and then we add the error (which can be negative), so this is accumulating error over time
        integral = integral + error
        I_fix = integral * 0.001 # 0.001 is like the kp for I_fix

        # lastError starts at 0 and gets subtracted from the current error to get "derivative"
        # so this is a trailing indicator of the last two error amounts
        derivative = error - lastError
        lastError = error
        D_fix = derivative * 1 # the kp for D_fix is 1

        correction = P_fix+I_fix+D_fix # correct is the sum of our P, I, and D_fix's

        motor_pair.start_tank_at_power(int(speed+correction), int(speed-correction)) # add the correction from one wheel and subtract from the other to cause a turn

        if stop == True and stopMode is not None:
            motor_pair.stop()
### FUNCTION END
