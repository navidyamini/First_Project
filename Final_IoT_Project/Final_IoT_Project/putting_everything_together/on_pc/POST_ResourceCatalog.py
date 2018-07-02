import cherrypy
import json

class ResourceCatalog(object):

    exposed = True

    def GET(self, *uri, **params):

        try:
            file = open("../RawWebpage/initial_data.json", "r")
            json_string = file.read()
            file.close()
        except:
            raise KeyError("***** ERROR IN READING JSON FILE RELATED TO RESOURCES *****")
        return json_string

    def POST(self, *uri, **params):
        try:
            with open("../RawWebpage/initial_data.json", "r") as idata:
                inidata = json.loads(idata.read())
                data = cherrypy.request.body.read()
                newdata = json.loads(data)

                print data
                print inidata
                print newdata
                key = list(newdata.keys())[0]



                if key =='thresholds':

                    inidata['thresholds']['min_hum'] = newdata['thresholds']['min_hum']
                    inidata['thresholds']['min_temp'] = newdata['thresholds']['min_temp']
                    inidata['thresholds']['max_temp'] = newdata['thresholds']['max_temp']
                    inidata['thresholds']['max_hum'] = newdata['thresholds']['max_hum']
                elif key=='thingspeak':
                    inidata['thingspeak']['READ_API_KEY'] = newdata['thingspeak']['READ_API_KEY']
                    inidata['thingspeak']['ACCESS_TOKEN'] = newdata['thingspeak']['ACCESS_TOKEN']
                    inidata['thingspeak']['tTransport'] = newdata['thingspeak']['tTransport']
                    inidata['thingspeak']['channelID'] = newdata['thingspeak']['channelID']
                    inidata['thingspeak']['tPort'] = newdata['thingspeak']['tPort']
                    inidata['thingspeak']['mqttHost'] = newdata['thingspeak']['mqttHost']
                    inidata['thingspeak']['THINGSPEAK_HOST'] = newdata['thingspeak']['THINGSPEAK_HOST']
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
