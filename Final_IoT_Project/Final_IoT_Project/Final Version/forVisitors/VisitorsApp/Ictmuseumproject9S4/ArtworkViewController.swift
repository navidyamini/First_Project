//
//  ArtworkViewController.swift
//  Ictmuseumproject9S4
//
//  Created by Carla Corona on 27/09/18.
//  Copyright © 2018 edagroup.polito@gmail.com. All rights reserved.
//

import UIKit

class ArtworkViewController: UIViewController {

    @IBOutlet weak var artworkImage: UIImageView!
    @IBOutlet weak var ArtworkLab: UILabel!
    @IBOutlet weak var ArtworkDetails: UITextView!
    
    var myLabel = String()
    var myDescription = String()
    var myImage = String()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //here I push the selected content in the different elements inside the second page of the application, related to the information of the artworks
        ArtworkLab.text = myLabel
        ArtworkDetails.text = myDescription
        print("\n DESCRIPTION: \(ArtworkDetails.text)\n")
        artworkImage.image  = UIImage(named: myImage)!
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}
