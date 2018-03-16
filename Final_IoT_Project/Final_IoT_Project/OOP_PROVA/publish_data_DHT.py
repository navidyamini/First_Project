#####################################################
##   First class that have to PUBLISH data about   ##
##   TEMPERATURE and HUMIDITY                      ##
##   to be placed in RASPERRYPI                    ##
#####################################################

from reading_DHT import Reading_DHT
import paho.mqtt.client as mqttc
import time
import json

class Publisher_DHT:

    def __init__(self, sensor_t_h, client):
        self.sensor_t_h = sensor_t_h
        self.client = client

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print ('CONNACK received with code: ' + str(rc))
        return str(rc)

    @classmethod
    def on_publish(cls, client, userdata, mid):
        print("mid: " + str(mid))
        return str(mid)

    def publish_temp(self):

        self.sensor_t_h.reading_sensor()
        temp = self.sensor_t_h.temperature
        data_temp = {'temperature' : temp}
        json_temp = json.dumps(data_temp)
        print ("\n------------>", json_temp)
        (rc, mid) = client.publish('sensors/temperature', str(temp), qos=1)
        #print ("publish temp was done with code: ", rc)  #

        #######################
        msg_info = client.publish('sensors/temperature', str(temp), qos=1)
        if msg_info.is_published() == False:
            print ("\nMessage is not yet published.")

        # This call will block until the message is published
        msg_info.wait_for_publish()
        ########################
        return ("CIAONE", temp)


    def publish_hum(self):

        self.sensor_t_h.reading_sensor()

        # hum = sensor_data.humidity
        hum = self.sensor_t_h.humidity
        data_hum = {'humidity': hum}
        json_hum = json.dumps(data_hum)
        print ("\n------------>", json_hum)
        #(rc, mid) = client.publish('sensors/humidity', str(hum), qos=1)
        #print ("publish hum was done with code: ", hum)

        #######################
        msg_info = client.publish('sensors/humidity', str(hum), qos=1)
        if msg_info.is_published() == False:
            print ("Message is not yet published.")

        # This call will block until the message is published
        msg_info.wait_for_publish()
        ########################

        return ("CIAONEEE", hum)

    def change_status_led(self):
        status_led = client.subscribe("sensors/led", qos=1)
        print "Tge value of the LED is: " + str(status_led)


        #change_status_led = client.subscribe("sensors/led", qos=1)
        #print "****" + str(change_status_led)
        #print "+++++++" + str(client.subscribe("sensors/led/#")) + "+++++++"


if __name__ == '__main__':

    sensor_data = Reading_DHT()
    #while True:
    #    sensor_data.reading_sensor()
        #print str(sensor_data.humidity) + "****" + str(sensor_data.temperature)

    client = mqttc.Client()
    client.on_connect = Publisher_DHT.on_connect
    client.on_publish = Publisher_DHT.on_publish
    client.connect('192.168.1.110', 1883)
    client.loop_start()

    sens = Publisher_DHT(sensor_data, client)


    while True:

        sens.publish_temp()
        time.sleep(1)
        sens.publish_hum()
        time.sleep(1)
        sens.change_status_led()
        time.sleep(1)