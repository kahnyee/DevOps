from hal import hal_moisture_sensor as moisture_sensor
from hal import hal_servo as servo

lock = 0
lock2 = 0

def optimal_ec(Moisture_sensor):
    global lock
    global lock2
    if Moisture_sensor:
        if lock == 0:
            lock2 = 0
            servo.set_servo_position(0)
            lock += 1
            position = 0
        elif lock == 1:
            position = 0
            lock2 = 0

    if not Moisture_sensor:
        if lock2 == 0:
            lock = 0
            servo.set_servo_position(45)
            lock2 += 1
            position = 45
        elif lock2 == 1:
            position = 45
            lock = 0
    return position

def main():
    moisture_sensor.init()
    servo.init()
    while True:
        optimal_ec(moisture_sensor.read_sensor())

if __name__ == '__main__':
    main()