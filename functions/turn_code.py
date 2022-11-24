### FUNCTION START
def get_speed(start, end, percent):
    return int ( start + (end - start)*percent )



def turn_function(degrees=90, easing=None, stoptype='brake',startspeed=40, endspeed=30, motorletterleft='A', motorletterright='B',turntype='both', timeout_seconds = 0):

    neg = degrees<0

    hub = PrimeHub()


    hub.motion_sensor.reset_yaw_angle()
    motors = MotorPair(motorletterleft, motorletterright)
    t = Timer()
    t.reset()
    keep_spinning = True
    while keep_spinning == True:
        degrees_now= hub.motion_sensor.get_yaw_angle()
        if neg and degrees_now <= degrees :
            keep_spinning = False
        elif not neg and degrees_now >= degrees :
            keep_spinning = False

        if timeout_seconds != 0 and t.now() > timeout_seconds:
            keep_spinning = False

        if keep_spinning:
            pct_degrees = degrees_now/degrees
            pct_power = pct_degrees
            

            if easing is not None:
                pct_power = easing(pct_degrees)
            speed = get_speed (startspeed, endspeed, pct_power)

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
