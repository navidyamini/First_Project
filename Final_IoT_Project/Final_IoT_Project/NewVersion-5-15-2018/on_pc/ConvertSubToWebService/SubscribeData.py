#######################################################
##   Third class that have to SUBSCRIBE data         ##
##   to be placed on PC                              ##
#######################################################

import datetime
import paho.mqtt.client as paho
import requests
import json


class SubscribeData(object):

    def __init__(self,url,client):
        self.url = url
        self.client = client
        client.on_subscribe = self.on_subscribe
        client.on_message = self.on_message

    def load_topics(self):
        try:
            self.respond = requests.get(self.url)
            json_format = json.loads(self.respond.text)
            self.DHT_topic = json_format["broker"]["DHT_Topic"]
            self.counter_topic = json_format["broker"]["Counter_Topic"]
            self.AC_status = json_format["broker"]["Ac_Status"]
            print "SubscribeData: TOPICS ARE READY"
        except:
            print "SubscribeData: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER TOPICS"

    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("Subscribed: " + str(mid) + " " + str(granted_qos))
        print ("at time: " + str(current_time))

    @classmethod
    def on_message(self,client, userdata, msg):

        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("message received ", str(msg.payload.decode("utf-8")))
        print ("at time: " + str(current_time))
        message_body = str(msg.payload.decode("utf-8"))

        try:
            file = open("config_file.json", "r")
            json_string = file.read()
            file.close()
        except:
            raise KeyError("***** SubscribeData: ERROR IN READING CONFIG FILE *****")

        config_json = json.loads(json_string)
        url = config_json["reSourceCatalog"]["url"]

        try:
            respond = requests.get(url)
            json_format = json.loads(respond.text)
            DHT_topic = json_format["broker"]["DHT_Topic"]
            counter_topic = json_format["broker"]["Counter_Topic"]
            AC_status = json_format["broker"]["Ac_Status"]
            print "SubscribeData: TOPICS ARE READY"
        except:
            print "SubscribeData: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER TOPICS"

        try:
            file = open("real_time_data.json", "r")
            json_string = file.read()
            file.close()
        except:
            raise KeyError("*****SubscribeData: ERROR IN READING JSON FILE RELATED TO REAL TIME DATA *****")
        input = json.loads(message_body)
        json_format_output = json.loads(json_string)

        if(msg.topic == DHT_topic):
            json_format_output["temperature"]["value"] = input["temperature"]
            json_format_output["humidity"]["value"] = input["humidity"]

        elif(msg.topic == counter_topic):
            json_format_output["bluetoothCounter"]["value"] = input["bluetooth counter"]

        elif (msg.topic == AC_status):
            json_format_output["AcStatus"]["value"] = input["Status"]

        try:
            with open("real_time_data.json", 'w') as json_data_file:
                json.dump(json_format_output, json_data_file)
                json_data_file.close()
        except:
            raise KeyError("*****SubscribeData ERROR IN WRITING THE JSON FILE*****")

if __name__ == '__main__':
    #url = 'http://192.168.1.65:8080/'
    try:
        file = open("config_file.json", "r")
        json_string = file.read()
        file.close()
    except:
        raise KeyError("***** SubscribeData: ERROR IN READING CONFIG FILE *****")

    config_json = json.loads(json_string)
    url = config_json["reSourceCatalog"]["url"]
    client = paho.Client()
    sens = SubscribeData(url, client)

    while True:
        try:
            sens.load_topics()
            respond = requests.get(url)
            json_format = json.loads(respond.text)
            Broker_IP = json_format["broker"]["Broker_IP"]
            Broker_Port = json_format["broker"]["Broker_port"]
            print "SubscribeData:: BROKER VARIABLES ARE READY"
        except:
            print "SubscribeData: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER TOPICS"
        try:
            client.connect(Broker_IP, int(Broker_Port))
            client.subscribe(str(sens.DHT_topic), qos=1)
            client.subscribe(str(sens.counter_topic), qos=1)
            client.subscribe(str(sens.AC_status), qos=1)
            client.loop_forever()
        except:
            print "SubscribeData: Problem in connecting to broker"

