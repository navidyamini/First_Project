from MyMQTT import MyMQTT

class Publish_DHT(object):
    def __init__(self):
        #create an instance of paho.mqtt.client
        self.myMqtt = MyMQTT('192.168.1.110',1883,self)

    def run(self):
        #if needed, perform some other actions befor ending the sofware
        self.myMqtt.start()

    def end(self):
        self.myMqtt.stop()

    def notify(self,topic,msg):
        #manage here your recieved message. you can perform some error_check here
        print"received %s under topic %s" % (topic, msg)

if __name__ == "__main__":
    test = Publish_DHT()
    test.run()
    test.myMqtt.mySubscribe("/my/topic",2)
    test.myMqtt.myPublish("/my/topic","my message",2)

    #perform some other actions befor ending the software

    test.end()

