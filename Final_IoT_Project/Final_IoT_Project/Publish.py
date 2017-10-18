from MyPublisher import MyPublisher
import json
import time

test_temp = 30
test_hum = 45
#json_format = json.dumps({"temperature": test_temp, "humidity": test_hum})
json_format = "salam"
print json_format
#while True:
publish = MyPublisher('iot.eclipse.org', 1883, 'sensors/data', str(json_format), 1 )
time.sleep(600)
#message = json.loads(json_format)