from MyMQTT import MyMQTT

class Publish_Subscribe(object):
    def __init__(self, broker, port):
        #create an instance of paho.mqtt.client
        self.myMqtt = MyMQTT(broker, port,self)

    def run(self):
        #if needed, perform some other actions befor ending the sofware
        self.myMqtt.start()

    def end(self):
        self.myMqtt.stop()

    def notify(self,topic,msg):
        #manage here your recieved message. you can perform some error_check here
        print"received %s under topic %s" % (topic, msg)



