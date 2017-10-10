import paho.mqtt.client as PahoMQTT

class MyMQTT(object):
    def __init__(self, broker, port, notifier):
        self.broker = broker
        self.port = port
        self.notifier = notifier
        self._paho_mqtt = PahoMQTT.Client("clientid", False)
        self._paho_mqtt.on_connect = self.myOnConnect
        self._paho_mqtt.on_message = self.myOnMessageReceived
        #self._paho_mqtt.on_publish = self.on_publish
        #self._paho_mqtt.on_subscribe = self.mySubscribe

    def myOnConnect (self, paho_mqtt, userdata, flags, rc):
        print ("Connected to message broker with result code: "+str(rc))

    def myOnMessageReceived (self, paho_mqtt , userdata, msg):
# A new message is received
        self.notifier.notify (msg.topic, msg.payload)
        print "message recived"

    def myPublish(self, topic, msg, qos =2):
        self._paho_mqtt.publish(topic, msg, qos)
        print topic +" " + msg
    
    def mySubscribe(self, topic, qos =2):
        self._paho_mqtt.subscribe(topic, qos)
        print topic

    def start(self):
        #manage connection to broker
        self._paho_mqtt.connect(self.broker, self.port)
        self._paho_mqtt.loop_start()

    def stop(self):
        self._paho_mqtt.loop_stop()

#    def on_publish(client, userdata, mid):
#        print("mid: " + str(mid))
#done

