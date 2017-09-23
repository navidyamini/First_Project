#!/usr/bin/python
from time import sleep # import the time function from the sleep # library
import RPi.GPIO as GPIO # import our GPIO library
GPIO.setmode(GPIO.BCM) # set the board numbering system to BCM
# setup our output pins GPIO.setup(17,GPIO.OUT) GPIO.setup(27,GPIO.OUT)
# Turn LEDs on

GPIO.setup(17,GPIO.OUT)
print "lights on" 
GPIO.output(17,GPIO.HIGH) 
GPIO.output(17,GPIO.HIGH) 
sleep(1) # sleep for 1 second
    
# Turn LEDs off
print "lights off" 
GPIO.output(17,GPIO.LOW) 
GPIO.output(17,GPIO.LOW) 
sleep(1)
# Turn LEDs on
print "lights on" 
GPIO.output(17,GPIO.HIGH) 
GPIO.output(17,GPIO.HIGH) 
sleep(1)
# Turn LEDs off
print "lights off"
GPIO.output(17,GPIO.LOW)
GPIO.output(17,GPIO.LOW)
GPIO.cleanup() # the clean-up function will reset all the configurations made in this script. This will stop the warnings # we got from the tutorial 2.