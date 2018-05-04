
import paho.mqtt.client as paho
import requests
import telepot

url = "https://api.telegram.org/bot371024597:AAGK5je2cAXhyf4oMMD5wcUj1SguoZC5ZOY//sendMessage"
TELEGRAM_TOKEN = '371024597:AAGK5je2cAXhyf4oMMD5wcUj1SguoZC5ZOY'

TELEGRAM_CHAT_ID1='94432957' #Navid

TELEGRAM_CHAT_ID2='351809341' #Carla
#prove differenti fatte per leggere dati telemetry da ESTIMOTE CLOUD
APP_ID = "securityapp-jug"
APP_TOKEN = '8d43562322dbe4fc95737c90f5e551d1'
BEACON_ID = '5c47b10ea18fdc94802bb0177f1318'
moved="test"
'''
def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):
    results = data['result']
    print(results)
    total_updates = len(results) -1
    print(total_updates)
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response
'''

def on_connect(client, userdata, flags, rc):
    client.subscribe("commands/boards/raspberry3/actuators/led01")
    print("\n I'm connected to the MQTT SERVER")
    print("\n- Connection received with code: ", str(rc))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    message = str(msg.payload)
    print(msg.topic + " " + str(msg.qos) + " " + message)
    print("message received ", str(msg.payload.decode("utf-8")))
    moved = str(msg.payload.decode("utf-8"))
    print("message topic=", msg.topic)
    payload1 = {
        'chat_id': TELEGRAM_CHAT_ID1,
        'text': moved,
        'parse_mode': 'HTML'
    }
    payload2 = {
        'chat_id': TELEGRAM_CHAT_ID2,
        'text': moved,
        'parse_mode': 'HTML'
    }
    requests.post("https://api.telegram.org/bot{token}/sendMessage".format(token=TELEGRAM_TOKEN),
                  data=payload1).content
    requests.post("https://api.telegram.org/bot{token}/sendMessage".format(token=TELEGRAM_TOKEN),
                  data=payload2).content

client = paho.Client()
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect('192.168.1.110', 1883, 60)

#chat_id = get_chat_id(last_update(get_updates_json(url)))
#send_mess(chat_id, 'Your message goes here')

#client.subscribe("Estimote/TelemetryPackets/temperature", qos=0)
client.subscribe("Estimote/TelemetryPackets/motionState", qos=0)


##client.subscribe("commands/boards/raspberry3/actuators/led01", qos=0)
client.loop_forever()