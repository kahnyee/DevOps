import time
import subprocess
import os
import DataGeneration
import light_intensity
import ec_level
import temperature
from hal import hal_adc as adc
from hal import hal_moisture_sensor as moisture_sensor
from hal import hal_temp_humidity_sensor as temp_humid_sensor

#Moisture sensor subprocess
file_location_MS = os.path.realpath(__file__)
directory_MS = os.path.dirname(file_location_MS)
file_path_MS = os.path.join(directory_MS, "ec_level.py").replace("\\", "/")
process_MS = None

#Temperature subprocess
file_location_T = os.path.realpath(__file__)
directory_T = os.path.dirname(file_location_T)
file_path_T = os.path.join(directory_T, "temperature.py").replace("\\", "/")
process_T = None

#Light intensity subprocess
file_location_LI = os.path.realpath(__file__)
directory_LI = os.path.dirname(file_location_LI)
file_path_LI = os.path.join(directory_LI, "light_intensity.py").replace("\\", "/")
process_LI = None

def potentiometer_reading():
    Potentiometer = adc.get_adc_value(1)
    print("Potentiometer: " + str(Potentiometer))
    return Potentiometer

def temperature_humidity_reading():
    Temperature, Humidity = temp_humid_sensor.read_temp_humidity()
    print("Temperature : " + str(Temperature))
    print("Humidity : " + str(Humidity))
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

    global process_MS
    if process_MS is None:
        process_MS = subprocess.Popen(["python", file_path_MS])

    global process_T
    if process_T is None:
        process_T = subprocess.Popen(["python", file_path_T])

    global process_LI
    if process_LI is None:
        process_LI = subprocess.Popen(["python", file_path_LI])

    while True:
        Potentiometer = potentiometer_reading()
        Temperature, Humidity = temperature_humidity_reading()
        LDR = ldr_reading()
        Moisture_sensor = moisture_reading()
        if Temperature != -100:
            DataGeneration.DataGeneration(Temperature, Humidity, Moisture_sensor, Potentiometer, LDR)
        print(" ")
        time.sleep(5)

def stopthread():
    global process_MS
    if process_MS is not None:
        process_MS.terminate()
        process_MS = None

    global process_T
    if process_T is not None:
        process_T.terminate()
        process_T = None

    global process_LI
    if process_LI is not None:
        process_LI.terminate()
        process_LI = None


if __name__ == '__main__':
    main()