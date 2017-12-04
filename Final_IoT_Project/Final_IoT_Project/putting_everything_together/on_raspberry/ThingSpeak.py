from BluetoothCounter import BluetoothCounter
from ReadingDHT import ReadingDHT
import requests
import json
import paho.mqtt.publish as publish

class ThingSpeak(object):
    def __init__(self):
        self.url = 'http://192.168.1.65:8080/'
        self.dht = ReadingDHT()
        self.counter = BluetoothCounter()

    def setThingSpeakVariables(self):
        try:
            respond = requests.get(self.url+"ThingsSpeakInfoReader.py")
        except:
            print "ThingSpeak: ERROR IN CONNECTING TO THE SERVER FOR READING THINGSPEAKCONNECTIONINFO.JSON"
        json_format = json.loads(respond.text)
        self.THINGSPEAK_HOST = json_format["THINGSPEAK_HOST"]
        self.ACCESS_TOKEN = json_format["ACCESS_TOKEN"]
        self.channelID = json_format["channelID"]
        self.tTransport = json_format["tTransport"]
        self.tPort = int(json_format["tPort"])
        self.mqttHost =json_format["mqttHost"]
        print "ThingSpesk: THINGSPEAK VARIABLES ARE READY"

    def sending_dht_data(self):

        json_format = self.dht.reading_sensor()
        THD_json = json.loads(json_format)

        temperature = THD_json["temperature"]
        humidity= THD_json["humidity"]

        # Create the topic string
        self.topic = "channels/" + self.channelID + "/publish/" + self.ACCESS_TOKEN

        print "From thingspeak"
        print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)

        # build the payload string
        payload = "field1=" + str(temperature) + "&field2=" + str(humidity)

        # attempt to publish this data to the topic
        try:
            publish.single(self.topic, payload, hostname = self.mqttHost, transport = self.tTransport, port = self.tPort)
        except:
            print("ThingSpeak: ERROR IN PUBLISHING THE HUM AND TEMP TO THINGSPEAK")
        return

    def number_of_people(self):

        result = self.counter.device_counter()
        print result
        # build the payload string
        payload = "field3=" + str(result)
        # attempt to publish this data to the topic
        try:
            publish.single(self.topic, payload, hostname=self.mqttHost, transport=self.tTransport, port=self.tPort)
        except:
            print("ThingSpeak: ERROR IN PUBLISHING THE NUMBER OF PEOPLE TO THINGSPEAK.")
        return

if __name__ == '__main__':

    thingspeak = ThingSpeak()
    while True:
        thingspeak.setThingSpeakVariables()
        thingspeak.sending_dht_data()
        thingspeak.number_of_people()