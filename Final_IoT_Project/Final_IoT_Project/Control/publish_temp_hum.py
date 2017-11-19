#####################################################
##   First class that have to PUBLISH data about   ##
##   TEMPERATURE and HUMIDITY                      ##
##   to be placed in RASPERRYPI                    ##
#####################################################

from reading_DHT import Reading_DHT
import paho.mqtt.client as mqttc
import time
import datetime

class publish_temp_hum(object):

    def __init__(self, sensor_t_h, client):
        self.sensor_t_h = sensor_t_h
        self.client = client

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        # get the current time
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print ('CONNACK received with code: ' + str(rc))
        print ("at time: " + str(current_time))
        return str(rc)

    @classmethod
    def on_publish(cls, client, userdata, mid):
        # get the current time
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("mid: " + str(mid))
        print ("at time: " + str(current_time))
        return str(mid)

    def publish_data(self):
        #This function will publishe the data related to temperature and humidity
        try:
            json_format = self.sensor_t_h.reading_sensor()
            msg_info = client.publish('sensors/data', str(json_format), qos=1)
            if msg_info.is_published() == True:
                print ("\nMessage is published.")
            # This call will block until the message is published
            msg_info.wait_for_publish()
            return ("CIAONE", json_format)
        except:
            get_time = datetime.datetime.now()
            current_time = get_time.strftime("%Y-%m-%d %H:%M:%S")
            print "Error in publishing data data in class publish_temp_hum"
            print ("at time: " + str(current_time))

if __name__ == '__main__':


    try:
        sensor_data = Reading_DHT()
    except:
        print "Problem in getting data from sensor in publish_temp_hum"

    client = mqttc.Client()
    sens = publish_temp_hum(sensor_data, client)

    while True:
        try:
            client.on_connect = publish_temp_hum.on_connect
            client.on_publish = publish_temp_hum.on_publish
            client.connect('192.168.1.254', 1883)
            client.loop_start()
        except:
            print "Problem in connecting to broker in class publish_temp_hum"

        while True:
            sens.publish_data()
            time.sleep(5)