__author__ = 'mhurtado'

#! /usr/bin/env python

#import the modules used in the script

import random, time
import RPi.GPIO as GPIO

# Assign the hardware PWM pin and name it
led = 18

# Configure the GPIO to BCM and set it to output mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

# Set PWM and create some constants we will be using
pwm = GPIO.PWM(led, 100)
RUNNING = True
WIND = 9

def brightness():
    """Funtion to randomly set the brightness of
    the LED between 5 per cent and 100 per cent power"""
    return random.randint(5, 100)

def flicker():
    """Function to randomly set the regularity of
    the flicker effect"""
    return random.random() / WIND

print "Candle light. Press CTRL + C to quit"

# The main program loop follows.
# Use try, except and finally to ensure the program
# quits cleanly when CTRL+C is pressed to stop it.

try:
    while RUNNING:
        # Start PWM with the LED off
        pwm.start(0)
        # Randomly change the brightness of the LED
        pwm.ChangeDutyCycle(brightness())
        # Randomly pause on brightness to simulate flickering
        time.sleep(flicker())

# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
    running = False
    print "\nQuitting Candle Light"

# Actions under finally will Always be called, regardless of
# what stopped the program (be it an error or and interrupt)
finally:
    # Stop and clean up to finish cleanly so the pins
    # are available to be used again
    pwm.stop()
    GPIO.cleanup()