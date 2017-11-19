#######################################################
##   Third class that have to SUBSCRIBE data about   ##
##   turning on and off the AC                       ##
##   to be placed in RASPERRYPI                      ##
#######################################################

import paho.mqtt.client as paho
#from Checking_threshold import Checking_threshold
import datetime

class Subscribe_order_AC(object):

    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("Subscribed: " + str(mid) + " " + str(granted_qos))
        print ("at time: " + str(current_time))

    @staticmethod
    def on_message(client, userdata, msg):
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("message received ", str(msg.payload.decode("utf-8")))
        print ("at time: " + str(current_time))
        #sending the data to Checking_threshold for checking the tresholds.
        #check_data = Checking_threshold()
        #check_data.sensor_data(msg.payload)
        #check_data.load_file()
        #check_data.checking()


if __name__ == '__main__':
    # RUN THE SUBSCRIBE FOR GETTING THE order for AC
    client = paho.Client()
    while True:
        try:
            client.on_subscribe = Subscribe_order_AC.on_subscribe
            client.on_message = Subscribe_order_AC.on_message
            client.connect('192.168.1.254', 1883)
            client.subscribe('Ac/Order', qos=1)
            client.loop_forever()
        except:
            print "Problem in connecting to broker in Subscribe_order_AC classT"

