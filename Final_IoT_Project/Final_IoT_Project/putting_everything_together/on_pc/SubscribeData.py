#######################################################
##   Third class that have to SUBSCRIBE data         ##
##   to be placed on PC                              ##
#######################################################

import datetime
import paho.mqtt.client as paho

class SubscribeData(object):

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
        #check_data = CheckingThreshold()
        #check_data.sensor_data(msg.payload)
        #check_data.load_file()
        #check_data.checking()
        #to_thingspeak = thingspeak()
        #to_thingspeak.sending_dht_data(msg.payload)

if __name__ == '__main__':
    # RUN THE SUBSCRIBE FOR GETTING THE TEMPERATURE AND HUMIDITY DATA
    client = paho.Client()
    while True:
        try:
            client.on_subscribe = SubscribeData.on_subscribe
            client.on_message = SubscribeData.on_message
            client.connect('192.168.1.110', 1883)
            client.subscribe("sensors/data", qos=1)
            client.loop_forever()
        except:
            print "SubscribeData: Problem in connecting to broker"