import ec_level

def test_optimal_ec():
    position = 0
    Moisture_sensor = True
    result = ec_level.optimal_ec(Moisture_sensor)
    assert (position == result)

    position = 45
    Moisture_sensor = False
    result = ec_level.optimal_ec(Moisture_sensor)
    assert (position == result)