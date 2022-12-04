
### FUNCTION START
### this will TRY to get to the power plant and fail.
def zz_run_four():
    gyro_straight(degrees = 360, start_power = 70, end_power = 60, easing=ExponentialEaseInOut, motor_stop_mode = brake,kp = 1)
    turn_function(degrees=25, easing=None, stoptype='brake',startspeed=40, endspeed=40, motorletterleft='A',also_end_if = None, motorletterright='B',turntype='both', timeout_seconds = 0)
    gyro_straight(degrees = 170, start_power = 70, end_power = 60, easing=ExponentialEaseInOut, motor_stop_mode = brake,kp = 1)
    turn_function(degrees=-25, easing=None, stoptype='brake',startspeed=40, endspeed=40, motorletterleft='A',also_end_if = None, motorletterright='B',turntype='both', timeout_seconds = 0)
    def sensed_black_right(letter_one = 'C', letter_two = 'D'):
        color_sensor_one = ColorSensor(letter_one)
        color_sensor_two = ColorSensor(letter_two)
        color_one = color_sensor_one.get_color()
        color_two = color_sensor_two.get_color()
        if color_one == 'black':
            return True
        else:
            return False
    gyro_straight(degrees = 720, start_power = 50, end_power = 40, easing=ExponentialEaseInOut, motor_stop_mode = brake,kp = 1, also_stop_if = sensed_black_right)
    line_follow( Sspeed=30, Espeed=30, sensorLetter="C", stopIf=None, stopMode='brake', degrees=900, motorLeftletter = 'A', motorRightletter='B')
### FUNCTION END
