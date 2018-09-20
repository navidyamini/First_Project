import cherrypy
import json
import requests

class DataWithRest(object):

    exposed = True

    def GET(self, *uri, **params):

        try:
            file = open("real_time_data.json", "r")
            json_string = file.read()
            room_id = uri[0]
            file.close()
        except:
            raise KeyError("***** DataWithRest: ERROR IN READING JSON FILE RELATED TO DATA *****")
        results = json.loads(json_string)
        if (room_id in results):
            if(uri[1] == 'temp'):
                return str(results[room_id]['temperature']['value'])

            elif(uri[1] == 'hum'):
                return str(results[room_id]['humidity']['value'])

            elif(uri[1] == 'ac'):
                return str(results[room_id]['AcStatus']['value'])

            elif(uri[1] == 'noPeople'):
                return str(results[room_id]['bluetoothCounter']['value'])

            elif(uri[1] == 'all'):
                return str(results[room_id])


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
    Host_IP = json_format["Host_IP"]
    port = json_format["port"]

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
