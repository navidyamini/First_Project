#######################################################
##   PROVA class that have to SUBSCRIBE data about  ##
##   the status of the LED, and change it            ##
##   to be placed in RASPERRYPI                      ##
#######################################################


import paho.mqtt.client as paho
import RPi.GPIO as GPIO

def on_connect(client, userdata, flags, rc):
    client.subscribe("commands/boards/raspberry3/actuators/led01")
    print("\nI'm connected to the MQTT server")
    print '\nCONNACTION received with code: ' ,str(rc)

def on_subscribe(client, userdata, mid, granted_qos):
    print("\nSubscribed: " + str(mid) )

def on_message(client, userdata, msg):
    message = str(msg.payload)
    print("-->        message received ", message)
    print("-->        message topic=", msg.topic)

    GPIO.setup(17, GPIO.OUT)

    if msg.payload == "TURN ON":  #i have to change the status
        GPIO.output(17, GPIO.HIGH)
    elif msg.payload == "TURN OFF":
        GPIO.output(17, GPIO.LOW)

GPIO.setmode(GPIO.BCM)

client = paho.Client()
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect('192.168.1.254', 1883, 60)
client.subscribe("commands/boards/raspberry3/actuators/led01", qos=0)
client.loop_forever()
