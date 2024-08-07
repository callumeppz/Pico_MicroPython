from machine import Pin
import utime

# Initialise the PIR sensor pin
pir = Pin(16, Pin.IN, Pin.PULL_UP)

# Initialise the LED pins, this line initiates all usable pins on the breadboard using Pin.OUT
led_pins = [Pin(28, Pin.OUT), Pin(26, Pin.OUT), Pin(20, Pin.OUT), Pin(9, Pin.OUT), Pin(6, Pin.OUT), Pin(2, Pin.OUT)]

# Method to turn on all LEDs
def turn_on_leds():
    for led in led_pins: # FOR loop to loop through all pins
        led.high() # turns pins on 

# Method to turn off all LEDs
def turn_off_leds():
    for led in led_pins:
        led.low()

# Initial state: turn off all LEDs
turn_off_leds() 

while True:
    pir_value = pir.value() #initiates pir value
    if pir_value == 1: # if pir value is 1 (motion detected) run the loop
        turn_on_leds()
        utime.sleep(90)  # Keep LEDs on for 90 seconds
        turn_off_leds()

