from spike import PrimeHub, LightMatrix, Button, StatusLight, ColorSensor, Speaker
from spike.control import wait_for_seconds

### FUNCTION START

def start_run( color_sensor_letter = 'C', delay = 1):
    color = ColorSensor(color_sensor_letter)
    status_light = StatusLight()
    speaker = Speaker()
    while True:
        the_color = color.get_color()
        if the_color == 'red':
            print ( 'Detected red')
            status_light.on('red')
            speaker.beep(60, delay)
        elif the_color == 'blue':
            print ('Detected blueeee')
            status_light.on('blue')
            speaker.beep(100, delay)
        elif the_color == None:
            print ('NONE')
            status_light.off()

### FUNCTION END
start_run(color_sensor_letter = 'D', delay = 5)


