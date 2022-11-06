from spike import MotorPair, ColorSensor

from spike.control import wait_until

### FUNCTION START

def line_square ( speed=40, color_to_hit='black',leftfirst=True, sensorletterleft='E', sensorletterright='D', motorletterleft='A', motorletterright='B' ):
    motors = MotorPair(motorletterleft, motorletterright)
    motors.set_stop_action('brake')
    sensorL = ColorSensor ( sensorletterleft )
    sensorR = ColorSensor ( sensorletterright )

    def hit_colorL():
        print( 'left', sensorL.get_color() )
        return sensorL.get_color() == color_to_hit

    def hit_colorR():
        print( 'right', sensorR.get_color() )
        return sensorR.get_color() == color_to_hit

    if (leftfirst == True):
        if not hit_colorL ():
            motors.start_tank (speed, 0)
            wait_until (hit_colorL)
        if not hit_colorR ():
            motors.start_tank (0, speed)
            wait_until (hit_colorR)
    else:
        if not hit_colorR ():
            print('A')
            motors.start_tank (0, speed)
            wait_until (hit_colorR)
        if not hit_colorL ():
            print( 'B' )
            motors.start_tank (speed, 0)
            wait_until (hit_colorL)

    motors.stop()

### FUNCTION END

line_square ()
