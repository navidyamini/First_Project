//
// Please report any problems with this app template to contact@estimote.com
//

import UIKit
import UserNotifications
import CocoaMQTT

class ViewController: UIViewController, CocoaMQTTDelegate {
    
    let deviceManager = ESTDeviceManager()
    
    let beacon2 = "5c47b10ea18fdc94802bb0177f1318"
    let beacon4 = "dbc3ca355c21e192"
    let beacon5 = "79b1c4d98adf4ed4"
    let beacon6 = "b9c71e98bc32320b7bc9b6446d31342a"
    
    static var telemetryMotionTopic = String()      //"Estimote/TelemetryPackets/motionState"
    var hostIP = String()                           //ip of the broker taken from the web server
    var webServerIP = [String:Any]()                //ip of the web server
    var mqttClient: CocoaMQTT!
    

    //************************************** MQTT *************************************//

    func configureMQTTAndConnect(host:String) {
        let clientID = "iOSTelemetryData-" + String(ProcessInfo().processIdentifier)
        // Replace with the host name for the MQTT Server
        let hostIP = host    //"192.168.43.159" //"192.168.1.110"  //devo sostituirlo con quello di eclipse
        print("\nHOST: \(hostIP)")
        // Replace with the port number for MQTT over TCP (without TLS)
        let port = UInt16(1883)
        mqttClient = CocoaMQTT(clientID: clientID, host: hostIP, port: port)
        mqttClient.username = ""
        mqttClient.password = ""
        mqttClient.keepAlive = 60
        mqttClient.delegate = self
        mqttClient.connect()
    }
    
    //**************************************************************************************//
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //*************************** read  the configuration json file ********************//
        if let path = Bundle.main.url(forResource: "config_file", withExtension: "json") {
            print("\nPATH: \(path)")
            do {
                let jsonData = try Data(contentsOf: path, options: .mappedIfSafe)
                do {
                    if let jsonResult = try JSONSerialization.jsonObject(with: jsonData, options: JSONSerialization.ReadingOptions(rawValue: 0)) as? NSDictionary {
                        webServerIP = jsonResult["beaconWebServer"] as! [String: Any]
                        print("\nThe WEB SERVER IP: \(webServerIP)")
                    }
                } catch let error as NSError {
                    print("Error: \(error)")
                }
            } catch let error as NSError {
                print("Error: \(error)")
            }
        }
        //*********************************************************************************//

        print("\n -URL IS: \(webServerIP["url"] ?? "NO URL FOUND")")

        // Reading the BROKER INFORMATION from json file published in the Web Server
        gettingBrokerInfo.readBrokerInfo(withAPI_url: webServerIP["url"] as! String) { (results:[gettingBrokerInfo]) in
            for result in results {
                //save in the class variable the values taken from the json related to:
                //-Topic,
                //-Broker IP
                ViewController.telemetryMotionTopic = result.topic
                //print("\nTOPIC FROM RESULT: \(result.topic)")
                self.hostIP = result.Broker_IP
                //print("\nHOST IP FROM RESULT: \(self.hostIP)")
                //call of the function used from the MQTT connection to the BROKER
                self.configureMQTTAndConnect(host: self.hostIP)
            }
        }


//*******************    create the content for the notification    ******************//

        
        let motionStateNotification = ESTTelemetryNotificationMotion { (motInfo1) in
            print("\n--beacon ID: \(motInfo1.shortIdentifier), "
                + "MOTION_STATE: \(motInfo1.motionState)")

            var beacon_id = String(motInfo1.shortIdentifier)
            var beaconstring=""
            for character in beacon_id! {
                //print("****************", character)
                beaconstring+=String(character)
            }
            print("- BEACON_IDENTIFIER is: ", beaconstring)
            //let motString = String(motInfo1.shortIdentifier)  //sarà il messagePayload
            
            self.mqttClient.publish(type(of: self).telemetryMotionTopic,
                                    withString: beaconstring, qos: CocoaMQTTQOS.qos0,
                                    retained: false, dup: false)
        }
        deviceManager.register(forTelemetryNotification: motionStateNotification)
 
    }
//***************************  MQTT FUNCTION DECLARATATION   **********************************//
        
    func mqtt(_ mqtt: CocoaMQTT, didConnect host: String, port: Int) {
        // Connection established with the MQTT Server
        print("Connected with MQTT Server \(host):\(port)")
    }
        
    func mqtt(_ mqtt: CocoaMQTT, didConnectAck ack: CocoaMQTTConnAck) {
        // Connection acknowledged
        print("Connection acknowledged \(ack)，rawValue: \(ack.rawValue)")
        if ack == .accept {
            // Subscribe to the motor01StatusTopic topic with QoS 0
            mqtt.subscribe(type(of: self).telemetryMotionTopic, qos: CocoaMQTTQOS.qos0)
        }
    }
        
    func mqtt(_ mqtt: CocoaMQTT, didPublishMessage message: CocoaMQTTMessage, id: UInt16) {
        print("Message published to topic \(message.topic) with payload \(message.string!)")
    }
        
    func mqtt(_ mqtt: CocoaMQTT, didPublishAck id: UInt16) {
        print("Publish acknowledged with id: \(id)")
    }
        
    func mqtt(_ mqtt: CocoaMQTT, didReceiveMessage message: CocoaMQTTMessage, id: UInt16 ) {
        print("Message received in topic \(message.topic) with payload \(message.string!)")
        //if (message.topic == type(of: self).TelemetryDataTopic) {
        //    statusLabel.text = "\(message.string!)"
        //}
    }
        
    func mqtt(_ mqtt: CocoaMQTT, didSubscribeTopic topic: String) {
        print("Subscribed to \(topic)")
    }
        
    func mqtt(_ mqtt: CocoaMQTT, didUnsubscribeTopic topic: String) {
        print("Unsubscribed from \(topic)")
    }
        
    func mqttDidPing(_ mqtt: CocoaMQTT) {
    }
        
    func mqttDidReceivePong(_ mqtt: CocoaMQTT) {
    }
        
    func mqttDidDisconnect(_ mqtt: CocoaMQTT, withError err: Error?) {
        print("Disconnected from the MQTT Server")
    }
        
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
}

