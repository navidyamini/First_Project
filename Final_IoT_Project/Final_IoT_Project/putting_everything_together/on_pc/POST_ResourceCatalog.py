import cherrypy
import json

class ResourceCatalog(object):

    exposed = True

    def GET(self, *uri, **params):

        try:
            file = open("../RawWebpage/initial_data.json", "r") #Navid's IP
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
            with open("../RawWebpage/initial_data.json", "r") as idata:
                inidata = json.loads(idata.read())
                data = cherrypy.request.body.read()
                newdata = json.loads(data)
                item = uri[0]


                if (item in inidata):

                    key = list(newdata.keys())[0]

                    if key =='thresholds':
                        inidata[item]['thresholds']['min_hum'] = newdata['thresholds']['min_hum']
                        inidata[item]['thresholds']['min_temp'] = newdata['thresholds']['min_temp']
                        inidata[item]['thresholds']['max_temp'] = newdata['thresholds']['max_temp']
                        inidata[item]['thresholds']['max_hum'] = newdata['thresholds']['max_hum']
                    elif key=='thingspeak':
                        inidata[item]['thingspeak']['READ_API_KEY'] = newdata['thingspeak']['READ_API_KEY']
                        inidata[item]['thingspeak']['ACCESS_TOKEN'] = newdata['thingspeak']['ACCESS_TOKEN']
                        inidata[item]['thingspeak']['tTransport'] = newdata['thingspeak']['tTransport']
                        inidata[item]['thingspeak']['channelID'] = newdata['thingspeak']['channelID']
                        inidata[item]['thingspeak']['tPort'] = newdata['thingspeak']['tPort']
                        inidata[item]['thingspeak']['mqttHost'] = newdata['thingspeak']['mqttHost']
                        inidata[item]['thingspeak']['THINGSPEAK_HOST'] = newdata['thingspeak']['THINGSPEAK_HOST']
                    elif key == 'topic':
                        inidata[item]['topic']['AC_Topic'] = newdata['topic']['AC_Topic']
                        inidata[item]['topic']['DHT_Topic'] = newdata['topic']['DHT_Topic']
                        inidata[item]['topic']['Ac_Status'] = newdata['topic']['Ac_Status']
                        inidata[item]['topic']['Counter_Topic'] = newdata['topic']['Counter_Topic']
                    elif key == 'broker':
                        inidata['broker']['Broker_IP'] = newdata['broker']['Broker_IP']
                        inidata['broker']['Broker_port'] = newdata['broker']['Broker_port']
                    elif key == 'telegram':
                        inidata['telegram']['Port'] = newdata['telegram']['Port']
                        inidata['telegram']['chatID'] = newdata['telegram']['chatID']
                    elif key == 'dataToRest':
                        inidata['dataToRest']['Host_IP'] = newdata['dataToRest']['Host_IP']
                        inidata['dataToRest']['port'] = newdata['dataToRest']['port']
                else:
                    return




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
