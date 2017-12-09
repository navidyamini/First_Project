import cherrypy
import os
import requests
import json

class SettingThingSpeak(object):
    exposed = True

    def GET(self, *uri):
        try:
            if (uri[0] == "thingspeak"):
                return '''<!DOCTYPE html>
                        <html>
                            <head>
                                <title>Sample Web Form</title>
                                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
                                <script>
                                $(document).ready(function(){
                                    $("input").on({
                                        blur: fucntion(){
                                             $(this).css("background-color", "#ffffff");
                                        }
                                    });
                                });
                                </script>
                            </head>
                        <body>

                        <h1>Museum thingspeak connection settings</h1>
                        <p>please Enter the thingspeak connection info here.</p>

                        <form action="/reply" method="POST">
                            <table>
                                <fieldset>
                                    THINGSPEAK_HOST:<br>
                                    <input type="text" name="THINGSPEAK_HOST1">
                                    <br/>
                                    mqttHost:<br>
                                    <input type="text" name="mqttHost1">
                                    <br/>
                                    tPort:<br>
                                    <input type="text" name="tPort1">
                                    <br/>
                                    channelID:<br>
                                    <input type="text" name="channelID1">
                                    <br/>
                                    tTransport:<br>
                                    <input type="text" name="tTransport1">
                                    <br/>
                                    ACCESS_TOKEN:<br>
                                    <input type="text" name="ACCESS_TOKEN1">
                                    <br/>
                                    READ_API_KEY:<br>
                                    <input type="text" name="READ_API_KEY1">
                                    <br/>
                                </fieldset>
                                <button> Submit </button>
                                <!--input type="submit"-->
                            </table>
                        </form>

                        </body>
                        </html>
                        '''
        except:
            raise KeyError("***** ERROR IN OPENING THE PAGE /thingspeak PLEASE WRITE host:port/thingspeak IN URL*****")
        else:
            return cherrypy.request.body.read()

    def POST(self,*uri, **params):

        try:
            with open("../RawWebpage/initial_data.json", 'r') as json_data_file:
                obj = json.load(json_data_file)

            dict_data = obj['thingspeak']
            obj['thingspeak'] = {"THINGSPEAK_HOST": str(params['THINGSPEAK_HOST1']),
                             "mqttHost": str(params['mqttHost1']),
                             "tPort": str(params['tPort1']),
                             "channelID": str(params['channelID1']),
                             "tTransport": str(params['tTransport1']),
                             "ACCESS_TOKEN": str(params['ACCESS_TOKEN1']),
                             "READ_API_KEY": str(params['READ_API_KEY1'])}

            with open("../RawWebpage/initial_data.json", 'w') as json_data_file:
                json.dump(obj, json_data_file)
        except:
            raise KeyError("***** ERROR IN READING THE JSON FILE*****")
        return '''<!DOCTYPE html>
                    <html>
                        <head>
                            <title>Sample Web Form</title>
                            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
                            <script>
                            $(document).ready(function(){
                                $("input").on({
                                    blur: fucntion(){
                                         $(this).css("background-color", "#ffffff");
                                    }
                                });
                            });
                            </script>
                        </head>
                    <body>

                    <h1>Museum thingspeak connection settings</h1>
                    <p>Successfully Writing the ThingSpeak connection info into the json file.</p>

                    <form action="/reply" method="POST">
                        <table>
                            <fieldset>
                                THINGSPEAK_HOST:<br>
                                <input type="text" name="THINGSPEAK_HOST1">
                                <br/>
                                mqttHost:<br>
                                <input type="text" name="mqttHost1">
                                <br/>
                                tPort:<br>
                                <input type="text" name="tPort1">
                                <br/>
                                channelID:<br>
                                <input type="text" name="channelID1">
                                <br/>
                                tTransport:<br>
                                <input type="text" name="tTransport1">
                                <br/>
                                ACCESS_TOKEN:<br>
                                <input type="text" name="ACCESS_TOKEN1">
                                <br/>
                                READ_API_KEY:<br>
                                <input type="text" name="READ_API_KEY1">
                                <br/>
                            </fieldset>
                            <button> Submit </button>
                            <!--input type="submit"-->
                        </table>
                    </form>

                    </body>
                    </html>
                    '''
if __name__ == "__main__":
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        }
    }
    cherrypy.tree.mount(SettingThingSpeak(), '/', conf)
    cherrypy.server.socket_host = '192.168.1.65'
    cherrypy.engine.start()
    cherrypy.engine.block()