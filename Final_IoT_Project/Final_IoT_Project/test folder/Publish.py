from Publish_Subscribe import Publish_Subscribe
from reading_DHT import Reading_DHT
import time
import json

if __name__ == "__main__":

    sensor_data = Reading_DHT()
    test = Publish_Subscribe('iot.eclipse.org',1883)
    test.run()
    #test.myMqtt.mySubscribe("/my/topic",2)
    try:
        while True:
            json_format = sensor_data.reading_sensor()
            THD_json = json.loads(json_format)
            test.myMqtt.myPublish("/my/topic","try to test",2)
            time.sleep(30)
    #perform some other actions befor ending the software
    except KeyboardInterrupt:
        test.end()