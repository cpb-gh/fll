### START FUNCTION
def party_mode(color_sensor_one = 'C', color_sensor_two = 'D', party_length = 20):
    from random import random
    cs_one = ColorSensor(color_sensor_one)
    cs_two = ColorSensor(color_sensor_two)
    timer = Timer()
    timer.reset()

    # the first half of the party is random lights at random intensities
    while timer.now() < (party_length/2):
        intensity = int(100 * random())
        light_choice = 6 * random()
        if light_choice <= 1:
            cs_one.light_up(intensity, 0, 0)
        elif light_choice <= 2:
            cs_one.light_up(0, intensity, 0)
        elif light_choice <= 3:
            cs_one.light_up(0, 0, intensity)
        elif light_choice <= 4:
            cs_two.light_up(intensity, 0, 0)
        elif light_choice <= 5:
            cs_two.light_up(0, intensity, 0)
        elif light_choice <= 6:
            cs_two.light_up(0, 0, intensity)
        wait_for_seconds(0.05)
    cs_one.light_up_all(0)
    cs_two.light_up_all(0)
    wait_for_seconds(0.2)

    # the second half of the paty is bright blinking lights
    # at random intervals
    toggle = 1
    while timer.now() < party_length:
        wait_time = random() * 0.25
        cs_one.light_up_all(100 * toggle)
        cs_two.light_up_all(100 * toggle)
        wait_for_seconds(wait_time)
        if toggle == 1:
            toggle = 0
        else:
            toggle = 1

    # turn off the lights at the end of the party
    cs_one.light_up_all(0)
    cs_two.light_up_all(0)
### END FUNCTION
