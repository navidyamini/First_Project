#####################################################
##   First class that have to PUBLISH data about   ##
##   No.People in room                             ##
##   to be placed on RASPERRYPI                    ##
#####################################################

import paho.mqtt.client as mqttc
import time
import datetime
import requests
import json
from BluetoothCounter import BluetoothCounter

class PublishPeopleNo(object):

    def __init__(self, url,bCounter,roomId, client):
        self.url = url
        self.bCounter = bCounter
        self.client = client
        self.roomId=roomId

    def load_topics(self):
        try:
            self.respond = requests.get(self.url)
            json_format = json.loads(self.respond.text)
            self.Counter_Topic = json_format["broker"]["Counter_Topic"]
            print "PublishPeopleNo:: BROKER VARIABLES ARE READY"
        except:
            print "PublishPeopleNo: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER TOPICS"


    @staticmethod
    def on_connect(client, userdata, flags, rc):
        # get the current time
        get_time = datetime.datetime.now()
        current_time = get_time.strftime("%Y-%m-%d %H:%M:%S")
        print ('CONN ACK received with code: ' + str(rc))
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

    def publish_people_counting(self):
        #this function will publish data related to the number of people in the room
        try:
            counter = self.bCounter.device_counter()
            json_format = json.dumps({'roomId':self.roomId,'bluetooth counter': str(counter)})
            msg_info = client.publish(self.Counter_Topic, str(json_format), qos=1)
            if msg_info.is_published() == True:
                print ("\nMessage is published.")
            # This call will block until the message is published
            msg_info.wait_for_publish()
            return ("Hello", json_format)
        except:
            get_time = datetime.datetime.now()
            current_time = get_time.strftime("%Y-%m-%d %H:%M:%S")
            print "PublishData: ERROR IN PUBLISHING BLUETOOTH COUNTER"
            print ("at time: " + str(current_time))

if __name__ == '__main__':

    #url = 'http://192.168.1.65:8080/'

    try:
        file = open("config_file.json", "r")
        json_string = file.read()
        file.close()
    except:
        raise KeyError("***** PublishPeopleNo: ERROR IN READING CONFIG FILE *****")

    config_json = json.loads(json_string)
    ip = config_json["reSourceCatalog"]["url"]
    roomId = config_json["reSourceCatalog"]["roomId"]
    url = ip+roomId

    try:
        bCounter = BluetoothCounter()
    except:
        print "PublishPeopleNo: ERROR IN GETTING DATA FROM SENSOR "

    client = mqttc.Client()
    sens = PublishPeopleNo(url, bCounter,roomId, client)

    while True:
        sens.load_topics()
        try:
            respond = requests.get(url)
            json_format = json.loads(respond.text)
            ip = json_format["broker"]["Broker_IP"]
            port = json_format["broker"]["Broker_port"]
        except:
            print "PublishPeopleNo: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER IP"

        try:
            client.on_connect = PublishPeopleNo.on_connect
            client.on_publish = PublishPeopleNo.on_publish
            client.connect(ip, int(port))
            client.loop_start()
        except:
            print "PublishPeopleNo: ERROR IN CONNECTING TO THE BROKER"

        while True:
            sens.load_topics()
            sens.publish_people_counting()
            time.sleep(30)