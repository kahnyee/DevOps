import temperature

def test_optimal_temp():
    speed = 50
    Temperature = 21
    result = temperature.optimal_temp(Temperature)
    assert (speed == result)

    speed = 0
    Temperature = 19
    result2 = temperature.optimal_temp(Temperature)
    assert (speed == result2)