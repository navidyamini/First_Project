//
//  ArtistViewController.swift
//  Ictmuseumproject9S4
//
//  Created by Carla Corona on 27/09/18.
//  Copyright © 2018 edagroup.polito@gmail.com. All rights reserved.
//

import UIKit

class ArtistViewController: UIViewController {

    @IBOutlet weak var artistImage: UIImageView!
    @IBOutlet weak var ArtistLab: UILabel!
    @IBOutlet weak var ArtistDetails: UITextView!
    
    var myLabel = String()
    var myArtistInfo = String()
    var myImage = String()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //here I push the selected content in the different elements inside the second page of the application, related to the information of the artist
        ArtistLab.text = myLabel
        ArtistDetails.text = myArtistInfo
        artistImage.image = UIImage(named: myImage)

    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}
