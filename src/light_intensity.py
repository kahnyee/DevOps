from hal import hal_adc as adc
from hal import hal_led as led

lock = 0
lock2 = 0

def optimal_light(LDR):
    global lock
    global lock2

    if LDR <= 200:
        if lock == 0:
            led.set_output(1, 1)
            lock += 1
            lock2 = 0
            LED = 1
        elif lock == 1:
            LED = 1
            lock2 = 0

    if LDR > 200:
        if lock2 == 0:
            led.set_output(1, 0)
            lock2 += 1
            lock = 0
            LED = 0
        elif lock2 == 1:
            LED = 0
            lock = 0
    return LED

def main():
    adc.init()
    led.init()
    while True:
        optimal_light(adc.get_adc_value(0))

if __name__ == '__main__':
    main()