import paho.mqtt.client as PahoMQTT
import time
class MySubscriber:
    def __init__(self, broker, port, topic, qos):
        self._paho_mqtt = PahoMQTT.Client("clientId",False)
        self._paho_mqtt.on_connect = self.myOnConnect
        self._paho_mqtt.on_subscribe = self.subscribe
        self._paho_mqtt.on_message = self.myOnMessageReceived
        self. _paho_mqtt.connect(broker, port)
        self._paho_mqtt.loop_start()
        self._paho_mqtt.subscribe(topic, qos)
        time.sleep(50)
    def myOnConnect (self, paho_mqtt, userdata, flags, rc):
        print ("Connected to message broker with result code: "+str(rc))

    def myOnMessageReceived (self, _paho_mqtt , userdata, msg):
        print ("Message: " + msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    def subscribe(client, userdata, mid,flag, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))