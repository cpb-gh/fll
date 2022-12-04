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
        return sensorR.get_color() is 'white'

    # from start position, move to middle of field
    gyro_straight(degrees=1700, start_power=90, end_power=60, easing=ExponentialEaseInOut, kp=1)
    wait_for_seconds(1)

    #turn to get distance from the power plant
    turn_function(degrees=10, startspeed=40, endspeed=30)
    wait_for_seconds(1)

    #move forward till black
    gyro_straight(degrees=360, start_power=30, end_power=30, easing=ExponentialEaseInOut, also_stop_if=see_black_either)
    wait_for_seconds(1)
    #keep on going
    gyro_straight(degrees= 110, start_power=40, end_power=40)
    wait_for_seconds(1)
    #now, swing your tail to unlock power plant energies
    turn_function(degrees=90, startspeed=40, endspeed=40, timeout_seconds=1, easing=ExponentialEaseOut, turntype="both")
    #and back up to let the energies out
    wait_for_seconds(1)
    control_attachments(motor_letter="E",start_speed=40, end_speed=40, degrees_wanted=-500)
    gyro_straight(degrees=-400, start_power=80, end_power=60, kp=1)
    #forward to the high five!
    gyro_straight(degrees=500, start_power=40, end_power=40, kp=1)
    #turn_function(degrees=45,startspeed=40,endspeed=40,also_end_if=see_black_left)
    wait_for_seconds(1)
    gyro_straight(degrees=400)
    control_attachments(motor_letter="E", start_speed=40, end_speed=40, degrees_wanted=-1500)
    control_attachments(motor_letter="E", start_speed=40, end_speed=40, degrees_wanted=1500)
    turn_function(degrees=-40, startspeed=40, endspeed=40, timeout_seconds=1, easing=ExponentialEaseOut, turntype="both")

    # for i in range(2):
    #     gyro_straight(degrees=-180, start_power=40, end_power=40, kp=2)
    #     gyro_straight(degrees=190, start_power=40, end_power=40,kp=2)
    # gyro_straight(degrees=-400, kp=2, start_power=40, end_power=40)
    # turn_function(degrees=-45, startspeed=40, endspeed=40, turntype="left")

    # # turn_function(degrees=-15, startspeed=50, endspeed=50)
    # gyro_straight(degrees=1000, start_power=40, end_power=40)

### FUNCTION END
