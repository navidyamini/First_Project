import Adafruit_DHT
import json
import datetime


class ReadingDHT(object):
    """reading temperature and humidity"""

    def __init__(self):

        self.humidity = 0
        self.temperature = 0

    def reading_sensor(self):

        try:
            self.humidity, self.temperature = Adafruit_DHT.read_retry(11, 4)
        except:
            print "ReadingDHT: ERROR IN READING THE SENSOR"
        if (self.humidity is not None and self.temperature is not None):
            print "From Sensor:"
            print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(self.temperature, self.humidity)
            get_time = datetime.datetime.now()
            current_time = get_time.strftime("%Y-%m-%d %H:%M:%S")
            json_format = json.dumps({"temperature": self.temperature, "humidity": self.humidity,"time":current_time})
            # print json_format
            return json_format
        else:
            print 'ReadingDHT: ERROR IN SENDING JSON'
        return
'''
if __name__ == '__main__':

    data_of_DHT = ReadingDHT()
    while True:
        data_of_DHT.reading_sensor()
'''