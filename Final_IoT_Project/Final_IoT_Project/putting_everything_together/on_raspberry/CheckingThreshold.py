import json
from LEDbyRelay import LEDbyRelay
import requests
import time
from ReadingDHT import ReadingDHT


class CheckingThreshold(object):

    def __init__(self):
        self.url = 'http://192.168.1.65:8080/'
        self.flag = 0
        self.temperature = 0.00
        self.humidity = 0.00
        self.max_temperature = 0.00
        self.max_humidity = 0.00
        self.min_temperature = 0.00
        self.min_humidity = 0.00
        self.controling_LED = LEDbyRelay(17)
        self.dht = ReadingDHT()

    def sensor_data(self):
        try:
            json_format = self.dht.reading_sensor()
            THD_json = json.loads(json_format)
            self.humidity = THD_json["humidity"]
            self.temperature = THD_json["temperature"]
        except:
            print "CheckingThreshold: ERROR IN READING HUMIDITY AND TEMPERATUR"

    def load_file(self):
        try:
            respond = requests.get(self.url)
            json_format = json.loads(respond.text)
            #print json_format
            self.max_temperature = json_format["thresholds"]["max_temp"]
            self.max_humidity = json_format["thresholds"]["max_hum"]
            self.min_temperature = json_format["thresholds"]["min_temp"]
            self.min_humidity = json_format["thresholds"]["min_hum"]

        except :
            print "CheckingThreshold: ERROR IN CONNECTING TO THE SERVER FOR READING initial_data.JSON"
        return

    def checking(self):

        if self.temperature > self.max_temperature or self.temperature < self.min_temperature or self.humidity > self.max_humidity or self.humidity < self.min_humidity:
            order = "Turn_on"
            print order,self.flag

            if(self.flag == 0):
                try:
                    self.controling_LED.setup()
                    self.controling_LED.connect()
                    self.flag = 1
                except:
                    print "CheckingThreshold: ERROR IN SENDING TURN ON ORDER"
        else:
            order = "Turn_off"
            print order,self.flag

            if(self.flag == 1):
                try:
                    self.controling_LED.setup()
                    self.controling_LED.disconnect()
                    self.flag = 0
                except:
                    print "CheckingThreshold: ERROR IN SENDING TURN OFF ORDER"

if __name__ == '__main__':

    treshhold = CheckingThreshold()

    while True:
        treshhold.sensor_data()
        treshhold.load_file()
        treshhold.checking()
        time.sleep(60)