#!/usr/bin/sudo python

import wiringpi2 as wiringpi
import random
import time
import sys

# set up wiringPi with GPIO numbering of pins
wiringpi.wiringPiSetupGpio()

pins = [18, 23, 24]
unused_pin = 17

random.seed()

# setup pins for output
for pin in pins:
  wiringpi.pinMode(pin, 1) # 1 = output

# light the pins randomly
num_cycles = int(sys.argv[1])*10 if len(sys.argv) > 1 else 100
for i in range(0, num_cycles):
  for pin in pins:
    wiringpi.digitalWrite(pin, random.randint(0,1))
  time.sleep(0.1)

# turn them all off
for pin in pins:
  wiringpi.digitalWrite(pin, 0)
