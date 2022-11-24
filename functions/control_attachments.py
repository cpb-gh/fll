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
# NOTE - default parameters are evaluated at compile time
# so we need to set ease to "None" by default
#and then if it is "None" set our actual default "LinearInOut"
def control_attachments(start_speed=40, end_speed=100, ease=None, degrees_wanted=720, also_end_if = None, motor_stop_mode='BRAKE', motor_letter='C', timeout_seconds = 0):
    this_way = degrees_wanted>0
    t = Timer()
    t.reset()
    # if no ease, it sets the ease to linear
    if ease is None:
        ease = LinearInOut
    hub_motor = get_motor_by_letter( motor_letter )
    #it is presetting the count to 0
    hub_motor.preset( 0 )
    #set motor power to the start speed
    if (this_way):
        hub_motor.pwm( start_speed )
    else:
        hub_motor.pwm( -start_speed )

    keep_spinning = True

    while keep_spinning:
        speed, degrees_now, x, xx = hub_motor.get( )
        pct_to_degrees = abs(degrees_now) / abs(degrees_wanted)
        print (pct_to_degrees)

        #math for fanding speed based on how far we are.
        speed = start_speed + ease(pct_to_degrees) * (end_speed - start_speed)
        if this_way:
            hub_motor.pwm(speed)
        else:
            hub_motor.pwm(-speed)

        #need to test multiple conditions
        #1 to the left
        #2 to the right
        #3 if ouur passed in functions is true (if touching black)
        if  ((degrees_now >= degrees_wanted and this_way) or
            (degrees_now<=degrees_wanted and not this_way) or
            also_end_if==True):
            print( degrees_now, 'all done' )
            keep_spinning = False
        ### at the start we start a timer and if that timer excedes timeout_seconds then it will stop.
        if timeout_seconds != 0 and t.now() > timeout_seconds:
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
control_attachments( degrees_wanted=720, motor_letter='F')
