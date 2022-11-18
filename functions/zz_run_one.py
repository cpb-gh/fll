from spike.control import Timer

### FUNCTION START
def zz_run_one():
    sensorL = ColorSensor ( 'D' )
    sensorR = ColorSensor ( 'C' )
    #start fast, arrive slow -> expo-in-out!
    gyro_straight(degrees = 750, start_power = 60, end_power = 30, easing=ExponentialEaseInOut, motor_stop_mode = brake, kp=2)
    #back up from tv
    gyro_straight(degrees = -150, start_power = 30, end_power = 25, kp=0)
    #orient the robot towards windmill T
    turn_function(degrees = -45, easing = ExponentialEaseInOut, stoptype = 'brake', startspeed = 30, endspeed = 30, turntype = 'right')
    #move toward front of windmill
    gyro_straight(degrees = 720, start_power = 100, end_power = 30, kp=0.5, easing=ExponentialEaseInOut)
    #spin to face windmill head on
    turn_function(degrees=85, easing=ExponentialEaseOut, stoptype='brake', startspeed=30, endspeed=20, turntype = 'both')
    #charge at the windmill! hope we funnel onto it
    gyro_straight(degrees = 350, start_power = 30, end_power = 30, kp=0.5)
    #snag the energies
    control_attachments(start_speed=80, end_speed=80, degrees_wanted=1200, motor_letter = 'E')
    control_attachments(start_speed=80, end_speed=80, degrees_wanted= -1200, motor_letter = 'E')
    control_attachments(start_speed=80, end_speed=80, degrees_wanted=1200, motor_letter = 'E')
    control_attachments(start_speed=80, end_speed=80, degrees_wanted= -1200, motor_letter = 'E')
    #back up from windmill
    gyro_straight(degrees=-205, start_power=20, end_power=20, easing=ExponentialEaseInOut, kp=0)
    #turn to the T near the car
    turn_function(degrees=-125, easing=ExponentialEaseInOut, stoptype='brake', startspeed=30, endspeed=30, turntype = 'both')
    wait_for_seconds(1)
    #advance to the T near the car
    gyro_straight(degrees=400, easing=ExponentialEaseInOut,start_power=30, end_power=30, kp=0)
    def hit_color_black():
        hit = sensorL.get_color() == 'black' or sensorR.get_color() == "black"
        return hit
    #stop on the black on the T and line up
    gyro_straight(degrees=250, start_power=30, end_power=30, kp=0, also_stop_if=hit_color_black)
    line_square(overshoot_seconds=0.1)
    wait_for_seconds(1)

    #turn so we are facing between highfive and car
    timer = Timer()
    then = timer.now()
    def three_sec():
        now = timer.now()
        return now - then >= 3
    turn_function(degrees=43, startspeed=20, endspeed=20, turntype='both', also_end_if=three_sec)
    wait_for_seconds(1)
    #move betweek highfive and car
    gyro_straight(degrees=360, start_power=30, end_power=30, kp=0)
    #HIGH FIVE!!!
    control_attachments(start_speed=80, end_speed=80, degrees_wanted=900, motor_letter = 'E')
    control_attachments(start_speed=100, end_speed=100, degrees_wanted=-900, motor_letter = 'E')

    #get a little closer to the car
    then = timer.now()
    def one_sec():
        now = timer.now()
        return now - then >= 1
    turn_function(degrees=10, startspeed=25, endspeed=25, turntype='both', also_end_if=one_sec)
    wait_for_seconds(1)
    #quickly lift up the arm to release the car
    control_attachments(motor_letter='F', degrees_wanted=-55, start_speed=100, end_speed=70, ease=ExponentialEaseInOut)

### FUNCTION END
