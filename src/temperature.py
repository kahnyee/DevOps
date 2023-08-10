from hal import hal_temp_humidity_sensor as temp_humid_sensor
from hal import hal_dc_motor as dc_motor

lock = 0
lock2 = 0
temp = 0
def optimal_temp(Temperature):
    global lock
    global lock2

    if Temperature > 20:
        if lock == 0:
            dc_motor.set_motor_speed(50)
            lock += 1
            lock2 = 0
            speed = 50
        else:
            speed = 50
            lock2 = 0

    if Temperature <= 20:
        if lock2 == 0:
            dc_motor.set_motor_speed(0)
            lock2 += 1
            lock = 0
            speed = 0
        elif lock2 == 1:
            speed = 0
            lock = 0
    return speed

def temperature_data(temperature):
    global temp
    temp = temperature

def main():
    global temp
    temp_humid_sensor.init()
    dc_motor.init()
    while True:
        if temp != -100:
            optimal_temp(temp)
            print(temp)

if __name__ == '__main__':
    main()