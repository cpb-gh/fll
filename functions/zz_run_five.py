### FUNCTION START
### this will put the mission model and energy into the middle and go to the right side of the board. This is the last run
def zz_run_five():
    gyro_straight( left_motor_letter='A', right_motor_letter='B', degrees=1640, start_power=100, end_power=40, easing = None, motor_stop_mode = brake, kp = 0.5, timeout_seconds = 0 )
    control_attachments(start_speed=50, end_speed=50, ease=None, degrees_wanted=580, also_end_if = None, motor_stop_mode='BRAKE', motor_letter='F', timeout_seconds = 0)
    gyro_straight( left_motor_letter='A', right_motor_letter='B', degrees=300, start_power=50, end_power=50, easing = None, motor_stop_mode = brake, kp = 0.5, timeout_seconds = 0 )
    turn_function(degrees=75, easing=None, stoptype='brake',startspeed=20, endspeed=20, motorletterleft='A',also_end_if = None, motorletterright='B',turntype='both', timeout_seconds = 0)
    gyro_straight( left_motor_letter='A', right_motor_letter='B', degrees=720, start_power=50, end_power=50, easing = None, motor_stop_mode = brake, kp = 0.5, timeout_seconds = 0 )
    turn_function(degrees=-45, easing=None, stoptype='brake',startspeed=20, endspeed=20, motorletterleft='A',also_end_if = None, motorletterright='B',turntype='both', timeout_seconds = 0)
    gyro_straight( left_motor_letter='A', right_motor_letter='B', degrees=1100, start_power=50, end_power=50, easing = None, motor_stop_mode = brake, kp = 0.5, timeout_seconds = 0 )
### FUNCTION END
