import paho.mqtt.client as PahoMQTT

class MyMQTT:
    def __init__(self, broker, port, notifier):
        self.broker = broker
        self.port = port
        self.notifier = notifier
# create an instance of paho.mqtt.client
        self._paho_mqtt = PahoMQTT.Client("clientid", False)
# register the callback
        self._paho_mqtt.on_connect = self.myOnConnect
        self._paho_mqtt.on_message = self.myOnMessageReceived
    def myOnConnect (self, paho_mqtt, userdata, flags, rc):
        print ("Connected to message broker with result code: "+str(rc))
    def myOnMessageReceived (self, paho_mqtt , userdata, msg):
# A new message is received
        self.notifier.notify (msg.topic, msg.payload)