from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

### FUNCTION START
def get_speed( low_speed, high_speed, pct ):
    return low_speed+((high_speed-low_speed)*pct)


def line_follow( Sspeed=40, Espeed=20, sensorLetter="D", 
                 stopIf=None, stopMode='brake', ease = None, degrees=1000,
                 motorLeftletter = 'A', motorRightletter='B'):
    
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
        mdeg1 = motor1.get_degrees_counted()
        mdeg2 = motor2.get_degrees_counted()
        motordeg = (abs(mdeg1) + abs(mdeg2))/ 2
        if motordeg >= degrees:
            stop = True

        pct = motordeg/degrees 
        if ease is not None:
            pct = ease( pct )
        
        speedy = get_speed( Sspeed, Espeed, pct )
        # print(  'speedy', speedy )



        speed = speedy

        error = color.get_reflected_light() - 50
        P_fix = error * 0.3

        integral = integral + error
        
        I_fix = integral * 0.001

        derivative = error - lastError
        lastError = error
        D_fix = derivative * 1

        correction = P_fix+I_fix+D_fix

        motor_pair.start_tank_at_power(int(speed-correction), int(speed+correction))

        if stop == True and stopMode is not None:
            motor_pair.stop()
 
### FUNCTION END

