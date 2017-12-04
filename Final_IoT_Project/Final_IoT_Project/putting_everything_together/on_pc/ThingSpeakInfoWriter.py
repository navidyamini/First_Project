import cherrypy
import json
""""
THINGSPEAK_HOST = 'mqtt.thingspeak.com'
ACCESS_TOKEN = 'DDNTX8BUX8A17YZG'
channelID = "240810"
tTransport = "websockets"
tPort = 80
mqttHost = "mqtt.thingspeak.com"
READ_API_KEY="PN6SHE0RIBDLGS85"
"""
class ThingSpeakInfoWriter(object):

    exposed = True

    def GET(self, *uri, **params):

        if len(uri) != 7:
            raise KeyError(
                " ***** WRONG INPUT!!! THE INPUT SHOULD BE LIKE 'http://localhost:8080/THINGSPEAK_HOST/ACCESS_TOKEN/channelID/tTransport/tPort/mqttHost/READ_API_KEY.. *****")

        try:
            THINGSPEAK_HOST = (uri[0])
            ACCESS_TOKEN = (uri[1])
            channelID =(uri[2])
            tTransport = (uri[3])
            tPort = (uri[4])
            mqttHost = (uri[5])
            READ_API_KEY = uri[6]
        except:
            raise KeyError("***** THE INPUT'S SHOULD BE 6 variables 'THINGSPEAK_HOST',ACCESS_TOKEN,channelID,tTransport,tPortmqttHost. *****")

        json_string = json.dumps({"THINGSPEAK_HOST": THINGSPEAK_HOST, "ACCESS_TOKEN": ACCESS_TOKEN,"channelID":channelID,
                       "tTransport": tTransport,"tPort":tPort,"mqttHost":mqttHost,"READ_API_KEY":READ_API_KEY})
        try:
            file = open("thingSpeakConnectionInfo.json", "w")
            file.write(json_string)
            file.close()
        except:
            raise KeyError("***** ERROR IN WRITNG JSON FILE. *****")
        return open('ThingSpeakWriteResult.html', 'r').read()

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    # cherrypy.quickstart(WebCalculator(),'/',conf)
    cherrypy.tree.mount(ThingSpeakInfoWriter(), '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()


