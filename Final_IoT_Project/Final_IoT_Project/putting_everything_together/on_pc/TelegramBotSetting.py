import cherrypy
import os
import json

class BrokerSetting(object):
    exposed = True

    def GET(self, *uri):
        try:
            if (uri[0] == "telegram"):
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

                        <h1>Museum telegram connection settings</h1>
                        <p>Please enter the telegram connection info here.</p>

                        <form action="/reply" method="POST">
                            <table>
                                <fieldset>
                                    Port:<br>
                                    <input type="text" name="Port1">
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
            raise KeyError("***** ERROR IN OPENING THE PAGE /broker PLEASE WRITE host:port/telegram IN URL*****")
        else:
            return cherrypy.request.body.read()

    def POST(self,*uri, **params):

        try:
            with open("../RawWebpage/initial_data.json", 'r') as json_data_file:
                obj = json.load(json_data_file)

            dict_data = obj['telegram']
            obj['telegram'] = {"Port": str(params['Port1'])}
        except:
            raise KeyError("***** ERROR IN READING THE JSON FILE*****")
        try:
            with open("../RawWebpage/initial_data.json", 'w') as json_data_file:
                json.dump(obj, json_data_file)
        except:
            raise KeyError("***** ERROR IN WRITING THE JSON FILE*****")
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

                    <h1>Museum telegram connection settings</h1>
                    <p>Successfully writing the telegram connection info into the json file.</p>

                    <form action="/reply" method="POST">
                        <table>
                            <fieldset>
                                Port:<br>
                                <input type="text" name="Port1">
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
    cherrypy.tree.mount(BrokerSetting(), '/', conf)
    #cherrypy.server.socket_host = '192.168.1.65'
    cherrypy.config.update({
        "server.socket_host": '192.168.1.65',
        "server.socket_port": 8085})
    cherrypy.engine.start()
    cherrypy.engine.block()