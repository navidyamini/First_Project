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
    file = open("config_file.json", "r")
    json_string = file.read()
    file.close()
    data = json.loads(json_string)
    ip = data["reSourceCatalog"]["ip"]
    port = data["reSourceCatalog"]["port"]
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    cherrypy.tree.mount(MuseumWebService(), '/', conf)
    cherrypy.config.update({
        "server.socket_host": ip,
        "server.socket_port": int(port)})
    cherrypy.engine.start()
    cherrypy.engine.block()
