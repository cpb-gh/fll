import hub
import math

"""
Linear
"""
def LinearInOut(t):
    return t

def ExponentialEaseIn(t):
    if t == 0:
        return 0
    return math.pow(2, 10 * (t - 1))

def get_motor_by_letter( motor_letter ):
    if motor_letter == 'A':
        return hub.port.A.motor
    if motor_letter == 'B':
        return hub.port.B.motor
    if motor_letter == 'C':
        return hub.port.C.motor
    if motor_letter == 'D':
        return hub.port.D.motor
    if motor_letter == 'E':
        return hub.port.E.motor
    if motor_letter == 'F':
        return hub.port.F.motor

### FUNCTION START
# NOTE - default parameters are evaluated at compile time so we need to set east to "None" by default and then if it is "None" set our actual default "LinearInOut"
def control_attachments(start_speed=40, end_speed=100, ease=None, degrees_wanted=720, also_end_if = None, motor_stop_mode='BRAKE', motor_letter='C'):
    if ease is None:
        ease = LinearInOut
    hub_motor = get_motor_by_letter( motor_letter )
    hub_motor.preset( 0 )
    hub_motor.pwm( start_speed )

    keep_spinning = True

    while keep_spinning:
        speed, degrees_now, ignore_this, pwm = hub_motor.get( )

        pct_to_degrees = degrees_now / degrees_wanted
        print( 'degrees', degrees_now, pct_to_degrees )

        speed=start_speed+ease(pct_to_degrees)*(end_speed-start_speed)
        hub_motor.pwm(speed)

        if degrees_now >= degrees_wanted or also_end_if==True:
            keep_spinning = False

        if keep_spinning == False:
            if motor_stop_mode == 'BRAKE':
                hub_motor.brake( )
            elif motor_stop_mode == 'FLOAT':
                hub_motor.float( )
            elif motor_stop_mode == 'HOLD':
                hub_motor.hold( )
### FUNCTION END

#call the function we just wrote
control_attachments(motor_stop_mode='FLOAT', motor_letter='A', ease=ExponentialEaseInOut)
control_attachments(motor_stop_mode='FLOAT', motor_letter='B', degrees_wanted=1000) 
