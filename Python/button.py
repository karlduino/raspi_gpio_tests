#!/usr/bin/env python
#
# button.py: button + 3 LEDs on raspberry pi
#
# 3.3V ---- Button ---- pin 25 --\/\/\/\/-- GND
# (pin connected to one side of button and also,
#  through a 10k resistor, to ground)
#
# ===> If you skip the resistor, you'll reset
#      (or maybe kill) the RaspPi when you 
#      press the button

import wiringpi2 as wiringpi

# set up wiringPi with GPIO numbering of pins
wiringpi.wiringPiSetupGpio()

pins = [18, 23, 24]
button = 25

# setup pins for output
for pin in pins:
  wiringpi.pinMode(pin, 1) #  1 = output
wiringpi.pinMode(button, 0) # 0 = input

# turn LEDs off
for pin in pins:
  wiringpi.digitalWrite(pin, 0)

# turn LEDs off at exit
import atexit
def exit_handler():
  for pin in pins:
    wiringpi.digitalWrite(pin, 0)
atexit.register(exit_handler)

# turn LEDs on when button is pressed
while(1):
  value = wiringpi.digitalRead(button)
  for pin in pins:
    wiringpi.digitalWrite(pin, value)
