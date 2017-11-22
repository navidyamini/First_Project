# this class is going to count the number of people

import time
import bluetooth

class Bluetooth_Counter(object):
    def __init__(self):
        #for countin the number of bluetooth devices
        self.counter = 0

    def search(self):
        devices = bluetooth.discover_devices(duration=20, lookup_names = True)
        return devices

    def count(self):
        self.counter +=1
        return

    def reset(self):
        self.counter = 0
        return

    def device_counter(self):
        results = self.search()
        if (results!=None):
            for addr, name in results:
                #print the mac address and the name of the device
                print ("{0} - {1}".format(addr, name))
                #increse the counter
                bluetooth_counter.count()
        final_result = self.counter
        self.reset()
        print "number of bluetooth devise is:" + str(final_result)
        return final_result

if __name__=="__main__":
    bluetooth_counter = Bluetooth_Counter()
    while True:
        #results = bluetooth_counter.search()
        #if (results!=None):
            #for addr, name in results:
                #print the mac address and the name of the device
                #print ("{0} - {1}".format(addr, name))
                #increse the counter
                #bluetooth_counter.count()
        # print the nuumber of devices
        #print bluetooth_counter.counter
        bluetooth_counter.device_counter()
        #time.sleep(5)
        #reset the counter to zero for nexrt time
        #bluetooth_counter.reset()
