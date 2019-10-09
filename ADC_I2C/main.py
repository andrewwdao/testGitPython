from adc import adc_button,adc_switches
import time
button = adc_button()

while True:
    print(button.read())
    time.sleep(0.5)