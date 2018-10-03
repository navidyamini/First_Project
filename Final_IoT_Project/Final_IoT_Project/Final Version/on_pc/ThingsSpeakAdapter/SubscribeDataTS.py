#######################################################
##   Third class that have to SUBSCRIBE data         ##
##   to be placed on PC                              ##
#######################################################
# this program subscribe the data coming from publishers and submit them on the thingSpkea
import datetime
import paho.mqtt.client as paho
import requests
import json
import time
from ThingSpeakUpload import ThingSpeak


class SubscribeDataTS(object):
    payload = "null"
    topic = "null"

    def __init__(self,url,client):
        self.url = url
        self.client = client
        client.on_subscribe = self.on_subscribe
        client.on_message = self.on_message
        # create an object from ThingSpeak class
        self.thingSpeak = ThingSpeak(self.url)

    def load_topics(self):
        try:
            # request the topics from the resource catalog
            self.respond = requests.get(self.url)
            json_format = json.loads(self.respond.text)
            self.DHT_topic = json_format["topic"]["DHT_Topic"]
            self.counter_topic = json_format["topic"]["Counter_Topic"]
            self.AC_status = json_format["topic"]["Ac_Status"]
            print ("SubscribeDataTS:: TOPICS ARE READY")
        except:
            print ("SubscribeDataTS: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER TOPICS")

    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("Subscribed: " + str(mid) + " " + str(granted_qos))
        print ("at time: " + str(current_time))

    @classmethod
    def on_message(cls,client, userdata, msg):
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("message received ", str(msg.payload.decode("utf-8")))
        print ("at time: " + str(current_time))
        print("--------------------------------------------------------------------")
        message_body = str(msg.payload.decode("utf-8"))
        cls.payload = json.loads(message_body)
        cls.topic = msg.topic

    # check the topic of the received message to call the relative method of the
    # thingSpeak object and publish the data on that channel
    def check(self):
        if(self.payload != 'null'):
            self.thingSpeak.setThingSpeakVariables()

            if(self.topic == self.DHT_topic ):
                self.thingSpeak.sending_dht_data(self.payload)
                time.sleep(10)
            elif(self.topic == self.counter_topic ):
                self.thingSpeak.number_of_people(self.payload)
                time.sleep(10)

            elif(self.topic == self.AC_status ):
                self.thingSpeak.ac_status(self.payload)
                time.sleep(10)
            payload='null'
        return

if __name__ == '__main__':
    # from config file it reads the resource catalog url and the
    # room_id that it should listen to its publishers.
    try:
        file = open("config_file.json", "r")
        json_string = file.read()
        file.close()
    except:
        raise KeyError("***** SubscribeDataTS: ERROR IN READING CONFIG FILE *****")
    #set the url and the room id
    config_json = json.loads(json_string)
    resourceCatalogIP = config_json["reSourceCatalog"]["url"]
    roomId = config_json["reSourceCatalog"]["roomId"]

    url= resourceCatalogIP + roomId
    client = paho.Client()
    #create an object from SubscribeDataTS
    sens = SubscribeDataTS(url, client)

    while True:
        try:
            # send the request to ge the broker ip
            sens.load_topics()
            respond = requests.get(resourceCatalogIP+"/broker")
            json_format = json.loads(respond.text)
            Broker_IP = json_format["Broker_IP"]
            Broker_Port = json_format["Broker_port"]
            print ("SubscribeDataTS:: BROKER VARIABLES ARE READY")
        except:
            print ("SubscribeDataTS: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER TOPICS")
        try:
            # set the topics by using the SubscribeDataTS
            client.connect(Broker_IP, int(Broker_Port))
            client.subscribe(str(sens.DHT_topic), qos=1)
            client.subscribe(str(sens.counter_topic), qos=1)
            client.subscribe(str(sens.AC_status), qos=1)
            client.loop_start()
        except:
            print ("SubscribeDataTS: Problem in connecting to broker")
        while True:
            sens.check()
            time.sleep(10)
