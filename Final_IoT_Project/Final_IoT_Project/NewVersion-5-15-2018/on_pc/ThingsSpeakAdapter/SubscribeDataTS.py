#######################################################
##   Third class that have to SUBSCRIBE data         ##
##   to be placed on PC                              ##
#######################################################

import datetime
import paho.mqtt.client as paho
import requests
import json
import time
from ThingSpeakUpload import ThingSpeak
payload = "null"
topic = "null"

class SubscribeDataTS(object):

    def __init__(self,url,client):
        self.url = url
        self.client = client
        client.on_subscribe = self.on_subscribe
        client.on_message = self.on_message
        self.thingSpeak = ThingSpeak(self.url)

    def load_topics(self):
        try:
            self.respond = requests.get(self.url)
            json_format = json.loads(self.respond.text)
            self.DHT_topic = json_format["broker"]["DHT_Topic"]
            self.counter_topic = json_format["broker"]["Counter_Topic"]
            self.AC_status = json_format["broker"]["AC_Topic"]
            print "SubscribeDataTS:: TOPICS ARE READY"
        except:
            print "SubscribeDataTS: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER TOPICS"

    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("Subscribed: " + str(mid) + " " + str(granted_qos))
        print ("at time: " + str(current_time))

    @classmethod
    def on_message(self,client, userdata, msg):
        global payload
        global topic
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("message received ", str(msg.payload.decode("utf-8")))
        print ("at time: " + str(current_time))
        message_body = str(msg.payload.decode("utf-8"))
        payload = json.loads(message_body)
        topic = msg.topic

    def check(self):
        global payload
        global topic

        if(payload != 'null'):
            self.thingSpeak.setThingSpeakVariables()
            #print(payload)
            if(topic == self.DHT_topic ):
                self.thingSpeak.sending_dht_data(payload)
                time.sleep(10)
            elif(topic == self.counter_topic ):
                self.thingSpeak.number_of_people(payload)
                time.sleep(10)
            #TODO send the ac status to thing speak
            #elif(topic == self.AC_status ):
                #self.thingSpeak.ac_status(payload)
            #print ("from chek",payload,topic)
            payload='null'
        return

if __name__ == '__main__':
    #url = 'http://192.168.1.65:8080/'
    try:
        file = open("config_file.json", "r")
        json_string = file.read()
        file.close()
    except:
        raise KeyError("***** SubscribeDataTS: ERROR IN READING CONFIG FILE *****")

    config_json = json.loads(json_string)
    url = config_json["reSourceCatalog"]["url"]
    client = paho.Client()
    sens = SubscribeDataTS(url, client)

    while True:
        try:
            sens.load_topics()
            respond = requests.get(url)
            json_format = json.loads(respond.text)
            Broker_IP = json_format["broker"]["Broker_IP"]
            Broker_Port = json_format["broker"]["Broker_port"]
            print "SubscribeDataTS:: BROKER VARIABLES ARE READY"
        except:
            print "SubscribeDataTS: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER TOPICS"
        try:
            client.connect(Broker_IP, int(Broker_Port))
            client.subscribe(str(sens.DHT_topic), qos=1)
            client.subscribe(str(sens.counter_topic), qos=1)
            client.subscribe(str(sens.AC_status), qos=1)
            client.loop_start()
        except:
            print "SubscribeDataTS: Problem in connecting to broker"
        while True:
            sens.check()
            time.sleep(10)
