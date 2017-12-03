import json
import time

import telepot

from Final_IoT_Project.Final_IoT_Project.putting_everything_together.on_raspberry.reading_DHT import Reading_DHT
from LEDbyRelay import LEDbyRelay


#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(17,GPIO.OUT)

class telegramBot(object):
    """by using this class we will handel the comminucation between our software and telegrambot"""

    def __init__(self):
        self.pinNo = 17
        bot = telepot.Bot('371024597:AAGK5je2cAXhyf4oMMD5wcUj1SguoZC5ZOY')
        self.dht = Reading_DHT()
        self.led = LEDbyRelay(self.pinNo)
    
    def handler(self,msg):

        chat_id = msg['chat']['id']
        command = msg['text']
        
        if command == '/turnon':
            bot.sendMessage(chat_id, self.turn_on())
      
        elif command =='/turnoff':
            bot.sendMessage(chat_id, self.turn_off())
        
        elif command =='/gettemp':
            bot.sendMessage(chat_id, self.get_temp())
        
        elif command =='/gethum':
            bot.sendMessage(chat_id, self.get_hum())
        
        elif command =='/getstat':
            bot.sendMessage(chat_id, self.get_stat())
        
        else:
            bot.sendMessage(chat_id, "Invalid Command")    
    
    def turn_on(self):
        print'trying to turn it on'
        #self.led.setup()
        self.led.connect()        
        return "on"
    
    def turn_off(self):
        print'trying to turn it off'
        self.led.disconnect()
        return "off"
    
    def get_temp(self):

        print'trying to send back temperature'

        json_format = self.dht.reading_sensor()
        THD_json = json.loads(json_format)
        temperature = THD_json["temperature"]

        return 'Temperature is: {0:0.1f} C'.format(temperature)
    
    def get_hum(self):

        print'trying to send back humidity'

        json_format = self.dht.reading_sensor()
        THD_json = json.loads(json_format)
        humidity= THD_json["humidity"]

        return 'Humidity is: {0:0.1f} %'.format(humidity)
    
    def get_stat(self):

        print'trying to rsend back stat'

        return "Under Construction"

if __name__ == '__main__':

    telegram_bot = telegramBot()
    
    def handle(msg):
    #print msg
        telegram_bot.handler(msg)
        
    bot = telepot.Bot('371024597:AAGK5je2cAXhyf4oMMD5wcUj1SguoZC5ZOY')
    bot.message_loop(handle)
    
    print 'I am listening...'

    while 1:
        time.sleep(10)