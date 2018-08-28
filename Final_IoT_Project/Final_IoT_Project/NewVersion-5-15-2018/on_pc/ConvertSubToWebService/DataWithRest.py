import cherrypy
import json
import requests

class DataWithRest(object):

    exposed = True

    def GET(self, *uri, **params):

        try:
            file = open("real_time_data.json", "r")
            json_string = file.read()
            file.close()
        except:
            raise KeyError("***** DataWithRest: ERROR IN READING JSON FILE RELATED TO DATA *****")
        results = json.loads(json_string)

        if(uri[0] == 'temp'):
            return str(results['temperature']['value'])

        elif(uri[0] == 'hum'):
            return str(results['humidity']['value'])

        elif(uri[0] == 'ac'):
            return str(results['AcStatus']['value'])

        elif(uri[0] == 'noPeople'):
            return str(results['bluetoothCounter']['value'])

        elif(uri[0] == 'all'):
            return str(json_string)


if __name__ == '__main__':

    try:
        #file = open("config_file.json", "r") #Navid's Local IP address
        file = open("config_file_xime.json", "r") #Ximena's local IP address
        json_string = file.read()
        file.close()
    except:
        raise KeyError("***** DataWithRest: ERROR IN READING CONFIG FILE *****")

    config_json = json.loads(json_string)
    url = config_json["reSourceCatalog"]["url"]

    respond = requests.get(url)
    json_format = json.loads(respond.text)
    Host_IP = json_format["dataToRest"]["Host_IP"]
    port = json_format["dataToRest"]["port"]

    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }

    cherrypy.tree.mount(DataWithRest(), '/', conf)
    cherrypy.config.update({
        "server.socket_host": Host_IP,
        "server.socket_port": int(port)})
    cherrypy.engine.start()
    cherrypy.engine.block()
