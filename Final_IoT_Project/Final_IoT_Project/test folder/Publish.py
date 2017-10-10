from Publish_Subscribe import Publish_Subscribe


if __name__ == "__main__":
    
    while True:
        test = Publish_Subscribe('iot.eclipse.org',1883)
        test.run()
        #test.myMqtt.mySubscribe("/my/topic",2)
        test.myMqtt.myPublish("/my/topic","my message",2)

        #perform some other actions befor ending the software

        test.end()