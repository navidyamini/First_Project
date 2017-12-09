import json
import time
import requests
import telepot
import urllib2

class telegramBot(object):
    def __init__(self):
        self.url = 'http://192.168.1.65:8080/'
        bot = telepot.Bot('371024597:AAGK5je2cAXhyf4oMMD5wcUj1SguoZC5ZOY')

    def setThingSpeakVariables(self):
        try:
            respond = requests.get(self.url)
        except:
            print "TelegramBot: ERROR IN CONNECTING TO THE SERVER FOR READING THINGSPEAKCONNECTIONINFO.JSON"
        json_format = json.loads(respond.text)
        self.channelID = json_format["thingspeak"]["channelID"]
        self.READ_API_KEY = json_format["thingspeak"]["READ_API_KEY"]
        print "TelegramBot:: THINGSPEAK VARIABLES ARE READY"

    def handler(self, msg):

        chat_id = msg['chat']['id']
        command = msg['text']
        self.setThingSpeakVariables()

        if command == '/turnon':
            bot.sendMessage(chat_id, self.turn_on())

        elif command == '/turnoff':
            bot.sendMessage(chat_id, self.turn_off())

        elif command == '/gettemp':
            bot.sendMessage(chat_id, self.get_temp())

        elif command == '/gethum':
            bot.sendMessage(chat_id, self.get_hum())

        elif command == '/getpeopleno':
            bot.sendMessage(chat_id, self.getpeopleno())
        else:
            bot.sendMessage(chat_id, "Invalid Command")

    def turn_on(self):
        print'trying to turn it on'
        # self.led.setup()
        self.led.connect()
        return "on"

    def turn_off(self):
        print'trying to turn it off'
        self.led.disconnect()
        return "off"

    def get_temp(self):
        print'trying to send back temperature'
        try:
            TS = urllib2.urlopen(
            "http://api.thingspeak.com/channels/%s/fields/field1/last.json?api_key=%s" % (self.channelID, self.READ_API_KEY))
            response = TS.read()
            data = json.loads(response)
            temperature = data['field1']
            time.sleep(5)
            TS.close()
        except:
            print "ERROR IN READING TEMPERATURE FROM THINGSPEAK"
        return 'Temperature is: {0:0.1f} C'.format(float(temperature))

    def get_hum(self):
        print'trying to send back humidity'
        try:
            TS = urllib2.urlopen(
            "http://api.thingspeak.com/channels/%s/fields/field2/last.json?api_key=%s" % (self.channelID, self.READ_API_KEY))
            response = TS.read()
            data = json.loads(response)
            #print data
            humidity = data['field2']
            time.sleep(5)
            TS.close()
        except:
                print "ERROR IN READING HUMIDITY FROM THINGSPEAK"
        return 'Humidity is: {0:0.1f} %'.format(float(humidity))

    def getpeopleno(self):
        print'trying to send back number of people'
        try:
            TS = urllib2.urlopen(
                "http://api.thingspeak.com/channels/%s/fields/field3/last.json?api_key=%s" % (self.channelID, self.READ_API_KEY))
            response = TS.read()
            data = json.loads(response)
            number_of_people = data['field3']
            time.sleep(5)
            TS.close()
        except:
                print "ERROR IN READING NUMBER OF PEOPLE FROM THINGSPEAK"
        return 'no.people in the museum : '+ number_of_people

if __name__ == '__main__':

    respond = requests.get("http://192.168.1.65:8080/")
    json_format = json.loads(respond.text)
    port = json_format["telegram"]["Port"]
    telegram_bot = telegramBot()
    try:
        def handle(msg):
            # print msg
            telegram_bot.handler(msg)
        bot = telepot.Bot(port)
        bot.message_loop(handle)
        print 'I am listening...'
    except:
        print "TelegramBot: ERROR IN CONNECTING TO THE TELEGRAM BOT"
    while 1:
        time.sleep(10)