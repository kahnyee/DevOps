from hal import hal_temp_humidity_sensor as temp_humid_sensor
from hal import hal_dc_motor as dc_motor

lock = 0
lock2 = 0

def optimal_temp(Temperature):
    global lock
    global lock2

    if Temperature > 20:
        if lock == 0:
            dc_motor.set_motor_speed(50)
            lock += 1
            speed = 50
        else:
            speed = 50
            lock2 = 0

    if Temperature <= 20:
        if lock2 == 0:
            dc_motor.set_motor_speed(0)
            lock2 += 1
            speed = 0
        elif lock2 == 1:
            speed = 0
            lock = 0
    return speed
def main():
    temp_humid_sensor.init()
    dc_motor.init()
    while True:
        Temperature, Humidity = temp_humid_sensor.read_temp_humidity()
        if Temperature != -100:
            optimal_temp(Temperature)

if __name__ == '__main__':
    main()