import ec_level

def test_dispense_nutrients():
    # Wet
    answer = 0
    MoistReadings = True
    result = ec_level.optimal_ec(MoistReadings)
    assert (answer == result)

    # Dry
    answer2 = 45
    MoistReadings = False
    result2 = ec_level.optimal_ec(MoistReadings)
    assert (answer2 == result2)