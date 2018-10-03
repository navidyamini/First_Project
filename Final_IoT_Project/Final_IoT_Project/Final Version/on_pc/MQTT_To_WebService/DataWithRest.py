import cherrypy
import json
import requests
# this web service read the real time data and expose it on the given url

class DataWithRest(object):
    exposed = True

    def GET(self, *uri, **params):
# reading the real time data file when it recives the request

        try:
            file = open("real_time_data.json", "r")
            json_string = file.read()
            item = uri[0]
            file.close()
        except:
            raise KeyError("***** DataWithRest: ERROR IN READING JSON FILE RELATED TO DATA *****")
        results = json.loads(json_string)
       # if the item exist in side the real time data json file it will return the asked data
        if (item == "all"):
            return json_string

        if (item in results):
            if (uri[1] == 'temp'):
                return str(results[item]['temperature']['value'])

            elif (uri[1] == 'hum'):
                return str(results[item]['humidity']['value'])

            elif (uri[1] == 'ac'):
                return str(results[item]['AcStatus']['value'])

            elif (uri[1] == 'noPeople'):
                return str(results[item]['bluetoothCounter']['value'])

            elif (uri[1] == 'all'):
                return str(json.dumps(results[item]))
        else:
            # in case of wrong input it will return this message
            return "Nothing found, check the input again"


if __name__ == '__main__':
# reading the reaource catalog url from the json file
    try:
        file = open("config_file.json", "r")
        json_string = file.read()
        file.close()
    except:
        raise KeyError("***** DataWithRest: ERROR IN READING CONFIG FILE *****")
# sending request to the resource catalog to ask for the MQTT to web service URL
    config_json = json.loads(json_string)
    url = config_json["reSourceCatalog"]["url"]

    respond = requests.get(url + "/dataToRest")
    json_format = json.loads(respond.text)
# set the ip and the port that the mqtt to web service should expose the data on it
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
        "server.socket_host": str(Host_IP),
        "server.socket_port": int(port)})
    cherrypy.engine.start()
    cherrypy.engine.block()
