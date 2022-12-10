### FUNCTION START

def zz_run_three():
    sensorL = ColorSensor ( 'D' )
    sensorR = ColorSensor ( 'C' )
    def see_black_either():
        return sensorL.get_color() is 'black' or sensorR.get_color() is 'black'
    def see_black_left():
        return sensorL.get_color() is 'black'
    def see_black_right():
        return sensorR.get_color() is 'black'
    def see_white_left():
        return sensorL.get_color() is 'white'
    def see_white_either():
        return sensorR.get_color() is 'white'or sensorL.get_color() is 'white'
    def see_white_right():
        return sensorR.get_color() is 'white'

    #from start position, move to middle of field
    gyro_straight(degrees=1550, start_power=40, end_power=40, kp=0.5)
    wait_for_seconds(1)
    turn_function(degrees=30, startspeed=30, endspeed=30)
    wait_for_seconds(1)
    gyro_straight(degrees=550, timeout_seconds=2, start_power=60, end_power=60)
    wait_for_seconds(1)
    turn_function(degrees=20, startspeed=30, endspeed=30)
    wait_for_seconds(1)
    gyro_straight(degrees=700, start_power=70, end_power=40, kp=0.5, timeout_seconds=2)
    gyro_straight(degrees=-170, start_power=40, end_power=40)
    # high five
    control_attachments(motor_letter="E", start_speed=100, end_speed=100, degrees_wanted=-2700)
    control_attachments(motor_letter="E", start_speed=100, end_speed=100, degrees_wanted=2700)
    #back up
    gyro_straight(degrees=-200, start_power=40, end_power=40)
    # knock out water
    turn_function(degrees=-45, startspeed=30, endspeed=30)
    # line back up
    turn_function(degrees=28, startspeed=30, endspeed=30)
    # keep backin up
    gyro_straight(degrees=-50, start_power=40, end_power=40)

    turn_function(degrees=-10, startspeed=30, endspeed=30)
    gyro_straight(degrees=1000, start_power=40, end_power=40, also_stop_if=see_black_left)
    line_follow(degrees=600, stopIf=see_black_right)
    for i in range(3):
        gyro_straight(degrees=360, start_power=40, end_power=40, timeout_seconds=1)
        gyro_straight(degrees=-180, start_power=40, end_power=40, timeout_seconds=1)
    turn_function(degrees=-45, startspeed=30, endspeed=30)
    gyro_straight(degrees=1500, start_power=100, end_power=100)
    control_attachments(motor_letter="E", start_speed=100, end_speed=100, degrees_wanted=-2500)

### FUNCTION END
