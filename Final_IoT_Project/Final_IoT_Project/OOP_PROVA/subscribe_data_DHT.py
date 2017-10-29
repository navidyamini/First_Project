#######################################################
##   Third class that have to SUBSCRIBE data about   ##
##   TEMPERATURE and HUMIDITY                        ##
##   to be placed in PC                              ##
#######################################################

### It's also the second client of lab4 ex4

import paho.mqtt.client as paho

class Subscriber_DHT():

    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))
    @staticmethod
    def on_message(client, userdata, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        print("message received ", str(msg.payload.decode("utf-8")))
        print("message topic=", msg.topic)
        #print("message qos=", msg.qos)
        #print("message retain flag=", msg.retain)

if __name__ == '__main__':

    client = paho.Client()
    client.on_subscribe = Subscriber_DHT.on_subscribe
    client.on_message = Subscriber_DHT.on_message
    client.connect('192.168.1.254', 1883)
    client.subscribe("sensors/#", qos=1)
    client.loop_forever()

    # print("- VISUALIZE: \n1) Temperature \n2) Humidity \n3) Status of the LED")
    # selection = input("-->")
    #
    # if selection == 1:
    #     sens.publish_temp()
    #
    # elif selection == 2:
    #     sens.publish_hum()
    #
    # elif selection == 3:
    #     sens.change_status_led()
    #
    # else:
    #     print ("Insert a valid option")
