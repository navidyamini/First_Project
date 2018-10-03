//
//  Artwork.swift
//  Ictmuseumproject9S4
//
//  Created by Carla Corona on 14/09/18.
//  Copyright © 2018 edagroup.polito@gmail.com. All rights reserved.
//

import Foundation

struct Artwork {
    let beacon_id: String
    let beacon_name: String
    let paint: String
    let painter: String
    let description: String
    let artistInfo: String
    
    enum SerializationError: Error {
        case missing(String)  //se manca la stringa key
        case invalid(String, Any) //se mancano entrami
    }
    
    init(json:[String:Any]) throws {
        guard let beacon_id = json["beacon_id"] as? String else {
            throw SerializationError.missing("Summary is missing")}
        
        guard let beacon_name = json["beacon_name"] as? String else {
            throw SerializationError.missing("Icon is missing")}
        
        guard let paint = json["paint"] as? String else {
            throw SerializationError.missing("Paint is missing")}
        
        guard let painter = json["painter"] as? String else {
            throw SerializationError.missing("Painter is missing")}
        
        guard let description = json["description"] as? String else {
            throw SerializationError.missing("Description is missing")}
        
        guard let artistInfo = json["artistInfo"] as? String else {
            throw SerializationError.missing("ArtistInfo is missing")}
        
        self.beacon_id = beacon_id
        self.beacon_name = beacon_name
        self.paint = paint
        self.painter = painter
        self.description = description
        self.artistInfo = artistInfo
    }

    static func takeArtworksData(withAPI_url API_url:String, completion: @escaping ([Artwork]) -> ()) {
        
        let url = API_url
        print("TAKEN URL: \(url)")
        
        // Then I will create the request and the session to allowing the app to take the information that it needs from the museum web Service
        let request = URLRequest(url: URL(string: url)!)
        
        let task = URLSession.shared.dataTask(with: request) {
            (data:Data?, response:URLResponse?, error: Error?) in
            
            var artworksArray:[Artwork] = []
            
            if let data = data {
                do {
                    if let json = try JSONSerialization.jsonObject(with: data, options: []) as? [String:Any] {
                        if let data1 = json["roomArtworks"] as? [[String: Any]] {
                            for dataPoint in data1 {
                                if let dataObj = try? Artwork(json: dataPoint) {
                                    artworksArray.append(dataObj)
                                }
                            }
                        }
                    }
                } catch {
                    print(error.localizedDescription)
                }
                completion(artworksArray)
            }
        }
        task.resume()
    }
}

