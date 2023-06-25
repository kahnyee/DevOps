import time
from threading import Thread
import queue

from hal import hal_led as led
from hal import hal_adc as adc
from hal import hal_moisture_sensor as moisture_sensor
from hal import hal_servo as servo
from hal import hal_temp_humidity_sensor as temp_humid_sensor
from hal import hal_dc_motor as dc_motor

from hal import dht11
from hal import hal_adc
from hal import hal_moisture_sensor
from hal import hal_temp_humidity_sensor
from hal import hal_servo
from hal import hal_led
from hal import hal_dc_motor

def potentiometer_reading():
    PotReadings = adc.get_adc_value(1)
    print(PotReadings)

def temperature_reading():
    TempReadings = temp_humid_sensor.read_temp_humidity()
    print(TempReadings[0])

def humidity_reading():
    HumiReadings = temp_humid_sensor.read_temp_humidity()
    print(HumiReadings[1])

def ldr_reading():
    LDRReadings = adc.get_adc_value(0)
    print(LDRReadings)

def moisture_reading():
    MoistReadings = hal_moisture_sensor.read_sensor()
    print(MoistReadings)


def main():
    # initialization of HAL modules
    led.init()
    adc.init()
    moisture_sensor.init()
    servo.init()
    temp_humid_sensor.init()
    dc_motor.init()

    while True:
        potentiometer_reading()
        temperature_reading()
        humidity_reading()
        ldr_reading()
        moisture_reading()

if __name__ == '__main__':
    main()