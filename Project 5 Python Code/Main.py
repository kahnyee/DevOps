import time
from threading import Thread
import queue

from hal import hal_led as led
from hal import hal_adc as adc
from hal import hal_moisture_sensor as moisture_sensor
from hal import hal_servo as servo
from hal import hal_temp_humidity_sensor as temp_humid_sensor
from hal import hal_dc_motor as dc_motor

def main():
    # initialization of HAL modules
    led.init()
    adc.init()
    moisture_sensor.init()
    servo.init()
    temp_humid_sensor.init()
    dc_motor.init()

    while (True):

if __name__ == '__main__':
    main()