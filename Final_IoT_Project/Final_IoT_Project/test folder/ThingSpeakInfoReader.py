import cherrypy
import json

class ThingSpeakInfoWriter(object):

    exposed = True

    def GET(self, *uri, **params):

        try:
            file = open("thingSpeakConnectionInfo.json", "r")
            json_string = file.read()
            file.close()
        except:
            raise KeyError("***** ERROR IN READING THINGSPEAK CONNECTION INFO JSON FILE *****")
        return json_string
if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    # cherrypy.quickstart(WebCalculator(),'/',conf)
    cherrypy.tree.mount(ThingSpeakInfoWriter(), '/', conf)
    #cherrypy.server.socket_host = '192.168.1.65'
    cherrypy.config.update({
        "server.socket_host": '192.168.1.65',
        "server.socket_port": 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()


