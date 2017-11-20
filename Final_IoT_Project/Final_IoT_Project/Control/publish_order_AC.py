#####################################################
##   First class that have to PUBLISH data about   ##
##   turning on and off the AC                     ##
##   to be placed in PC                            ##
#####################################################

import paho.mqtt.client as paho
import time
import datetime
import json

class publish_order_AC(object):

    def __init__(self):
        try:
            self.client = paho.Client()
            self.client.on_connect = self.on_connect
            self.client.on_publish = self.on_publish
            self.client.connect('192.168.1.254', 1883)
        except:
            print "problem in connecting to mqq broker in calss publish_order_AC"

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
            self.client.publish('Ac/Order', str(json_format), qos=1)
            return ("CIAONE", json_format)
        except:
            get_time = datetime.datetime.now()
            current_time = get_time.strftime("%Y-%m-%d %H:%M:%S")
            print "Error in publishing data in class publish_order_AC"
            print ("at time: " + str(current_time))