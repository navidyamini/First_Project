
import cherrypy
import json
import temp_hum

class MyClass(object):

    def GET(self, *uri):
        if uri[0]=='temperature':
            temp_hum.MyFirstSensor()
            

        elif uri[0]=='humidity':
            pass

        elif uri[0]=='relay':
            pass
        
        else:
            print("Insert valid operation")
