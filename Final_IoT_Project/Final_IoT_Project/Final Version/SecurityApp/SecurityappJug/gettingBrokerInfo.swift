//
//  gettingBrokerInfo.swift
//  SecurityappJug
//
//  Created by Carla Corona on 27/09/18.
//  Copyright © 2018 edagroup.polito@gmail.com. All rights reserved.
//

import Foundation

struct gettingBrokerInfo {
    let topic: String
    let Broker_IP: String
    let Broker_port: String
    
    enum SerializationError: Error {
        case missing(String)  //se manca la stringa key
        case invalid(String, Any) //se mancano entrami
    }
    
    init(json:[String:Any]) throws {
        guard let topic = json["topic"] as? String else {
            throw SerializationError.missing("Topic is missing")}
        
        guard let Broker_IP = json["Broker_IP"] as? String else {
            throw SerializationError.missing("Broker_IP is missing")}
        
        guard let Broker_port = json["Broker_port"] as? String else {
            throw SerializationError.missing("Broken_port is missing")}
        
        self.topic = topic
        self.Broker_IP = Broker_IP
        self.Broker_port = Broker_port

    }

    static func readBrokerInfo(withAPI_url API_url:String, completion: @escaping ([gettingBrokerInfo]) -> ()) {

        //print("URL RECEVED: \(url)")
        let url = API_url
        //create the request
        let request = URLRequest(url: URL(string: url)!)
        //create the session
        let task = URLSession.shared.dataTask(with: request) {
            (data:Data?, response:URLResponse?, error: Error?) in
            //create the array to save the info that we read from the json in the web service
            var BrokenInfoArray:[gettingBrokerInfo] = []
            
            if let data = data {
                do {
                    //read the whole json file
                    if let json = try JSONSerialization.jsonObject(with: data, options: []) as? [String:Any] {
                        //print("--- \(json)\n\n")
                        //take the part of the part of the json that im interested in
                        if let data1 = json["broker"] as? [String: Any] {
                            //print("\n BROKER: \(data1)\n")
                            //create the object of type gettingBrokerInfo where we save info
                            if let dataObj = try? gettingBrokerInfo(json: data1) {
                                //print("\n DATAOBJ: \(dataObj)")
                                BrokenInfoArray.append(dataObj)
                            }
                        }
                    }
                } catch {
                    print(error.localizedDescription)
                }
                completion(BrokenInfoArray)
            }
        }
        task.resume()
    }
}

