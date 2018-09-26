import cherrypy
import json
class MuseumWebService(object):

    exposed = True

    def GET(self, *uri, **params):

        try:
            file = open("map_beac_paints.json", "r")
            json_str = file.read()
            file.close()
            return json_str
        except:
            raise KeyError("***** ERROR IN READING JSON FILE RELATED TO RESOURCES *****")

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    # cherrypy.quickstart(WebCalculator(),'/',conf)
    cherrypy.tree.mount(MuseumWebService(), '/', conf)
    #cherrypy.server.socket_host = '192.168.1.65'
    #cherrypy.server.socket_port = '8080'
    cherrypy.config.update({
        "server.socket_host": '192.168.43.91',
        "server.socket_port": 8082})
    cherrypy.engine.start()
    cherrypy.engine.block()
