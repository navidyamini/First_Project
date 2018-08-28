#####################################################
##   First class that have to PUBLISH data about   ##
##   the status of the AC                          ##
##   to be placed on RASPERRYPI                    ##
#####################################################

import paho.mqtt.client as paho
import datetime
import json
import requests

class PublishAcStatus(object):

    def __init__(self,url):
        self.url = url
        self.client = paho.Client()
        self.client.on_connect = self.on_connect
        self.client.on_publish = self.on_publish


    @staticmethod
    def on_connect(client, userdata, flags, rc):
        # get the current time
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
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

    def publish_data(self,order):
        #This function will publishe the order to AC
        try:
            json_format = json.dumps({'Status' : str(order)})
            self.client.publish(self.AC_Topic, str(json_format), qos=1)
            return ("CIAONE", json_format)
        except:
            get_time = datetime.datetime.now()
            current_time = get_time.strftime("%Y-%m-%d %H:%M:%S")
            print ("PublishAcStatus:ERROR IN PUBLISHING THE DATA")
            print ("at time: " + str(current_time))

    def start(self):
        self.client.loop_start();

    def stop(self):
        self.client.loop_stop();

    def load(self):
        try:
            respond = requests.get(self.url)
            json_format = json.loads(respond.text)
            Broker_IP = json_format["broker"]["Broker_IP"]
            Broker_port = json_format["broker"]["Broker_port"]
            self.AC_Topic = json_format["broker"]["Ac_Status"]
            print "PublishAcStatus:: BROKER VARIABLES ARE READY"
        except:
            print ("PublishAcStatus: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER TOPICS")
        try:
            self.client.connect(Broker_IP, int(Broker_port))
        except:
            print ("PublishAcStatus:ERROR IN CONNECTING TO THE BROKER")
