import cherrypy
import os
import requests
import json


class MuseumsWP(object):
    exposed = True

    def GET(self, *uri, **params):
        with open('initial_data.json', 'r') as json_data_file:
            obj = json.load(json_data_file)
        if (uri[0] == "index"):

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

                    <h1>Museum controlling settings</h1>
                    <p>The museum humidity and temperature behaviour is going to work under the following values, or thresholds.
                        Those indicate the allowed temperature and humidity values per an specific art exhibition.</p>

                    <h2>Current thresholds values: </h2>

                    <p id="current_thresholds">
                                            <b id="label_max_temp">''' + "Max. temperature: " + str(obj["thresholds"]["max_temp"]) + '''</b><br>
                                            <b id="label_min_temp">''' + "Min. temperature: " + str(obj["thresholds"]["min_temp"]) + '''</b><br>
                                            <b id="label_max_hum">''' + "Max. humidity: " + str(obj["thresholds"]["max_hum"]) + '''</b><br>
                                            <b id="label_min_hum">''' + "Min. humidity: " + str(obj["thresholds"]["min_hum"]) + '''</b><br>
                                        </p>


                    <form action="/reply" method="POST">
                            Max temperature: <input type="text" name="maxt">
                        <br/>
                        Min temperature: <input type="text" name="mint">
                        <br/>
                        Max humidity: <input type="text" name="maxh">
                        <br/>
                        Min humidity: <input type="text" name="minh">
                        <br/>
                        <button> Submit </button>
                        <!--input type="submit"-->
                    </form>

                    </body>
                    </html>
                    '''

        elif (uri[0] == "maxTemp"):
            return (str(obj["thresholds"]["max_temp"]))
        elif (uri[0] == "minTemp"):
            return (str(obj["thresholds"]["min_temp"]))
        elif (uri[0] == "maxHum"):
            return (str(obj["thresholds"]["max_hum"]))
        elif (uri[0] == "minHum"):
            return (str(obj["thresholds"]["min_hum"]))
        else:
            return cherrypy.request.body.read()

    def POST(self, *uri, **params):
        # obj = cherrypy.request.body.read()

        with open('initial_data.json', 'r') as json_data_file:
            obj = json.load(json_data_file)

        dict_data = obj['thresholds']
        obj['thresholds'] = {"max_temp": float(params['maxt']),
                             "min_temp": float(params['mint']),
                             "max_hum": float(params['maxh']),
                             "min_hum": float(params['minh'])}


        with open('initial_data.json', 'w') as json_data_file:
            json.dump(obj, json_data_file)
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

                    <h1>Museum controlling settings</h1>
                    <p>The museum humidity and temperature behaviour is going to work under the following values, or thresholds.
                        Those indicate the allowed temperature and humidity values per an specific art exhibition.</p>

                    <h2>Current thresholds values: </h2>

                    <p id="current_thresholds">
                                            <b id="label_max_temp">''' + "Max. temperature: " + str(obj["thresholds"]["max_temp"]) + '''</b><br>
                                            <b id="label_min_temp">''' + "Min. temperature: " + str(obj["thresholds"]["min_temp"]) + '''</b><br>
                                            <b id="label_max_hum">''' + "Max. humidity: " + str(obj["thresholds"]["max_hum"]) + '''</b><br>
                                            <b id="label_min_hum">''' + "Min. humidity: " + str(obj["thresholds"]["min_hum"]) + '''</b><br>
                                        </p>


                    <form action="/reply" method="POST">
                        Max temperature: <input type="text" name="maxt">
                        <br/>
                        Min temperature: <input type="text" name="mint">
                        <br/>
                        Max humidity: <input type="text" name="maxh">
                        <br/>
                        Min humidity: <input type="text" name="minh">
                        <br/>
                        <button> Submit </button>
                        <!--input type="submit"-->
                    </form>

                    </body>
                    </html>
                    '''

    def PUT(self, *uri, **params):
        return

    def DELETE(self, *uri, **params):
        return


if __name__ == "__main__":
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        }
    }
    cherrypy.tree.mount(MuseumsWP(), '/', conf)
    cherrypy.server.socket_host = '192.168.1.65'
    cherrypy.server.socket_port = 8081
    cherrypy.engine.start()
    cherrypy.engine.block()
