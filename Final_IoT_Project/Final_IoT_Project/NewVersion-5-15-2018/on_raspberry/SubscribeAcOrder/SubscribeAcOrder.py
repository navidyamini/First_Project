#######################################################
##   Third class that have to SUBSCRIBE data         ##
##   to be placed on PC                              ##
#######################################################

import datetime
import paho.mqtt.client as paho
import requests
import json
import time
from LEDbyRelay import LEDbyRelay

class SubscribeAcOrder(object):

    payload = "null"
    orders = 'null'
    def __init__(self,url,roomId,client):
        self.flag = 0
        self.url =url
        self.controling_LED = LEDbyRelay(url,roomId)
        self.client = client
        client.on_subscribe = self.on_subscribe
        client.on_message = self.on_message

    def load_topics(self):
        try:
            self.respond = requests.get(self.url)
            json_format = json.loads(self.respond.text)
            self.AC_status = json_format["broker"]["AC_Topic"]
            print "SubscribeAcOrder: Ac TOPIC ARE READY"
        except:
            print "SubscribeAcOrder: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER TOPICS"

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
        message_body = str(msg.payload.decode("utf-8"))
        cls.payload = json.loads(message_body)
        cls.orders = cls.payload["Order"]

    def order(self):

        if(self.orders == "Turn_on" and self.flag == 0):
            print("Sending Turn on order")

            try:
                self.controling_LED.setup()
                self.controling_LED.connect()
                self.flag = 1
            except:
                print "SubscribeAcOrder: ERROR IN SENDING TURN ON ORDER TO RELAY"

        elif(self.orders == "Turn_off" and self.flag == 1):
            print("Sending Turn off order")
            try:
                self.controling_LED.setup()
                self.controling_LED.disconnect()
                self.flag = 0
            except:
                print "SubscribeAcOrder: ERROR IN SENDING TURN OFF ORDER TO RELAY"

if __name__ == '__main__':
    # RUN THE SUBSCRIBE FOR GETTING THE TEMPERATURE AND HUMIDITY DATA
    try:
        file = open("config_file.json", "r")
        json_string = file.read()
        file.close()
    except:
        raise KeyError("***** SubscribeAcOrder: ERROR IN READING CONFIG FILE *****")

    config_json = json.loads(json_string)
    ip = config_json["reSourceCatalog"]["url"]
    roomId = config_json["reSourceCatalog"]["roomId"]
    url = ip+roomId
    client = paho.Client()
    sens = SubscribeAcOrder(url,roomId, client)

    while True:
        try:
            sens.load_topics()
            respond = requests.get(url)
            json_format = json.loads(respond.text)
            Broker_IP = json_format["broker"]["Broker_IP"]
            Broker_Port = json_format["broker"]["Broker_port"]
            print "SubscribeAcOrder:: BROKER VARIABLES ARE READY"
        except:
            print "SubscribeAcOrder: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER TOPICS"
        try:
            client.connect(Broker_IP, int(Broker_Port))
            client.subscribe(str(sens.AC_status), qos=1)
            client.loop_start()
        except:
            print "SubscribeAcOrder: Problem in connecting to broker"
        sens.order()
        time.sleep(10)



