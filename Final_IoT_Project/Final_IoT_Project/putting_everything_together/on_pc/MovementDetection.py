import paho.mqtt.client as paho
import requests
import json
import time

class MovementDetection(object):

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        client.subscribe("commands/boards/raspberry3/actuators/led01")
        print("\n I'm connected to the MQTT SERVER")
        print("\n- Connection received with code: ", str(rc))

    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    @staticmethod
    def on_message(client, userdata, msg):
        #moved ="null"
        message = str(msg.payload)
        print(msg.topic + " " + str(msg.qos) + " " + message)
        print("message received ", str(msg.payload.decode("utf-8")))

        try:
            file = open("../RawWebpage/map_beac_paints.json", "r")
            json_string = file.read()
            file.close()
        except:
            raise KeyError("***** ERROR IN READING JSON FILE RELATED TO RESOURCES *****")
        painting_json_format = json.loads(json_string)
        moved = painting_json_format[str(msg.payload.decode("utf-8"))]["paint"]
        print moved
        #moved = str(msg.payload.decode("utf-8"))
        print("message topic=", msg.topic)

        url = 'http://192.168.1.65:8080/'
        try:
            respond = requests.get(url)
        except:
            print "MovementDetection: ERROR IN CONNECTING TO THE SERVER FOR READING TELEGRAM INFO.JSON"
        json_format = json.loads(respond.text)
        TELEGRAM_TOKEN = json_format["telegram"]["Port"]
        TELEGRAM_CHAT_ID = json_format["telegram"]["chatID"]
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
    #movementDetection=MovementDetection()
    while True:
        try:
            #movementDetection.setTelegramVariables()
            client.on_connect = MovementDetection.on_connect
            client.on_subscribe = MovementDetection.on_subscribe
            client.on_message = MovementDetection.on_message
            client.connect('192.168.1.110', 1883, 60)
            client.subscribe("Estimote/TelemetryPackets/motionState", qos=0)
            client.loop_forever()
        except:
            print "MovementDetection: Problem in connecting to broker"
