import cherrypy

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
if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    # cherrypy.quickstart(WebCalculator(),'/',conf)
    cherrypy.tree.mount(ResourceCatalog(), '/', conf)
    cherrypy.server.socket_host = '192.168.1.65'
    cherrypy.server.socket_port = '8080'
    cherrypy.engine.start()
    cherrypy.engine.block()
