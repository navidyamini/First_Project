import requests
import json
import time
import datetime
import paho.mqtt.client as mqttc

class CheckingThreshold(object):

    def __init__(self,url,roomId,client):
        self.url_resource = url
        self.room_id = roomId
        self.flag = 0
        self.temperature = 0.00
        self.humidity = 0.00
        self.max_temperature = 0.00
        self.max_humidity = 0.00
        self.min_temperature = 0.00
        self.min_humidity = 0.00
        self.client = client

    def load_file(self):
        try:
            # sending the rquest to the resource
            # catalog to get he MQTT To webService url
            respond = requests.get(self.url_resource+"/dataToRest")
            json_format = json.loads(respond.text)
            self.restURL = json_format["Host_IP"]
            self.port = json_format["port"]

        except :
            print "CheckingThreshold: ERROR IN CONNECTING TO THE SERVER FOR GETTING WEB SERVICE IP"

        try:
          # sending the request to the resource catalog to
          # get the threshold values for the specified room
            respond = requests.get(self.url_resource+"/"+self.room_id)
            json_format = json.loads(respond.text)
            self.AC_Topic = json_format["topic"]["AC_Topic"]
            self.max_temperature = json_format["thresholds"]["max_temp"]
            self.max_humidity = json_format["thresholds"]["max_hum"]
            self.min_temperature = json_format["thresholds"]["min_temp"]
            self.min_humidity = json_format["thresholds"]["min_hum"]

        except :
            print "CheckingThreshold: ERROR IN CONNECTING TO THE SERVER FOR READING initial_data.JSON"
        return

    def getting_temp_hum(self):
        # sending request to the MQTT To WebService to get
        # the current value for the temperature and humidity
        try:
            self.temperature = requests.get("http://" + self.restURL + ":" + self.port + "/" + self.room_id + "/temp").content
            self.humidity = requests.get("http://" + self.restURL + ":" + self.port + "/" + self.room_id + "/hum").content
            print "real time data",self.temperature,self.humidity
        except:
            print "CheckingThreshold: ERROR IN GETTING DATA FROM WEB SERVICE"
        return

    def check_thresholds(self):
        # check the current values with the thresholds
        temperature =float(self.temperature)
        humidity= float(self.humidity)
        if (temperature > float(self.max_temperature)) or (temperature < float(self.min_temperature)) or (humidity > float(self.max_humidity)) or (humidity < float(self.min_humidity)):
            #set the publisher message for turning on the A/C
            self.order = "Turn_on"
            try:
                self.order_msg = json.dumps({"subject": "AcOrder","roomId": self.room_id,"Order": str(self.order)})
            except:
                print "CheckingThreshold: ERROR IN SENDING TURN ON ORDER"
        else:
            # set the publisher message for turning off the A/C
            self.order = "Turn_off"
            try:
                self.order_msg = json.dumps({"subject": "AcOrder","roomId": self.room_id, "Order": str(self.order)})
            except:
                print "CheckingThreshold: ERROR IN SENDING TURN OFF ORDER"
        return

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        # get the current time
        get_time = datetime.datetime.now()
        current_time = get_time.strftime("%Y-%m-%d %H:%M:%S")
        print ('CONNACK received with code: ' + str(rc))
        print ("at time: " + str(current_time))
        return str(rc)

    @classmethod
    def on_publish(cls, client, userdata, mid):
        # get the current time
        get_time = datetime.datetime.now()
        current_time = get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("mid: " + str(mid))
        print("Published Message")
        print ("at time: " + str(current_time))
        print("--------------------------------------------------------------------")
        return str(mid)

    def publish_order(self):
        #This function will publishe the order to AC
        try:
            print self.order_msg
            self.client.publish(self.AC_Topic, str(self.order_msg), qos=1)
            return ("CIAONE", self.order_msg)
        except:
            get_time = datetime.datetime.now()
            current_time = get_time.strftime("%Y-%m-%d %H:%M:%S")
            print ("PublishAcStatus:ERROR IN PUBLISHING THE DATA")
            print ("at time: " + str(current_time))
        return

if __name__ == '__main__':
    # reading the config file to set the room_id and the resource catalog url
    try:
        file = open("config_file.json", "r")
        json_string = file.read()
        file.close()
    except:
        raise KeyError("***** CheckingThreshold: ERROR IN READING CONFIG FILE *****")

    config_json = json.loads(json_string)

    resourceCatalogIp = config_json["reSourceCatalog"]["url"]
    roomId = config_json["reSourceCatalog"]["room_Id"]
    client = mqttc.Client()
    sens = CheckingThreshold(resourceCatalogIp, roomId ,client)

    while True:
        sens.load_file()
        sens.getting_temp_hum()
        sens.check_thresholds()
    # sending request to resource catalog to het the broker ip
        try:
            respond = requests.get(resourceCatalogIp+"/broker")
            json_format = json.loads(respond.text)
            ip = json_format["Broker_IP"]
            port = json_format["Broker_port"]
        except:
            print "PublishData: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER IP"

        try:
            client.on_connect = CheckingThreshold.on_connect
            client.on_publish = CheckingThreshold.on_publish
            client.connect(str(ip), int(port))
            client.loop_start()
        except:
            print "PublishData: ERROR IN CONNECTING TO THE BROKER"

        sens.publish_order()
        time.sleep(10)