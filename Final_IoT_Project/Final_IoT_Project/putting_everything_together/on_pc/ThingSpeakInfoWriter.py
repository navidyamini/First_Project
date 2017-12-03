import cherrypy
import json

class ThingSpeakInfoWriter(object):

    exposed = True

    def GET(self, *uri, **params):

        if len(uri) != 6:
            raise KeyError(
                " ***** WRONG INPUT!!! THE INPUT SHOULD BE LIKE 'http://localhost:8080/THINGSPEAK_HOST/ACCESS_TOKEN/channelID/tTransport/tPort/mqttHost.. *****")

        try:
            THINGSPEAK_HOST = (uri[0])
            ACCESS_TOKEN = (uri[1])
            channelID =(uri[2])
            tTransport = (uri[3])
            tPort = (uri[4])
            mqttHost = (uri[5])
        except:
            raise KeyError("***** THE INPUT'S SHOULD BE 6 variables 'THINGSPEAK_HOST',ACCESS_TOKEN,channelID,tTransport,tPortmqttHost. *****")

        json_string = json.dumps({"THINGSPEAK_HOST": THINGSPEAK_HOST, "ACCESS_TOKEN": ACCESS_TOKEN,"channelID":channelID,
                       "tTransport": tTransport,"tPort":tPort,"mqttHost":mqttHost})
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


