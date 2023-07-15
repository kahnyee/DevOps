import temperature

def test_Turn_on_fan:
    # Turn on fan
    temperature = 21
    result = temperature.optimal_temp(temperature)
    answer = 50
    assert (answer == result)

    # Turn off fan
    temperature = 19
    result2 = temperature.optimal_temp(temperature)
    answer2 = 0
    assert (answer2 == result2)