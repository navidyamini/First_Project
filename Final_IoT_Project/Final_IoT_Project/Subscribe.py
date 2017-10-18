from MySubscriber import MySubscriber
import json
import time


subscribe =MySubscriber('iot.eclipse.org', 1883, 'sensors/data', 1)
time.sleep(5000)