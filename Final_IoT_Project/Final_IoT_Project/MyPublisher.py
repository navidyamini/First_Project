import paho.mqtt.client as PahoMQTT
import time

class MyPublisher:

    def __init__(self, broker, port, topic, msg, qos):

        self.paho_mqtt_client = PahoMQTT.Client("clientId",False)
        self.paho_mqtt_client.on_connect = self.onConnect
        #time.sleep(5)
        self.paho_mqtt_client.on_publish = self.onPublish
        #time.sleep(5)
        self.paho_mqtt_client.connect(broker, port)
        #time.sleep(5)
        self.paho_mqtt_client.loop_start()
        self.paho_mqtt_client.publish(topic, msg, qos)
        time.sleep(30)
    def onConnect (self, paho_mqtt, userdata, flags, rc):
        print ("Connected to message broker with result code: "+str(rc))

    def onPublish(client, userdata,flags, mid):
        print("mid: " + str(mid))
        #print "hi"

    #def publish(self, topic, msg, qos ):
        #self.paho_mqtt_client.publish(topic, msg, qos)