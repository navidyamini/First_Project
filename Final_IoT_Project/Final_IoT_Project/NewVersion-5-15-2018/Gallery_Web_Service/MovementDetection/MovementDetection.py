#RUN THE SUBSCRIBER FOR TRACKING BEACONS
#if someone move the beacon, it will publish the message
#with the beacon's Id, and this subscriber will send it to the telegram bot.

import paho.mqtt.client as paho
import requests
import json

class MovementDetection(object):

    @staticmethod
    def on_connect(rc):
        print("\n I'm connected to the MQTT SERVER")
        print("\n- Connection received with code: ", str(rc))

    @staticmethod
    def on_subscribe(mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    @staticmethod
    def on_message(msg):

        paint = "null"
        message = str(msg.payload)
        print(msg.topic + " " + str(msg.qos) + " " + message)
        print("message received ", str(msg.payload.decode("utf-8")))

        # read the config file to get the web server ip address
        # and then get information related to artworks
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

        #find whih beacon is moving and send the info about it to telegram bot
        for object in painting_json_format:
            if object['beacon_id'] == str(msg.payload.decode("utf-8")):
                paint =  object['paint']
        if(paint != "null"):
            moved ="WARNING " + paint +" is moving"
        else:
            moved = str(msg.payload.decode("utf-8"))
        TELEGRAM_TOKEN = json_data["telegram"]["Port"]
        TELEGRAM_CHAT_ID = json_data["telegram"]["chatID"]

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
        # read the config file to get the web server ip address
        # and then getting the broker ip address and the topic from the web server
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

        while True:
            try:
                client.on_connect = MovementDetection.on_connect
                client.on_subscribe = MovementDetection.on_subscribe
                client.on_message = MovementDetection.on_message
                client.connect(str(brokerIp), str(brokerPort), 60)
                client.subscribe(str(topic), qos=0)
                client.loop_forever()
            except:
                print "MovementDetection: Problem in connecting to broker"
