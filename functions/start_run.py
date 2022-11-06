from spike import PrimeHub, LightMatrix, Button, StatusLight, ColorSensor, Speaker
from spike.control import wait_for_seconds

### FUNCTION START


def start_run( color_sensor_letter = 'C', delay = 1):
    # color_sensor_letter = 'C' means that the active sensor is on the right side of the robot when it is facing the same direction as you
    color = ColorSensor(color_sensor_letter)
    status_light = StatusLight()
    speaker = Speaker()
    waiting_for_run = True
    while waiting_for_run:
        the_color = color.get_color()
        if the_color == 'red':
            print ( 'Detected:', the_color)
            status_light.on('red')
            speaker.beep(60, delay)
            zz_run_one()
            waiting_for_run = False
        elif the_color == 'yellow':
            print ( 'Detected:', the_color)
            status_light.on('red')
            speaker.beep(60, delay)
            #zz_run_two()
            waiting_for_run = False
        else:
            print ('not a run color:', the_color)
            status_light.off()


### FUNCTION END
start_run(color_sensor_letter = 'D', delay = 5)
