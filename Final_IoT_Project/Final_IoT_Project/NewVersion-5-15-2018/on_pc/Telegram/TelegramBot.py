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
        print "TelegramBot: RESTFUL ARE READY"

    def handler(self, msg):

        chat_id = msg['chat']['id']
        command = msg['text']
        self.setWebServiceVariables()
        bot.sendMessage(chat_id, self.sendResult(command))

    def sendResult(self,command):
        print'trying to send back the result'
        try:
            result = requests.get("http://"+self.restURL+ ":" + self.port+ "/"+command+"/all").content
            time.sleep(5)
            jsonformat = json.loads(result)
            temp=jsonformat['temperature']['value']
            hum=jsonformat['humidity']['value']
            staus=jsonformat['AcStatus']['value']
            count=jsonformat['bluetoothCounter']['value']
            outputString = 'Temperature: '+ str(temp) + "\n" + 'Humidity: ' + str(hum) +"\n"+"AcStatus: "+staus+"\n"+"Number of people: "+str(count)

        except:
                return "Please enter the correct room id\nex: room_1"

        return str(outputString)



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