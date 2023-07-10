import time
from hal import hal_moisture_sensor as moisture_sensor
from hal import hal_servo as servo
def optimal_ec():
    MoistReadings = moisture_sensor.read_sensor()
    if MoistReadings:
        servo.set_servo_position(45)
    else:
        servo.set_servo_position(0)
def main():
    moisture_sensor.init()
    servo.init()
    while True:
        optimal_ec()

if __name__ == '__main__':
    main()