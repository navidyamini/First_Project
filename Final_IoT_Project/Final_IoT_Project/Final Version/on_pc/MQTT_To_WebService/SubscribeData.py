#######################################################
##   Third class that have to SUBSCRIBE data         ##
##   to be placed on PC                              ##
#######################################################
# this will subscribe the data from all publishers, and write the received data into real time data json file
import datetime
import paho.mqtt.client as paho
import requests
import json


class SubscribeData(object):

    def __init__(self,client):
        self.client = client
        client.on_subscribe = self.on_subscribe
        client.on_message = self.on_message

    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("Subscribed: " + str(mid) + " " + str(granted_qos))
        print ("at time: " + str(current_time))

    @classmethod
    def on_message(self,client, userdata, msg):
        # the received message is in json format,
        get_time = datetime.datetime.now()
        current_time =  get_time.strftime("%Y-%m-%d %H:%M:%S")
        print("message received ", str(msg.payload.decode("utf-8")))
        print ("at time: " + str(current_time))
        print("--------------------------------------------------------------------")
        message_body = str(msg.payload.decode("utf-8"))

        #first it will read the real time data file
        try:
            file = open("real_time_data.json", "r")
            json_string = file.read()
            file.close()
        except:
            raise KeyError("*****SubscribeData: ERROR IN READING JSON FILE RELATED TO REAL TIME DATA *****")
        input = json.loads(message_body)
        json_format_output = json.loads(json_string)
        # it will extract the room id from the received message and it will
        # check that it is exist in the real time data file or not,
        # if exist, it will uodate the values
        # if it is not exist it will inser the new room into the file
        the_romm_id = input["roomId"]
        subject = input["subject"]
        print(the_romm_id)
        if (the_romm_id in json_format_output ):
            if (subject == "temp_hum_data"):
                json_format_output[the_romm_id]["temperature"]["value"] = input["temperature"]
                json_format_output[the_romm_id]["humidity"]["value"] = input["humidity"]

            elif (subject == "num_people"):
                json_format_output[the_romm_id]["bluetoothCounter"]["value"] = input["bluetooth_counter"]

            elif (subject == "Ac_Status"):
                json_format_output[the_romm_id]["AcStatus"]["value"] = input["Status"]

        else:
            if (subject == "temp_hum_data"):
                temporary_json={}
                temporary_json["temperature"]={"value":input["temperature"]}
                temporary_json["humidity"]={"value":input["humidity"]}
                temporary_json["bluetoothCounter"]={"value":0}
                temporary_json["AcStatus"]={"value":"It is OFF"}
                json_format_output[the_romm_id] = temporary_json

            elif (subject == "num_people"):
                temporary_json={}
                temporary_json["temperature"]={"value":0}
                temporary_json["humidity"]={"value":0}
                temporary_json["bluetoothCounter"]={"value":input["bluetooth_counter"]}
                temporary_json["AcStatus"]={"value":"It is OFF"}
                json_format_output[the_romm_id] = temporary_json

            elif (subject == "Ac_Status"):
                temporary_json={}
                temporary_json["temperature"]={"value":0}
                temporary_json["humidity"]={"value":0}
                temporary_json["bluetoothCounter"]={"value":0}
                temporary_json["AcStatus"]={"value":input["Status"]}
                json_format_output[the_romm_id] = temporary_json

        # write the data into the file
        try:
            with open("real_time_data.json", 'w') as json_data_file:
                json.dump(json_format_output, json_data_file)
                json_data_file.close()
        except:
            raise KeyError("*****SubscribeData ERROR IN WRITING THE JSON FILE*****")

if __name__ == '__main__':
    #  reading the resource catalog url from the config file
    try:
        file = open("config_file.json", "r")
        json_string = file.read()
        file.close()
    except:
        raise KeyError("***** SubscribeData: ERROR IN READING CONFIG FILE *****")

    config_json = json.loads(json_string)
    resourceCatalogIP = config_json["reSourceCatalog"]["url"]
    wildcard_topic = config_json["reSourceCatalog"]["wildcards"]

    client = paho.Client()
    sens = SubscribeData(client)

    while True:
        # sending the request to the resource catolog to set the broker ip and topics
        try:
            respond = requests.get(resourceCatalogIP+"/broker")
            json_format = json.loads(respond.text)
            Broker_IP = json_format["Broker_IP"]
            Broker_Port = json_format["Broker_port"]
            print ("SubscribeData:: BROKER VARIABLES ARE READY")
        except:
            print ("SubscribeData: ERROR IN CONNECTING TO THE SERVER FOR READING BROKER TOPICS")
        try:
            client.connect(Broker_IP, int(Broker_Port))
            client.subscribe(str(wildcard_topic), qos=1)
            client.loop_forever()
        except:
            print ("SubscribeData: Problem in connecting to broker")

