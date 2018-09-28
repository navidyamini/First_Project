import paho.mqtt.client as paho
import requests
import json
import time

class MovementDetection(object):

    def __init__(self):
        try:
            file = open("config_file.json", "r")
            json_string = file.read()
            file.close()
        except:
            raise KeyError("*****MovementDetection: ERROR IN READING JSON FILE RELATED TO RESOURCES *****")
        config_json = json.loads(json_string)
        self.ip = config_json["GalleryWebService"]["url"]
        respond = requests.get(self.ip)
        json_data = json.loads(respond.text)
        self.brokerIp =  json_data["broker"]["Broker_IP"]
        self.brokerPort = json_data["broker"]["Broker_port"]
        self.topic = json_data["broker"]["topic"]
    @staticmethod

    def on_connect(client, userdata, flags, rc):
        print("\n I'm connected to the MQTT SERVER")
        print("\n- Connection received with code: ", str(rc))

    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    @staticmethod
    def on_message(client, userdata, msg):

        paint = "null"
        message = str(msg.payload)
        print(msg.topic + " " + str(msg.qos) + " " + message)
        print("message received ", str(msg.payload.decode("utf-8")))

        try:
            file = open("config_file.json", "r")
            json_string = file.read()
            file.close()
        except:
            raise KeyError("*****MovementDetection: ERROR IN READING JSON FILE RELATED TO RESOURCES *****")
        config_json = json.loads(json_string)
        ip = config_json["GalleryWebService"]["url"]
        respond = requests.get(ip)
        json_data = json.loads(respond.text)
        painting_json_format = json_data["roomArtworks"]

        for object in painting_json_format:
            if object['beacon_id'] == str(msg.payload.decode("utf-8")):
                paint =  object['paint']
        if(paint != "null"):
            moved ="WARNING " + paint +" is moving"
            print moved
        else:
            moved = str(msg.payload.decode("utf-8"))
        print("message topic=", msg.topic)
        TELEGRAM_TOKEN = json_data["telegram"]["Port"]
        TELEGRAM_CHAT_ID = json_data["telegram"]["chatID"]
        print "MovementDetection:: TELEGRAM VARIABLES ARE READY"

        payload = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': moved,
            'parse_mode': 'HTML'
        }

        requests.post("https://api.telegram.org/bot{token}/sendMessage".format(token=TELEGRAM_TOKEN),
                      data=payload).content

if __name__ == '__main__':
    # RUN THE SUBSCRIBE FOR TRACKING BEACONS
    client = paho.Client()
    while True:
        try:
            file = open("config_file.json", "r")
            json_string = file.read()
            file.close()
        except:
            raise KeyError("*****MovementDetection: ERROR IN READING JSON FILE RELATED TO RESOURCES *****")
        config_json = json.loads(json_string)
        ip = config_json["GalleryWebService"]["url"]
        respond = requests.get(ip)
        json_data = json.loads(respond.text)
        brokerIp = json_data["broker"]["Broker_IP"]
        brokerPort = json_data["broker"]["Broker_port"]
        topic = json_data["broker"]["topic"]
        #movementDetection=MovementDetection()
        while True:
            try:
            #movementDetection.setTelegramVariables()
                client.on_connect = MovementDetection.on_connect
                client.on_subscribe = MovementDetection.on_subscribe
                client.on_message = MovementDetection.on_message
                client.connect(str(brokerIp), str(brokerPort), 60)
                client.subscribe(str(topic), qos=0)
                client.loop_forever()
            except:
                print "MovementDetection: Problem in connecting to broker"
