import cherrypy
import json

class ThresholReader (object):

    exposed = True
    def GET(self, *uri, **params):

        try:
            file = open("../RawWebpage/initial_data.json", "r")
            #print "open"
            json_string = file.read()
            file.close()
        except:
            raise KeyError("***** ERROR IN READING THRESHOLDS JSON FILE *****")
        return json_string

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    # cherrypy.quickstart(WebCalculator(),'/',conf)
    cherrypy.tree.mount(ThresholReader(), '/', conf)
    cherrypy.server.socket_host = '192.168.1.65'
    cherrypy.engine.start()
    cherrypy.engine.block()



