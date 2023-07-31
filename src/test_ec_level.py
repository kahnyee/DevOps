import ec_level
from hal import hal_servo as servo

def test_optimal_ec():
    servo.init()
    position = 0
    Moisture_sensor = True
    result = ec_level.optimal_ec(Moisture_sensor)
    assert (position == result)

    position = 45
    Moisture_sensor = False
    result2 = ec_level.optimal_ec(Moisture_sensor)
    assert (position == result2)