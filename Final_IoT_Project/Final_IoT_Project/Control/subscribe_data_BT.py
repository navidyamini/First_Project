#######################################################
##   Third class that have to SUBSCRIBE data about   ##
##   no of active bluetooth devices                  ##
##   to be placed in PC                              ##
#######################################################

import datetime

import paho.mqtt.client as paho

from thingspeak import thingspeak


class Subscribe_data_BT(object):

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
        to_thingspeak = thingspeak()
        to_thingspeak.sending_noDevices(msg.payload)


if __name__ == '__main__':
    # RUN THE SUBSCRIBE FOR GETTING THE no bluetooth devices
    client = paho.Client()
    while True:
        try:
            client.on_subscribe = Subscribe_data_BT.on_subscribe
            client.on_message = Subscribe_data_BT.on_message
            client.connect('192.168.1.110', 1883)
            client.subscribe("raspberry/noBluetooth", qos=1)
            print "1"
            client.loop_forever()
        except:
            print "Problem in connecting to broker in Subscribe_data_BT classT"

