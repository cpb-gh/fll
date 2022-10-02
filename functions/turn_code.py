### FUNCTION START

from spike import PrimeHub,MotorPair

def get_speed(start, end, percent):
    return int ( start + (end - start)*percent )



def turn_function(degrees=90, ease=None, stoptype='brake',
    startspeed=20, endspeed=40, motorletterleft='A', motorletterright='B',
    turntype='both'):

    neg = degrees<0

    hub = PrimeHub()


    hub.motion_sensor.reset_yaw_angle()
    motors = MotorPair(motorletterleft, motorletterright)
    keep_spinning = True
    while keep_spinning == True:
        degrees_now= hub.motion_sensor.get_yaw_angle()
        if neg and degrees_now <= degrees :
            keep_spinning = False
        elif not neg and degrees_now >= degrees :
            keep_spinning = False

        if keep_spinning:
            pct = degrees_now/degrees
  
            if ease is not None:
                pct = ease(pct)
            speed = get_speed (startspeed, endspeed, pct)

            if turntype is 'both':
                if neg:
                    motors.start_tank_at_power(-speed, speed)
                else:
                    motors.start_tank_at_power(speed, -speed)
            elif turntype is 'left':
                if neg:
                    motors.start_tank_at_power(-speed, 0)
                else:
                    motors.start_tank_at_power(speed, 0)
            elif turntype is 'right':
                if neg:
                    motors.start_tank_at_power(0,speed)
                else:
                    motors.start_tank_at_power(0,-speed)


    if stoptype is not None:
        motors.set_stop_action( stoptype )
        motors.stop()

### FUNCTION END

turn_function (degrees=-90, ease=None, stoptype='brake',
    startspeed=20, endspeed=40, motorletterleft='A', motorletterright='B', turntype='right')
