from hal import hal_moisture_sensor as moisture_sensor
from hal import hal_servo as servo
def optimal_ec(Moisture_sensor):
    if Moisture_sensor:
        servo.set_servo_position(45)
        position = 45
    else:
        servo.set_servo_position(0)
        position = 0
    return position
def main():
    moisture_sensor.init()
    servo.init()
    while True:
        optimal_ec(moisture_sensor.read_sensor())

if __name__ == '__main__':
    main()