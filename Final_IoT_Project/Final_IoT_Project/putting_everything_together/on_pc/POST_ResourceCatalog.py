import cherrypy
import json

class ResourceCatalog(object):

    exposed = True

    def GET(self, *uri, **params):

        try:
            #file = open("../RawWebpage/initial_data.json", "r") #Navid's IP
            file = open("../RawWebpage/xime_initial_data.json", "r") #Ximena's IP "localhost"
            json_string = file.read()
            file.close()
            room_id = uri[0]
        except:
            raise KeyError("***** ERROR IN READING JSON FILE RELATED TO RESOURCES *****")
        json_dic = json.loads(json_string)
        if (room_id in json_dic):
            result = json_dic[uri[0]]
            requested_data = json.dumps(result)
            return requested_data
        else:
            return "NOTHING FOUNDED, MAKE SURE THAT YOU ARE SENDING THE RIGHT VALUE IN THE URL"

    def POST(self, *uri, **params):
        try:
            with open("../RawWebpage/new_initial_data.json", "r") as idata:
                inidata = json.loads(idata.read())
                data = cherrypy.request.body.read()
                newdata = json.loads(data)

                print data
                print inidata
                print newdata
                key = list(newdata.keys())[0]



                if key =='thresholds1':

                    inidata["room_1"]['thresholds']['min_hum'] = newdata['thresholds1']['min_hum']
                    inidata["room_1"]['thresholds']['min_temp'] = newdata['thresholds1']['min_temp']
                    inidata["room_1"]['thresholds']['max_temp'] = newdata['thresholds1']['max_temp']
                    inidata["room_1"]['thresholds']['max_hum'] = newdata['thresholds1']['max_hum']
                elif key=='thingspeak1':
                    inidata["room_1"]['thingspeak']['READ_API_KEY'] = newdata['thingspeak1']['READ_API_KEY']
                    inidata["room_1"]['thingspeak']['ACCESS_TOKEN'] = newdata['thingspeak1']['ACCESS_TOKEN']
                    inidata["room_1"]['thingspeak']['tTransport'] = newdata['thingspeak1']['tTransport']
                    inidata["room_1"]['thingspeak']['channelID'] = newdata['thingspeak1']['channelID']
                    inidata["room_1"]['thingspeak']['tPort'] = newdata['thingspeak1']['tPort']
                    inidata["room_1"]['thingspeak']['mqttHost'] = newdata['thingspeak1']['mqttHost']
                    inidata["room_1"]['thingspeak']['THINGSPEAK_HOST'] = newdata['thingspeak1']['THINGSPEAK_HOST']
                elif key == 'broker1':
                    inidata["room_1"]['broker']['Broker_IP'] = newdata['broker1']['Broker_IP']
                    inidata["room_1"]['broker']['DHT_Topic'] = newdata['broker1']['DHT_Topic']
                    inidata["room_1"]['broker']['AC_Topic'] = newdata['broker1']['AC_Topic']
                    inidata["room_1"]['broker']['Ac_Status'] = newdata['broker1']['Ac_Status']
                    inidata["room_1"]['broker']['Broker_port'] = newdata['broker1']['Broker_port']
                    inidata["room_1"]['broker']['Counter_Topic'] = newdata['broker1']['Counter_Topic']
                elif key == 'telegram1':
                    inidata["room_1"]['telegram']['Port'] = newdata['telegram1']['Port']
                    inidata["room_1"]['telegram']['chatID'] = newdata['telegram1']['chatID']
                elif key == 'dataToRest1':
                    inidata["room_1"]['dataToRest']['Host_IP'] = newdata['dataToRest1']['Host_IP']
                    inidata["room_1"]['dataToRest']['port'] = newdata['dataToRest1']['port']


                elif key =='thresholds2':

                    inidata["room_2"]['thresholds']['min_hum'] = newdata['thresholds2']['min_hum']
                    inidata["room_2"]['thresholds']['min_temp'] = newdata['thresholds2']['min_temp']
                    inidata["room_2"]['thresholds']['max_temp'] = newdata['thresholds2']['max_temp']
                    inidata["room_2"]['thresholds']['max_hum'] = newdata['thresholds2']['max_hum']
                elif key=='thingspeak2':
                    inidata["room_2"]['thingspeak']['READ_API_KEY'] = newdata['thingspeak2']['READ_API_KEY']
                    inidata["room_2"]['thingspeak']['ACCESS_TOKEN'] = newdata['thingspeak2']['ACCESS_TOKEN']
                    inidata["room_2"]['thingspeak']['tTransport'] = newdata['thingspeak2']['tTransport']
                    inidata["room_2"]['thingspeak']['channelID'] = newdata['thingspeak2']['channelID']
                    inidata["room_2"]['thingspeak']['tPort'] = newdata['thingspeak2']['tPort']
                    inidata["room_2"]['thingspeak']['mqttHost'] = newdata['thingspeak2']['mqttHost']
                    inidata["room_2"]['thingspeak']['THINGSPEAK_HOST'] = newdata['thingspeak2']['THINGSPEAK_HOST']
                elif key == 'broker2':
                    inidata["room_2"]['broker']['Broker_IP'] = newdata['broker2']['Broker_IP']
                    inidata["room_2"]['broker']['DHT_Topic'] = newdata['broker2']['DHT_Topic']
                    inidata["room_2"]['broker']['AC_Topic'] = newdata['broker2']['AC_Topic']
                    inidata["room_2"]['broker']['Ac_Status'] = newdata['broker2']['Ac_Status']
                    inidata["room_2"]['broker']['Broker_port'] = newdata['broker2']['Broker_port']
                    inidata["room_2"]['broker']['Counter_Topic'] = newdata['broker2']['Counter_Topic']
                elif key == 'telegram2':
                    inidata["room_2"]['telegram']['Port'] = newdata['telegram2']['Port']
                    inidata["room_2"]['telegram']['chatID'] = newdata['telegram2']['chatID']
                elif key == 'dataToRest2':
                    inidata["room_2"]['dataToRest']['Host_IP'] = newdata['dataToRest2']['Host_IP']
                    inidata["room_2"]['dataToRest']['port'] = newdata['dataToRest2']['port']

            with open("../RawWebpage/initial_data.json", "w") as file:
                json.dump(inidata, file)
                return "UPDATED"

        except  Exception as e:
            print ("error:",e)
            return "Problem in updating file"

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    # cherrypy.quickstart(WebCalculator(),'/',conf)
    cherrypy.tree.mount(ResourceCatalog(), '/', conf)
    #cherrypy.server.socket_host = '192.168.1.65'
    #cherrypy.server.socket_port = '8080'
    cherrypy.config.update({
        "server.socket_host": 'localhost',
        "server.socket_port": 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()
