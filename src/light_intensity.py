from hal import hal_adc as adc
from hal import hal_led as led
def optimal_light(LDR):
    if LDR <= 200:
        led.set_output(1, 1)
        LED = 1
    else:
        led.set_output(1, 0)
        LED = 0
    return LED
def main():
    adc.init()
    led.init()
    while True:
        optimal_light(adc.get_adc_value(0))

if __name__ == '__main__':
    main()