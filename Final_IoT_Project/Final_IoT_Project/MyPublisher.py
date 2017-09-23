import paho.mqtt.client as PahoMQTT

class MyPublisher:
    def __init__(self):
# create an instance of paho.mqtt.client
        self._paho_mqtt = PahoMQTT.Client(clientid, False)
#register the callback
        self._paho_mqtt.on_connect = self.myOnConnect
#manage connection to broker
        self. _paho_mqtt.connect('example.mqtt.com', 1883)
        self._paho_mqtt.loop_start()
# publish a message with a certain topic
        self._paho_mqtt.publish('/this/is/my/topic', 'whatever message, also in JSON', 2)
    def myOnConnect (self, paho_mqtt, userdata, flags, rc):
        print ("Connected to message broker with result code: "+str(rc))