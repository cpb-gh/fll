import hub
import math

"""
Linear
"""
def LinearInOut(t):
    return t

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
def control_attachments(start_speed=40, end_speed=100, ease=LinearInOut, degrees_wanted=720, also_end_if = None, motor_stop_mode='BRAKE', motor_letter='C'):

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
