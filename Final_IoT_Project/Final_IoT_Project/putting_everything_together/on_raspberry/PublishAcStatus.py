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

    def __init__(self):
        self.url = 'http://192.168.1.65:8080/'
        try:
            respond = requests.get(self.url)
        except:
            print ("PublishAcStatus: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER TOPICS")
        json_format = json.loads(respond.text)
        Broker_IP = json_format["broker"]["Broker_IP"]
        Broker_port = json_format["broker"]["Broker_port"]
        self.AC_Topic = json_format["broker"]["AC_Topic"]
        print "PublishAcStatus:: BROKER VARIABLES ARE READY"

        try:
            self.client = paho.Client()
            self.client.on_connect = self.on_connect
            self.client.on_publish = self.on_publish
            self.client.connect(Broker_IP, int(Broker_port))
        except:
            print ("PublishAcStatus:ERROR IN CONNECTING TO THE BROKER")

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
            json_format = json.dumps({'Order' : str(order)})
            self.client.publish(self.AC_Topic, str(json_format), qos=1)
            return ("CIAONE", json_format)
        except:
            get_time = datetime.datetime.now()
            current_time = get_time.strftime("%Y-%m-%d %H:%M:%S")
            print ("PublishAcStatus:ERROR IN PUBLISHING THE DATA")
            print ("at time: " + str(current_time))