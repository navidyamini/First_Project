from Checking_threshold import Checking_threshold
from subscribe_data_DHT import Subscriber_DHT
from LEDbyRelay import LEDbyRelay
import paho.mqtt.client as paho

if __name__ == '__main__':
    pinNo = 17
    controling_LED = LEDbyRelay(pinNo)
    checking_threshold = Checking_threshold()
    client = paho.Client()
    try:

        client.on_subscribe = Subscriber_DHT.on_subscribe
        client.on_message = Subscriber_DHT.on_message
        client.connect('192.168.1.110', 1883)
        client.subscribe("sensors/#", qos=1)
        client.loop_forever()

    except:
        print "ERROR: In subscribes the data"

