#######################################################
##   Second class that have to SUBSCRIBE data about  ##
##   the status of the LED, and change it            ##
##   to be placed in RASPERRYPI                      ##
#######################################################


import paho.mqtt.client as paho
import RPi.GPIO as GPIO

class Subscriber_LED:

    def on_subscribe(client, userdata, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

        ####controllare se devo fare return
        ### SICURAMENTE DOVR0' METTERE UN __init__ PER VARIABILI ALL'INTERNO DI FUNZIONI

    def on_message(client, userdata, msg):
        print("-->        message received ", str(msg.payload.decode("utf-8")))
        print("-->        message topic=", msg.topic)

        GPIO.setup(17, GPIO.OUT)

        if msg.payload == "HIGH":  #i have to change the status
            GPIO.output(17, GPIO.HIGH)
        elif msg.payload == "LOW":
            GPIO.output(17, GPIO.LOW)


if __name__ == '__main__':

    GPIO.setmode(GPIO.BCM)
    client = paho.Client()
    client.on_subscribe = Subscriber_LED.on_subscribe
    client.on_message = Subscriber_LED.on_message
    client.connect('192.168.1.254', 1883)
    client.subscribe("sensors/led", qos=1)
    client.loop_forever()