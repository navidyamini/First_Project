import RPi.GPIO as GPIO
import time
from ThingSpeak import ThingSpeak
from PublishAcStatus import PublishAcStatus

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

class LEDbyRelay(object):
    #"turnnig on and off the LED"""

    def __init__(self,relayPin):

        self.relayPin = relayPin
        self.thingSpeak = ThingSpeak()
        #self.publish = PublishAcStatus()
    #setup function for some setup---custom function
    def setup(self):
        try:
            GPIO.setwarnings(False)
            #set the gpio modes to BCM numbering
            GPIO.setmode(GPIO.BCM)
            #set RelayPin's mode to output,and initial level to LOW(0V)
            GPIO.setup(self.relayPin,GPIO.OUT,initial=GPIO.HIGH)
        except:
            print "LEDbyRelay: ERROR IN SETUP THE LED"
    #Turn on
    def connect(self):
        #self.thingSpeak.setThingSpeakVariables()
        publish = PublishAcStatus()
        GPIO.output(self.relayPin,GPIO.LOW)
        self.thingSpeak.ac_status(1)
        publish.publish_data("Turn_on")
        return

    #Turn off
    def disconnect(self):
        publish = PublishAcStatus()
        #self.thingSpeak.setThingSpeakVariables()
        GPIO.output(self.relayPin,GPIO.HIGH)
        self.thingSpeak.ac_status(0)
        publish.publish_data("Turn_off")
        return

    #define a destroy function for clean up everything after the script finished
    def destroy(self):
        #turn off relay
        GPIO.output(self.relayPin,GPIO.HIGH)
        #release resource
        GPIO.cleanup()

if __name__ == '__main__':
    
    pinNo = 17
    try:
        controling_LED = LEDbyRelay(pinNo)
        controling_LED.setup()
        while True:
            print ('|******************|')
            print ('|  ...Relay close  |')
            print ('|******************|\n')
        
            #disconnect
            controling_LED.disconnect()
            time.sleep(20)
            print ('|*****************|')
            print ('|  Relay open...  |')
            print ('|*****************|\n')
            print ('')
            #connect
            controling_LED.connect()
            time.sleep(20)
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        controling_LED.destroy()
        
        
