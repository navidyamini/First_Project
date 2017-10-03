import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

class LEDbyRelay(object):
    "turnnig on and off the LED"""

    def __init__(self,relayPin):

        self.relayPin = relayPin
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setwarnings(False)
        #GPIO.setup(17,GPIO.OUT)

    #setup function for some setup---custom function
    def setup(self):

        GPIO.setwarnings(False)
        #set the gpio modes to BCM numbering
        GPIO.setmode(GPIO.BCM)
        #set RelayPin's mode to output,and initial level to LOW(0V)
        GPIO.setup(self.relayPin,GPIO.OUT,initial=GPIO.LOW)

    #Turn on
    def connect(self):
        GPIO.output(self.relayPin,GPIO.LOW)

    #Turn off
    def disconnect(self):
        GPIO.output(self.relayPin,GPIO.HIGH)

    #define a destroy function for clean up everything after the script finished
    def destroy(self):
        #turn off relay
        GPIO.output(self.relayPin,GPIO.LOW)
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
            time.sleep(1)   
            print ('|*****************|')
            print ('|  Relay open...  |')
            print ('|*****************|\n')
            print ('')
            #connect
            controling_LED.connect()
            time.sleep(1)
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        controling_LED.destroy()
        
        
