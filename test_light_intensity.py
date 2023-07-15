import light_intensity

def test_Turn_on_LED:
    # Turn on LED
    LDRReadings = 190
    result = light_intensity.optimal_light(LDRReadings)
    answer = 1
    assert (answer == result)

    # Turn off LED
    LDRReadings = 210
    result2 = light_intensity.optimal_light(LDRReadings)
    answer2 = 0
    assert (answer2 == result2)
