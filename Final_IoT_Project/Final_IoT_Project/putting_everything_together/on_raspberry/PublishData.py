#####################################################
##   First class that have to PUBLISH data about   ##
##   TEMPERATURE and HUMIDITY and No.People in room##
##   to be placed on RASPERRYPI                    ##
#####################################################

from ReadingDHT import ReadingDHT
import paho.mqtt.client as mqttc
import time
import datetime
import requests
import json
from BluetoothCounter import BluetoothCounter

class PublishData(object):

    def __init__(self, sensor_t_h,bCounter, client):
        self.url = 'http://192.168.1.65:8080/'
        self.sensor_t_h = sensor_t_h
        self.client = client
        self.bCounter = bCounter

        try:
            respond = requests.get(self.url)
        except:
            print "PublishData: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER TOPICS"
        json_format = json.loads(respond.text)
        self.DHT_Topic = json_format["broker"]["DHT_Topic"]
        self.Counter_Topic = json_format["broker"]["Counter_Topic"]
        print "PublishData:: BROKER VARIABLES ARE READY"

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        # get the current time
        get_time = datetime.datetime.now()
        current_time = get_time.strftime("%Y-%m-%d %H:%M:%S")
        print ('CONNACK received with code: ' + str(rc))
        print ("at time: " + str(current_time))
        return str(rc)

    @classmethod
    def on_publish(cls, client, userdata, mid):
        # get the current time
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("mid: " + str(mid))
        print ("at time: " + str(current_time))
        return str(mid)

    def publish_sensor_data(self):
        #This function will publishe the data related to temperature and humidity
        try:
            json_format = self.sensor_t_h.reading_sensor()
            msg_info = client.publish(self.DHT_Topic, str(json_format), qos=1)
            if msg_info.is_published() == True:
                print ("\nMessage is published.")
            # This call will block until the message is published
            msg_info.wait_for_publish()
            return ("CIAONE", json_format)
        except:
            get_time = datetime.datetime.now()
            current_time = get_time.strftime("%Y-%m-%d %H:%M:%S")
            print "PublishData: ERROR IN PUBLISHING DATA RELATED TO THE SENSOR "
            print ("at time: " + str(current_time))

    def publish_people_counting(self):
        #this function will publish data related to the number of people in the room
        try:
            counter = self.bCounter.device_counter()
            json_format = json.dumps({'bluetooth counter': str(counter)})
            msg_info = client.publish(self.Counter_Topic, str(json_format), qos=1)
            if msg_info.is_published() == True:
                print ("\nMessage is published.")
            # This call will block until the message is published
            msg_info.wait_for_publish()
            return ("CIAONE", json_format)
        except:
            get_time = datetime.datetime.now()
            current_time = get_time.strftime("%Y-%m-%d %H:%M:%S")
            print "PublishData: ERROR IN PUBLISHING BLUETOOTH COUNTER"
            print ("at time: " + str(current_time))

if __name__ == '__main__':

    url = 'http://192.168.1.65:8080/'
    try:
        sensor_data = ReadingDHT()
        bCounter = BluetoothCounter()
    except:
        print "PublishData: ERROR IN GETTING DATA FROM SENSOR "
    client = mqttc.Client()
    sens = PublishData(sensor_data, bCounter, client)

    while True:
        try:
            respond = requests.get(url)
        except:
            print "PublishData: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER IP"

        json_format = json.loads(respond.text)
        ip = json_format["broker"]["Broker_IP"]
        port = json_format["broker"]["Broker_port"]
        try:
            client.on_connect = PublishData.on_connect
            client.on_publish = PublishData.on_publish
            client.connect(ip, int(port))
            client.loop_start()
        except:
            print "PublishData: ERROR IN CONNECTING TO THE BROKER"

        while True:
            sens.publish_sensor_data()
            sens.publish_people_counting()
            time.sleep(15)