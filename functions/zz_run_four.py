
### FUNCTION START
def zz_run_four():
    sensorL = ColorSensor ( 'D' )
    sensorR = ColorSensor ( 'C' )
    def see_black_left():
        return sensorL.get_color() is 'black'
    def see_black_right():
        return sensorR.get_color() is 'black'

    gyro_straight(degrees=1000, start_power=50, end_power=50, also_stop_if=see_black_left, kp=1)
    line_follow(degrees=750, stopIf=see_black_right)
    turn_function(degrees=-5, turntype='left', timeout_seconds=1, startspeed=40, endspeed=40)
    gyro_straight(degrees=400, start_power=100, end_power=100, timeout_seconds=3)
    control_attachments(degrees_wanted=-100, start_speed=100, end_speed=100, motor_letter='E', timeout_seconds=1)
    control_attachments(degrees_wanted=-150 ,start_speed=70, end_speed=70, motor_letter='F', timeout_seconds=1)
    gyro_straight(degrees=-400, start_power=40, end_power=40)
    turn_function(degrees=25, turntype='left', startspeed=40, endspeed=40)
    gyro_straight(degrees=-2000, start_power=100, end_power=100, kp=2)
### FUNCTION END
