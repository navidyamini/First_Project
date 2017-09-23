from __future__ import print_function
import paho.mqtt.publish as publish
import psutil

# The ThingSpeak Channel ID
# Replace <YOUR-CHANNEL-ID> with your channel ID
channelID = "240810"

# The Write API Key for the channel
# Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key
apiKey = "DDNTX8BUX8A17YZG"

# The Hostname of the ThinSpeak MQTT broker
mqttHost = "mqtt.thingspeak.com"

#Define the connection type as websockets, and set the port to 80.
tTransport = "websockets"
tPort = 80

#Create the topic string of the form shown in Publish to a Channel
# Feed to update field 1 and field 2 of the specified channel simultaneously.
# Create the topic string
topic = "channels/" + channelID + "/publish/" + apiKey

#Run a loop that calculates the system RAM and CPU performance every 20 seconds
# and publishes these values tofields 1 and 2 of the specified channel
# simultaneously using websockets.
while (1):

    # get the system performance data
    cpuPercent = psutil.cpu_percent(interval=20)
    ramPercent = psutil.virtual_memory().percent

    print(" CPU =", cpuPercent, "   RAM =", ramPercent)

    # build the payload string
    payload = "field1=" + str(cpuPercent) + "&field2=" + str(ramPercent)

    # attempt to publish this data to the topic
    try:
        publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort)

    except (KeyboardInterrupt):
        break

    except:
        print("There was an error while publishing the data.")

