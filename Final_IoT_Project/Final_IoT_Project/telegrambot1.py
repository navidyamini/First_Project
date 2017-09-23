import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

#LED
def on(pin):
        print'trying to turn on'
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        print'trying to turn off'
        GPIO.output(pin,GPIO.LOW)
        return
# to use Raspberry Pi board pin numbers
#GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
#GPIO.setup(17, GPIO.OUT)

def handle(msg):
    #print msg
    chat_id = msg['chat']['id']
    command = msg['text']
    #print 'chat is: %s' %chat_id
    print 'Got command: %s' % command

    if command == '/turnon':
       bot.sendMessage(chat_id, on(17))
       #on(17)
    elif command =='/turnoff':
       bot.sendMessage(chat_id, off(17))
      
       


bot = telepot.Bot('371024597:AAGK5je2cAXhyf4oMMD5wcUj1SguoZC5ZOY')
bot.message_loop(handle)
print 'I am listening...'



while 1:
     time.sleep(10)