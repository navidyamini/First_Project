import sys
import time
import random
import datetime
import telepot


def on(pin):
        print'trying to turn on'
        return "on"
def off(pin):
        print'trying to turn off'
        return "off"

def handle(msg):

    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Got command: %s' % command

    if command == '/turnon':
       bot.sendMessage(chat_id, on(17))
      
    elif command =='/turnoff':
       bot.sendMessage(chat_id, off(17))
 
bot = telepot.Bot('371024597:AAGK5je2cAXhyf4oMMD5wcUj1SguoZC5ZOY')
bot.message_loop(handle)
print 'I am listening...'

while 1:
     time.sleep(10)