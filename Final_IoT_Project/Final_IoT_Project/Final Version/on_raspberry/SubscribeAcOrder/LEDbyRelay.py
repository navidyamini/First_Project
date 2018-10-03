import RPi.GPIO as GPIO
import time
from PublishAcStatus import PublishAcStatus

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)


class LEDbyRelay(object):
    # "turnnig on and off the LED"""

    def __init__(self, url, roomId):
        self.relayPin = 17
        # create an object from PublishAcStatus class
        self.publish = PublishAcStatus(url, roomId)

    # setup function for some setup---custom function

    def setup(self):
        try:
            GPIO.setwarnings(False)
            # set the gpio modes to BCM numbering
            GPIO.setmode(GPIO.BCM)
            # set RelayPin's mode to output,and initial level to LOW(0V)
            GPIO.setup(self.relayPin, GPIO.OUT, initial=GPIO.HIGH)
        except:
            print "LEDbyRelay: ERROR IN SETUP THE LED"

    # Turn on
    def connect(self):
        try:
            self.publish.load()
            self.publish.stop()
        except:
            print("problem in publishing the A.C status")

        GPIO.output(self.relayPin, GPIO.LOW)
        self.publish.publish_data("It is ON")
        self.publish.start()
        return

    # Turn off
    def disconnect(self):
        self.publish.load()
        self.publish.stop()
        GPIO.output(self.relayPin, GPIO.HIGH)
        self.publish.publish_data("It is OFF")
        self.publish.start()
        return

    # define a destroy function for clean up everything after the script finished
    def destroy(self):
        # turn off relay
        GPIO.output(self.relayPin, GPIO.HIGH)
        # release resource
        GPIO.cleanup()
        return


if __name__ == '__main__':
# this main part is for testing, this class will be used in the SubscribeAcOrder
    pinNo = 17
    try:
        controling_LED = LEDbyRelay(pinNo)
        controling_LED.setup()
        while True:
            print ('*****...Relay close*****\n')

            # disconnect
            controling_LED.disconnect()
            time.sleep(20)
            print ('*****Relay open...*****\n')
            # connect
            controling_LED.connect()
            time.sleep(20)
    except KeyboardInterrupt:
        controling_LED.destroy()


