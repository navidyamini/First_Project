#######################################################
##   Third class that have to SUBSCRIBE data about   ##
##   turning on and off the AC                       ##
##   to be placed in RASPERRYPI                      ##
#######################################################

import paho.mqtt.client as paho
from LEDbyRelay import LEDbyRelay
import datetime
import json

class Subscribe_order_AC(object):

    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("Subscribed: " + str(mid) + " " + str(granted_qos))
        print ("at time: " + str(current_time))

    @staticmethod
    def on_message(client, userdata, msg):
        try:
            Subscribe_order_AC.flag = 0
            get_time = datetime.datetime.now()
            current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
            print("message received ", str(msg.payload.decode("utf-8")))
            print ("at time: " + str(current_time))
            message = str(msg.payload.decode("utf-8"))
        except:
            print "Problem in subscribe a message Subscribe_order_AC classT"
        #sending the data to chenging the status of the LED
        try:
            json_format = json.loads(message)
            order = json_format["Order"]
            print order
            controling_LED = LEDbyRelay(17)
            controling_LED.setup()
            if order == "Turn_on" and Subscribe_order_AC.flag ==0:
                Subscribe_order_AC.flag = 1
                controling_LED.connect()
            elif order == "Turn_off" and Subscribe_order_AC.flag == 1:
                Subscribe_order_AC.flag = 0
                controling_LED.disconnect()
        except:
            print" problem in connecting to LED in class Subscribe_order_AC"


if __name__ == '__main__':
    # RUN THE SUBSCRIBE FOR GETTING THE order for AC
    client = paho.Client()
    while True:

        try:
            client.on_subscribe = Subscribe_order_AC.on_subscribe
            client.on_message = Subscribe_order_AC.on_message
            client.connect('192.168.1.110', 1883)
            client.subscribe('Ac/Order', qos=1)
            client.loop_forever()
        except:
            print "Problem in connecting to broker in Subscribe_order_AC classT"

