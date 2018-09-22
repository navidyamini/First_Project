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
            item = uri[0]
        except:
            raise KeyError("***** ERROR IN READING JSON FILE RELATED TO RESOURCES *****")
        json_dic = json.loads(json_string)
        if(item in json_dic):
            result = json_dic[item]
            requested_data = json.dumps(result)
            return requested_data
        elif(item=="all"):
            return json_string
        else:
            return"NOTHING FOUNDED, MAKE SURE THAT YOU ARE SENDING THE RIGHT VALUE IN THE URL"

    def POST(self, *uri, **params):
        try:
            with open("../RawWebpage/xime_initial_data.json", "r") as idata:
                inidata = json.loads(idata.read())
                data = cherrypy.request.body.read()
                newdata = json.loads(data)

                print data
                print inidata
                print newdata
                key = list(newdata.keys())[0]

                #Room1
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

                #No specific room
                elif key == 'broker':
                    inidata['broker']['Broker_IP'] = newdata['broker']['Broker_IP']
                    inidata['broker']['DHT_Topic'] = newdata['broker']['DHT_Topic']
                    inidata['broker']['AC_Topic'] = newdata['broker']['AC_Topic']
                    inidata['broker']['Ac_Status'] = newdata['broker']['Ac_Status']
                    inidata['broker']['Broker_port'] = newdata['broker']['Broker_port']
                    inidata['broker']['Counter_Topic'] = newdata['broker']['Counter_Topic']
                elif key == 'telegram':
                    inidata['telegram']['Port'] = newdata['telegram']['Port']
                    inidata['telegram']['chatID'] = newdata['telegram']['chatID']
                elif key == 'dataToRest':
                    inidata['dataToRest']['Host_IP'] = newdata['dataToRest']['Host_IP']
                    inidata['dataToRest']['port'] = newdata['dataToRest']['port']

                #Room2
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



            with open("../RawWebpage/xime_initial_data.json", "w") as file:
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
