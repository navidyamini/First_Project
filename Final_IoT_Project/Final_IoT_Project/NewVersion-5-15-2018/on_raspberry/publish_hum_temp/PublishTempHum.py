#####################################################
##   First class that have to PUBLISH data about   ##
##   TEMPERATURE and HUMIDITY                      ##
##   to be placed on RASPERRYPI                    ##
#####################################################

from ReadingDHT import ReadingDHT
import paho.mqtt.client as mqttc
import time
import datetime
import requests
import json

class PublishData(object):

    def __init__(self, url, sensor_t_h,roomId, client):
        self.url = url
        self.sensor_t_h = sensor_t_h
        self.client = client
        self.roomId=roomId

    def load_topics(self):
        try:
            self.respond = requests.get(self.url)
            json_format = json.loads(self.respond.text)
            self.DHT_Topic = json_format["topic"]["DHT_Topic"]
            print "PublishData:: BROKER VARIABLES ARE READY"
        except:
            print "PublishData: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER TOPICS"

    @staticmethod
    def on_connect(rc):
        # get the current time
        get_time = datetime.datetime.now()
        current_time = get_time.strftime("%Y-%m-%d %H:%M:%S")
        print ('CONN ACK received with code: ' + str(rc))
        print ("at time: " + str(current_time))
        return str(rc)

    @classmethod
    def on_publish(cls, mid):
        # get the current time
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("mid: " + str(mid))
        print ("at time: " + str(current_time))
        return str(mid)

    def publish_sensor_data(self):
        #This function will publishe the data related to temperature and humidity
        try:
            json_format = self.sensor_t_h.reading_sensor()
            temp_hum_data = json.loads(json_format)
            temp = temp_hum_data["temperature"]
            hum = temp_hum_data["humidity"]
            time = temp_hum_data["time"]
            new_json_format=json.dumps({"subject":"temp_hum_data","roomId":self.roomId,"temperature": temp, "humidity": hum,"time":time})
            msg_info = client.publish(self.DHT_Topic, str(new_json_format), qos=1)
            if msg_info.is_published() == True:
                print ("\nMessage is published.")
            # This call will block until the message is published
            msg_info.wait_for_publish()
            return ("HELLO", json_format)
        except:
            get_time = datetime.datetime.now()
            current_time = get_time.strftime("%Y-%m-%d %H:%M:%S")
            print "PublishData: ERROR IN PUBLISHING DATA RELATED TO THE SENSORS"
            print ("at time: " + str(current_time))

if __name__ == '__main__':

    try:
        file = open("config_file.json", "r")
        json_string = file.read()
        file.close()
    except:
        raise KeyError("***** PublishData: ERROR IN READING CONFIG FILE *****")

    config_json = json.loads(json_string)
    resourceCatalogIP = config_json["reSourceCatalog"]["url"]
    roomId = config_json["reSourceCatalog"]["roomId"]
    url = resourceCatalogIP + roomId
    try:
        sensor_data = ReadingDHT()
    except:
        print "PublishData: ERROR IN GETTING DATA FROM SENSOR "

    client = mqttc.Client()
    sens = PublishData(url, sensor_data,roomId, client)

    while True:
        sens.load_topics()
        try:
            respond = requests.get(resourceCatalogIP+"/broker")
            json_format = json.loads(respond.text)
            broker_ip = json_format["Broker_IP"]
            port = json_format["Broker_port"]
        except:
            print "PublishData: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER IP"

        try:
            client.on_connect = PublishData.on_connect
            client.on_publish = PublishData.on_publish
            client.connect(broker_ip, int(port))
            client.loop_start()
        except:
            print "PublishData: ERROR IN CONNECTING TO THE BROKER"

        while True:
            sens.load_topics()
            sens.publish_sensor_data()
            time.sleep(30)