import json
from Final_IoT_Project.Final_IoT_Project.Control.publish_order_AC import publish_order_AC
import requests

class CheckingThreshold(object):
    def __init__(self):
        self.url = 'http://192.168.1.65:8080/'
        self.temperature = 0.00
        self.humidity = 0.00
        self.max_temperature = 0.00
        self.max_humidity = 0.00
        self.min_temperature = 0.00
        self.min_humidity = 0.00
        self.send_order = publish_order_AC()

    def sensor_data(self,data):
        try:
            json_format = json.loads(data)
            self.humidity = json_format["humidity"]
            self.temperature = json_format["temperature"]
        except:
            print "CheckingThreshold: ERROR IN READING HUMIDITY AND TEMPERATUR"

    def load_file(self):
        try:
            respond = requests.get(self.url+"ThresholdReader.py")
        except:
            print "CheckingThreshold: ERROR IN CONNECTING TO THE SERVER FOR READING initial_data.JSON"
        try:
            json_format = json.loads(respond.text)
            print json_format
            self.max_temperature = json_format["thresholds"]["max_temp"]
            self.max_humidity = json_format["thresholds"]["max_hum"]
            self.min_temperature = json_format["thresholds"]["min_temp"]
            self.min_humidity = json_format["thresholds"]["min_hum"]

        except :
            print "CheckingThreshold: ERROR IN READING THE JSON FILE VALUES"
        return

    def checking(self):

        if self.temperature > self.max_temperature or self.temperature < self.min_temperature or self.humidity > self.max_humidity or self.humidity < self.min_humidity:
            order = "Turn_on"
            print order
            self.send_order.publish_data(order)
        else:
            order = "Turn_off"
            print order
            self.send_order.publish_data(order)

if __name__ == '__main__':

    treshhold = CheckingThreshold()
    treshhold.load_file()