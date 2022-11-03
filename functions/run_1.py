### FUNCTION START
def run_one():
    gyro_straight(degrees = 900, start_power = 70, end_power = 100, easing = ExponentialEaseOut, motor_stop_modde = brake)
    gyro_straight(degrees = -100, start_power = 30, end_power = 30)
    turn_function(degrees = -25, easing = None, stoptype = 'brake', startspeed = 60, endspeed = 50,  motorletterleft = 'A', motorletterright = 'B', turntype = 'both')
