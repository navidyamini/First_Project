from MyMQTT import MyMQTT
import time

class Publish_Subscribe(object):
    def __init__(self, broker, port):
        #create an instance of paho.mqtt.client
        self.myMqtt = MyMQTT(broker, port,self)

    def run(self):
        self.myMqtt.start()

    def end(self):
        self.myMqtt.stop()

    def notify(self,topic,msg):
        #manage here your recieved message. you can perform some error_check here
        print"received %s under topic %s" % (topic, msg)


if __name__ == "__main__":

    test = Publish_Subscribe('iot.eclipse.org', 1883)
    test.run()
    test.myMqtt.mySubscribe("/my/topic",2)
    test.myMqtt.myPublish("/my/topic", "try to test", 2)
    #time.sleep(30)
    # perform some other actions befor ending the software
    test.end()



