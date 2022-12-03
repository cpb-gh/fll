

### FUNCTION START
def zz_run_two():
    ### dumps the energy into the toy factory
    gyro_straight( left_motor_letter='A', right_motor_letter='B', degrees=900, start_power=50, end_power=50, easing = None, motor_stop_mode = brake, kp = 0.5)
    gyro_straight( left_motor_letter='A', right_motor_letter='B', degrees=-1000, start_power=50, end_power=50, easing = None, motor_stop_mode = brake, kp = 0.5)
### FUNCTION END
