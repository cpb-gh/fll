### FUNCTION START
def zz_run_one():
    sensorL = ColorSensor ( 'D' )
    sensorR = ColorSensor ( 'C' )
    #start fast, arrive slow -> expo-in-out!
    gyro_straight(degrees = 900, start_power = 70, end_power = 60, easing=ExponentialEaseInOut, motor_stop_mode = brake, kp=2,)
    #back up from tv
    gyro_straight(degrees = -150, start_power = 30, end_power = 25, kp=0)
    #orient the robot towards windmill T
    turn_function(degrees = -45, easing = ExponentialEaseInOut, stoptype = 'brake', startspeed = 30, endspeed = 30, turntype = 'right')
    #move toward front of windmill
    gyro_straight(degrees = 720, start_power = 100, end_power = 30, kp=0.5, easing = ExponentialEaseInOut)
    #spin to face windmill head on
    turn_function(degrees=75, easing=ExponentialEaseOut, stoptype='brake', startspeed=50, endspeed=40, turntype = 'both')
    #charge at the windmill! hope we funnel onto it
    gyro_straight(degrees = 270, start_power = 50, end_power = 50, kp=0.5)
    #snag the energies
    t = Timer()
    control_attachments(start_speed=80, end_speed=80, degrees_wanted=1150, motor_letter = 'E', timeout_seconds = 3)
    wait_for_seconds(.5)
    control_attachments(start_speed=80, end_speed=80, degrees_wanted= -1150, motor_letter = 'E', timeout_seconds = 3)
    wait_for_seconds(.5)
    control_attachments(start_speed=80, end_speed=80, degrees_wanted=1150, motor_letter = 'E', timeout_seconds = 3)
    wait_for_seconds(.5)
    control_attachments(start_speed=80, end_speed=80, degrees_wanted= -1150, motor_letter = 'E', timeout_seconds = 3)
    #back up from windmill
    gyro_straight(degrees=-555, start_power=20, end_power=20, easing=ExponentialEaseInOut, kp=0)
    # moves the arm to not hit the toy factory
    control_attachments(start_speed=80, end_speed=80, degrees_wanted=550, motor_letter = 'E',)
    #move back to the base so we can prepare it to do something else
    turn_function(degrees=90, easing=ExponentialEaseOut, stoptype='brake', startspeed=50, endspeed=40, turntype = 'both')
    gyro_straight(degrees = 1200, start_power = 60, end_power = 60, kp=0.5)

    ### FUNCTION END
