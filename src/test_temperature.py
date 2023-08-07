import temperature
from hal import hal_dc_motor as dc_motor

def test_optimal_temp():
    dc_motor.init()
    speed = 50
    Temperature = 30
    result = temperature.optimal_temp(Temperature)
    assert (speed == result)

    speed = 0
    Temperature = 19
    result2 = temperature.optimal_temp(Temperature)
    assert (speed == result2)