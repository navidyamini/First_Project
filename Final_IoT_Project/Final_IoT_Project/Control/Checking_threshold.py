import json
from publish_order_AC import publish_order_AC

class Checking_threshold(object):
    def __init__(self):

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
            print "Error in reading the sensor data in Checking_threshhold class"

    def load_file(self):
        try:
            file_address = '../RawWebpage/initial_data.json'
            json_file = open(file_address)
            values = json.load(json_file)
            json_file.close()
            print values
            self.max_temperature = values["thresholds"]["max_temp"]
            self.max_humidity = values["thresholds"]["max_hum"]
            self.min_temperature = values["thresholds"]["min_temp"]
            self.min_humidity = values["thresholds"]["min_hum"]

        except :
            print "ERROR: In reading file in Checking_threshhold class"
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

    treshhold = Checking_threshold()
    treshhold.load_file()