import time
from threading import Thread
import DataGeneration
import light_intensity
import ec_level
import temperature
from hal import hal_adc as adc
from hal import hal_moisture_sensor as moisture_sensor
from hal import hal_temp_humidity_sensor as temp_humid_sensor

def potentiometer_reading():
    Potentiometer = adc.get_adc_value(1)
    print("Potentiometer: " + str(Potentiometer))
    return Potentiometer

def temperature_humidity_reading():
    Temperature, Humidity = temp_humid_sensor.read_temp_humidity()
    print("Temperature : " + str(Temperature))
    print("Humidity : " + str(Humidity))
    temperature.temperature_data(Temperature)
    return [Temperature, Humidity]

def ldr_reading():
    LDR = adc.get_adc_value(0)
    print("LDR: " + str(LDR))
    return LDR

def moisture_reading():
    Moisture_sensor = moisture_sensor.read_sensor()
    print("Moisture: " + str(Moisture_sensor))
    return Moisture_sensor

def main():
    adc.init()
    moisture_sensor.init()
    temp_humid_sensor.init()

    light_intensity_thread = Thread(target=light_intensity.main)
    ec_level_thread = Thread(target=ec_level.main)
    temperature_thread = Thread(target=temperature.main)
    light_intensity_thread.start()
    ec_level_thread.start()
    temperature_thread.start()

    while True:
        Potentiometer = potentiometer_reading()
        Temperature, Humidity = temperature_humidity_reading()
        LDR = ldr_reading()
        Moisture_sensor = moisture_reading()
        if Temperature != -100:
            DataGeneration.DataGeneration(Temperature, Humidity, Moisture_sensor, Potentiometer, LDR)
        print(" ")
        time.sleep(5)

if __name__ == '__main__':
    main()