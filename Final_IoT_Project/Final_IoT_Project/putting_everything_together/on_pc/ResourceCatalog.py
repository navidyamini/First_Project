import cherrypy
import json
class ResourceCatalog(object):

    exposed = True

    def GET(self, *uri, **params):

        try:
            file = open("../RawWebpage/initial_data.json", "r")
            json_string = file.read()
            file.close()
            item = uri[0]
        except:
            raise KeyError("***** ERROR IN READING JSON FILE RELATED TO RESOURCES *****")
        json_dic = json.loads(json_string)
        if(item in json_dic):
            result = json_dic[item]
            requested_data = json.dumps(result)
            return requested_data
        elif(item=="all"):
            return json_string
        else:
            return"NOTHING FOUNDED, MAKE SURE THAT YOU ARE SENDING THE RIGHT VALUE IN THE URL"
    '''
    def POST(self, *uri, **params):
        try:
            file = open("results.json","r")
            json_string = file.read()
            file.close()
            data = json.loads(json_string)
            if (uri[0]=="thingSpeak"):

                data['thingspeak'] = {"THINGSPEAK_HOST": str(uri[1]),
                             "mqttHost": str(uri[2]),
                             "tPort": str(uri[3]),
                             "channelID": str(uri[4]),
                             "tTransport": str(uri[5]),
                             "ACCESS_TOKEN": str(uri[6]),
                             "READ_API_KEY": str(uri[7])}
                file2 = open("results.json", "w")
                json.dump(data, file2)
                return "Done!"
        except:
            return "Problem in updating file"
    '''
if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    # cherrypy.quickstart(WebCalculator(),'/',conf)
    cherrypy.tree.mount(ResourceCatalog(), '/', conf)
    #cherrypy.server.socket_host = '192.168.43.91'
    #cherrypy.server.socket_port = '8080'
    cherrypy.config.update({
        "server.socket_host": '192.168.43.91',
        "server.socket_port": 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()
