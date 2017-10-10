from Publish_Subscribe import Publish_Subscribe
import time

if __name__ == "__main__":
    
    
    test = Publish_Subscribe('iot.eclipse.org',1883)
    test.run()
    #test.myMqtt.mySubscribe("/my/topic",2)
    try:
        while True:
            test.myMqtt.myPublish("/my/topic","try to test",2)
            time.sleep(30)
    #perform some other actions befor ending the software
    except KeyboardInterrupt:
        test.end()