#####################################################
##   Fourth class that have to PUBLISH data about  ##
##   the status of the LED                         ##
##   to be placed in PC                            ##
#####################################################

import paho.mqtt.client as mqttc

class Third_Client:

    def __init__(self, status_led):
        self.status_led = status_led

    def select_status_led(self):

        if self.status_led==1:
            final_status="HIGH"
            print "I'm changing the status of the LED..."

        elif self.status_led==0:
            final_status = "LOW"
            print "I'm not changing the status of the LED!"

        else:
            print "Insert a valid option..."


        return final_status

    def publish_status_led(self):
        (rc, mid) = client.publish('sensors/led', str(status), qos=1)
        print "\nI publish the LED status with code: ", rc  #

    def on_connect(client, userdata, flags, rc):
        print '\nCONNACTION received with code: ' ,str(rc)

    def on_publish(client, userdata, mid):
        print("mid: " + str(mid))

if __name__ == '__main__':

    print "Do you want to turn on the LED?\n" \
          "PRESS:\n" \
          "1) yes\n" \
          "0) no"
    stat_led = input("->")

    status = Third_Client(stat_led)

    client = mqttc.Client()
    client.on_connect = Third_Client.on_connect
    client.on_publish = Third_Client.on_publish
    client.connect('192.168.1.254', 1883)
    client.loop_start()

    status.publish_status_led()
    # (rc, mid) = client.publish('sensors/led', str(status), qos = 1)
    # print "\nI publish the LED status with code: ", rc #