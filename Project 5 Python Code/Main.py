import time
from threading import Thread
import queue
from time import sleep as sleep

from hal import hal_led as led
from hal import hal_adc as adc
from hal import hal_moisture_sensor as moisture_sensor
from hal import hal_servo as servo
from hal import hal_temp_humidity_sensor as temp_humid_sensor
from hal import hal_dc_motor as dc_motor



def potentiometer_reading():
    PotReadings = adc.get_adc_value(1)
    print("Potentiometer: " + str(PotReadings))

def temperature_reading():
    TempReadings = temp_humid_sensor.read_temp_humidity()
    print("Temperature: " + str(TempReadings[0]))

def humidity_reading():
    HumiReadings = temp_humid_sensor.read_temp_humidity()
    print("Humidity: " + str(HumiReadings[1]))

def ldr_reading():
    LDRReadings = adc.get_adc_value(0)
    print("LDR: " + str(LDRReadings))

def moisture_reading():
    MoistReadings = moisture_sensor.read_sensor()
    print("Moisture: " + str(MoistReadings))


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
        print(" ")
        sleep(1)

if __name__ == '__main__':
    main()