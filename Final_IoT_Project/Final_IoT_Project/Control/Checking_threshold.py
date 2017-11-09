import json

class Checking_threshold(object):
    def __init__(self):
        self.max_temperature = 0.00
        self.max_humidity = 0.00
        self.min_temperature = 0.00
        self.min_humidity = 0.00

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
            print "ERROR: In reading file"
            return

    def checking(self,temperature,humidity):
        if temperature > self.max_temperature or temperature < self.min_temperature or humidity > self.max_humidity or humidity < self.min_humidity:
            return "Turn_on"
        return "Turn_off"

if __name__ == '__main__':

    treshhold = Checking_threshold()
    treshhold.load_file()