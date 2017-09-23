#!/usr/bin/python
import sys
import cherrypy
import json
import requests
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)

def MyFirstSensor():

   #Parse command line parameters.
   sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }

   print "ciao"
   sensor = Adafruit_DHT.DHT11 
   pin=4

   humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
   print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
   print temperature, humidity
   return temperature, humidity
   

#   if humidity is not None and temperature is not None:
#      print "ciao"
#      print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
#      return humidity, temperature
#   else:
#      return -1, -1
