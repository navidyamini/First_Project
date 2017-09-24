import RPi.GPIO as GPIO
import time
# set BCM_GPIO 17 as relay pin
RelayPin = 17
#print message at the begining ---custom function
def print_message():
    print ('|**********************************************|')
    print ('|                     Relay                    |')
    print ('|        -----------------------------------   |')
    print ('|        GPIO0 connect to relay control pin    |')
    print ('|        led connect to relay NormalOpen pin   |')
    print ('|        5V connect to relay COM pin           |')
    print ('|        Make relay to control a led           |')
    print ('|        -----------------------------------   |')
    print ('|                                              |')
    print ('|                                        OSOYOO|')
    print ('|**********************************************|\n')
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')
    print ('\n')
#setup function for some setup---custom function
def setup():
    GPIO.setwarnings(False)
    #set the gpio modes to BCM numbering
    GPIO.setmode(GPIO.BCM)
    #set RelayPin's mode to output,and initial level to LOW(0V)
    GPIO.setup(RelayPin,GPIO.OUT,initial=GPIO.LOW)
#main function
def main():
    #print info
    print_message()
    while True:
        print ('|******************|')
        print ('|  ...Relay close  |')
        print ('|******************|\n')
        
        #disconnect
        GPIO.output(RelayPin,GPIO.LOW)
        time.sleep(1)
        print ('|*****************|')
        print ('|  Relay open...  |')
        print ('|*****************|\n')
        print ('')
        #connect
        GPIO.output(RelayPin,GPIO.HIGH)
        time.sleep(1)
#define a destroy function for clean up everything after the script finished
def destroy():
    #turn off relay
    GPIO.output(RelayPin,GPIO.LOW)
    #release resource
    GPIO.cleanup()
#
# if run this script directly ,do:
if __name__ == '__main__':
    setup()
    try:
            main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        destroy()