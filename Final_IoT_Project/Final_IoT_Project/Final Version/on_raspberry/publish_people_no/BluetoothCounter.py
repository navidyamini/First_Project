# this class is going to count the number of people

import time
import bluetooth

class BluetoothCounter(object):
    def __init__(self):
        #for countin the number of bluetooth devices
        self.counter = 0

    def search(self):
        # searching for the bluetooth devices
        try:
            devices = bluetooth.discover_devices(duration=20, lookup_names = True)
        except:
            print "BleutoothCounter: ERROR IN FINDING THE BLUETOOTH DEVICES"
        return devices

    def count(self):
        self.counter +=1
        return

    def reset(self):
        self.counter = 0
        return

    def device_counter(self):
        results = self.search()
        try:
            if (results!=None):
                for addr, name in results:
                    #print the mac address and the name of the device
                    print ("{0} - {1}".format(addr, name))
                    #   increse the counter
                    self.count()
            final_result = self.counter
            self.reset()
        except:
            print "BLUETOOTHCOUNTER: ERROR IN SENDING THE NUMBER OF BLUETOOTH DEVICES"
        print "number of bluetooth devise is:" + str(final_result)
        return final_result

if __name__=="__main__":
    # this is for testing we call this class in PublishPeopleNo class
    bluetooth_counter = BluetoothCounter()
    while True:
        bluetooth_counter.device_counter()

