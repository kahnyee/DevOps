import light_intensity
from hal import hal_led as led

def test_optimal_light():
    led.init()
    LED = 1
    LDR = 100
    result = light_intensity.optimal_light(LDR)
    assert (LED == result)

    LED = 0
    LDR = 800
    result2 = light_intensity.optimal_light(LDR)
    assert (LED == result2)