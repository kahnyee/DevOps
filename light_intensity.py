import time
from hal import hal_adc as adc
from hal import hal_led as led
def optimal_light():
    LDRReadings = adc.get_adc_value(0)
    if LDRReadings < 200:
        led.set_output(1, 1)
    else:
        led.set_output(1, 0)
def main():
    adc.init()
    led.init()
    while True:
        optimal_light()

if __name__ == '__main__':
    main()