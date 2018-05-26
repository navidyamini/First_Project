import RPi.GPIO as GPIO
import time
from PublishAcStatus import PublishAcStatus

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

class LEDbyRelay(object):
    #"turnnig on and off the LED"""

    def __init__(self,url):
        self.relayPin = 17
        self.publish = PublishAcStatus(url)
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
        try:
            self.publish.load()
            self.publish.stop()
        except:
            print("this is the problem")
        #self.thingSpeak.setThingSpeakVariables()
        #publish = PublishAcStatus()
        GPIO.output(self.relayPin,GPIO.LOW)
        self.publish.publish_data("It is ON")
        self.publish.start()
        return

    #Turn off
    def disconnect(self):
        self.publish.load()
        self.publish.stop()
        #publish = PublishAcStatus()
        #self.thingSpeak.setThingSpeakVariables()
        GPIO.output(self.relayPin,GPIO.HIGH)
        self.publish.publish_data("It is OFF")
        self.publish.start()
        return

    #define a destroy function for clean up everything after the script finished
    def destroy(self):
        #turn off relay
        GPIO.output(self.relayPin,GPIO.HIGH)
        #release resource
        GPIO.cleanup()
        return

if __name__ == '__main__':
    
    pinNo = 17
    try:
        controling_LED = LEDbyRelay(pinNo)
        controling_LED.setup()
        while True:
            print ('*****...Relay close*****\n')

            #disconnect
            controling_LED.disconnect()
            time.sleep(20)
            print ('*****Relay open...*****\n')
            #connect
            controling_LED.connect()
            time.sleep(20)
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        controling_LED.destroy()
        
        
