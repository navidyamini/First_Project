import json
import time
import requests
import telepot
import urllib2

class telegramBot(object):

    def __init__(self,url,port):
        self.url = url
        bot = telepot.Bot(port)

    def setWebServiceVariables(self):
        try:
            respond = requests.get(self.url+"/dataToRest")
        except:
            print "TelegramBot: ERROR IN CONNECTING TO THE SERVER FOR GETTING RESTFUL WEB SERVICE URL"
        json_format = json.loads(respond.text)
        self.restURL = json_format["Host_IP"]
        self.port = json_format["port"]
        print "TelegramBot:: RESTFUL ARE READY"

    def handler(self, msg):

        chat_id = msg['chat']['id']
        command = msg['text']
        self.setWebServiceVariables()

        bot.sendMessage(chat_id, self.sendResult(command))

        if command == '/acstatus':
            bot.sendMessage(chat_id, self.acstatus())

        elif command == '/visitors':
            bot.sendMessage(chat_id, self.getpeopleno())

        elif command == '/temp':
            bot.sendMessage(chat_id, self.get_temp())

        elif command == '/hum':
            bot.sendMessage(chat_id, self.get_hum())
        else:
            bot.sendMessage(chat_id, "Invalid Command")


    def sendResult(self,command):
        print'trying to send back the result'
        try:
            result = requests.get("http://"+self.restURL+ ":" + self.port+ "/"+command+"/all").content
            time.sleep(5)
        except:
                print "ERROR IN GETTING RESULTS"

        return str(result)


    def acstatus(self):
        print'trying to send back the A/C status'
        try:
            result = requests.get("http://"+self.restURL+ ":" + self.port+ "/ac").content
            time.sleep(5)
        except:
                print "ERROR IN READING THE A/S STATUS FROM THINGSPEAK"
        return 'A/C status : '+ str(result)


    def get_temp(self):
        print'trying to send back temperature'
        try:
            result = requests.get("http://"+self.restURL + ":" + self.port + "/temp").content
            time.sleep(5)

        except:
            print "ERROR IN READING TEMPERATURE FROM THINGSPEAK"
        return 'Temperature is: {0:0.1f} C'.format(float(result))

    def get_hum(self):
        print'trying to send back humidity'

        try:
            result = requests.get("http://"+self.restURL + ":" + self.port + "/hum").content
            time.sleep(5)
        except:
                print "ERROR IN READING HUMIDITY FROM THINGSPEAK"
        return 'Humidity is: {0:0.1f} %'.format(float(result))

    def getpeopleno(self):
        print'trying to send back number of people'
        try:
            result = requests.get("http://"+self.restURL + ":" + self.port + "/noPeople").content
            time.sleep(5)
        except:
                print "ERROR IN READING NUMBER OF PEOPLE FROM THINGSPEAK"
        return 'number of people in the museum : '+ result

if __name__ == '__main__':

    try:
        file = open("config_file.json", "r")
        json_string = file.read()
        file.close()
    except:
        raise KeyError("***** DataWithRest: ERROR IN READING CONFIG FILE *****")

    config_json = json.loads(json_string)
    url = config_json["reSourceCatalog"]["url"]

    try:
        respond = requests.get(url+"/telegram")
        json_format = json.loads(respond.text)
        port = json_format["Port"]
        telegram_bot = telegramBot(url,port)
    except:
        print "ERROR IN CONNECTING TO SERVER FOR GETTING TELEGROM BOT PORT"
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