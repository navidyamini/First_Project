import os
import sys
from reading_DHT import Reading_DHT 
import paho.mqtt.publish as publish
import json

class thingspeak(object):
    """by using this class we will try to send data to thinkspeak"""

    def __init__(self):
    
        #channel variables
        self.THINGSPEAK_HOST = 'mqtt.thingspeak.com'
        self.ACCESS_TOKEN = 'DDNTX8BUX8A17YZG'
        self.channelID = "240810"
        self.tTransport = "websockets"
        self.tPort = 80
        self.mqttHost = "mqtt.thingspeak.com"
        self.dht = Reading_DHT()
        #Data
        #self.humidity = 0
        #self.temperature = 0

    def sending_data(self):
        #dht = Reading_DHT()
        #client = mqtt.Client()
        json_format = self.dht.reading_sensor()
        THD_json = json.loads(json_format)

        temperature = THD_json["temperature"]
        humidity= THD_json["humidity"]

        # Create the topic string  
        topic = "channels/" + self.channelID + "/publish/" + self.ACCESS_TOKEN
        
        print "From thingspeak"
        print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)

        # build the payload string
        payload = "field1=" + str(temperature) + "&field2=" + str(humidity)
        
        # attempt to publish this data to the topic
        try:
            publish.single(topic, payload, hostname = self.mqttHost, transport = self.tTransport, port = self.tPort)
        except:
            print("There was an error while publishing the data.")
        return

if __name__ == '__main__':

    data_of_DHT = thingspeak()
    while True:
        data_of_DHT.sending_data()
    




