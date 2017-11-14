from Checking_threshold import Checking_threshold
from subscribe_data_DHT import Subscriber_DHT
#from LEDbyRelay import LEDbyRelay
import paho.mqtt.client as paho

if __name__ == '__main__':
    #pinNo = 17
    #controling_LED = LEDbyRelay(pinNo)
    checking_threshold = Checking_threshold()
    client_temp = paho.Client()

    try:
        client_temp.on_subscribe = Subscriber_DHT.on_subscribe
        client_temp.on_message = Subscriber_DHT.on_message
        client_temp.connect('192.168.1.254', 1883)
        client_temp.subscribe("sensors/temperature", qos=1)
        #print("Publishing message to topic____________", "sensors/temperature")
        client_temp.loop_forever()
    except:
        print "ERROR: In subscribing the temperature value"

