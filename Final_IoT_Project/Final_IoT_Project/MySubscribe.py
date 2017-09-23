29
import paho.mqtt.client as PahoMQTT

class MySubscriber:
    def __init__(self):
# create an instance of paho.mqtt.client
        self._paho_mqtt = PahoMQTT.Client(clientid, False)
# register the callback
        self._paho_mqtt.on_connect = self.myOnConnect
        self._paho_mqtt.on_message = self.myOnMessageReceived

        #manage connection to broker
        self. _paho_mqtt.connect('iot.eclipse.org', 1883)
        self._paho_mqtt.loop_start()
        # subscribe for a topic
        self._paho_mqtt.subscribe('/this/is/my/topic', 2)
    def myOnConnect (self, paho_mqtt, userdata, flags, rc):
        print ("Connected to message broker with result code: "+str(rc))
    def myOnMessageReceived (self, paho_mqtt , userdata, msg):
# A new message is received
        print ("Message: " + msg.topic+" "+str(msg.qos)+" "+str(msg.payload))