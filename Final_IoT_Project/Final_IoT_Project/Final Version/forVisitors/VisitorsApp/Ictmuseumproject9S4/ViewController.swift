//
// Please report any problems with this app template to contact@estimote.com
//

import UIKit
import UserNotifications

class ViewController: UIViewController, ProximityContentManagerDelegate {

    @IBOutlet weak var label: UILabel!
    @IBOutlet weak var image: UIImageView!
    @IBOutlet weak var activityIndicator: UIActivityIndicatorView!

    var proximityContentManager: ProximityContentManager!

    var current: String?
    var indexMoreInfo = 0
    var artDict = [String: Artwork]()
    var labArtist: String = ""
    var labArtwork = String()
    var artworkdescription = String()
    var artistInfo = String()
    var beacon_name = String()
    
    var webServerIP = [String:Any]()
    
    override func viewDidLoad() {
        super.viewDidLoad()

        self.activityIndicator.startAnimating()

        self.proximityContentManager = ProximityContentManager(
            beaconIDs: [
                BeaconID(UUIDString: "BB773F73-C6FB-5296-E10C-DDFB2E636E9D", major: 22059, minor: 23019),//smartgallery2
                BeaconID(UUIDString: "2E943AB5-563C-42D3-A1A0-5D196861BCD5", major: 38351, minor: 30050),//smartgallery6
                BeaconID(UUIDString: "C2D67E24-6CE3-4FC8-A18D-E6C5F6DFF2FD", major: 31678, minor: 38921),//smartgallery5
                BeaconID(UUIDString: "FAE21757-182E-4262-8DEE-6EF880DF2D89", major: 1710, minor: 13858)//smartgallery4
            ],
            beaconContentFactory: CachingContentFactory(beaconContentFactory: BeaconDetailsCloudFactory()))
        self.proximityContentManager.delegate = self
        self.proximityContentManager.startContentUpdates()
        
        //******************** Reading JSON of the CONFIGURATION FILE

        if let path = Bundle.main.url(forResource: "config_file", withExtension: "json") {
            do {
                let jsonData = try Data(contentsOf: path, options: .mappedIfSafe)
                do {
                    if let jsonResult = try JSONSerialization.jsonObject(with: jsonData, options:  JSONSerialization.ReadingOptions(rawValue: 0)) as? NSDictionary {
                        //Taking the value of the IP where we will read from the config_file
                        webServerIP = jsonResult["beaconWebServer"] as! [String: Any]
                    }
                } catch let error as NSError {
                    print("Error: \(error)")
                }
            } catch let error as NSError {
                print("Error: \(error)")
            }
        }
        //***********************************
        
        print("\n- URL IS: \(webServerIP["url"] ?? "NO VALUE")")
        
        //************ Calling the function that takes the data of the artworks from the Web Service 
        
        Artwork.takeArtworksData(withAPI_url: webServerIP["url"] as! String) { (results:[Artwork]) in
            for result in results {
                print(result.beacon_name)
                self.artDict[result.beacon_name] = result
                //print("\(result)\n\n")
            }
            print("\nLABEL: \(self.labArtist), \(self.labArtwork)")
        }
    }

    // Showing the information in relaton of the Beacon you are in front of
    func proximityContentManager(_ proximityContentManager: ProximityContentManager, didUpdateContent content: AnyObject?) {
        
        self.activityIndicator?.stopAnimating()
        self.activityIndicator?.removeFromSuperview()

        // Here we recall the functions related to the discovery or miss discovery of the beacons
        if let beaconDetails = content as? BeaconDetails {
            showBeaconFounded(beaconDetails: beaconDetails)
            print("\n BEACON: \(beaconDetails.beaconName)")
        } else {
            noBeaconFounded()
        }
    }

    override var preferredStatusBarStyle : UIStatusBarStyle {
        return .lightContent
    }

    // This is the function that i use when i found the beacon setting the relative values that i want to use later
    func showBeaconFounded(beaconDetails: BeaconDetails){
        self.beacon_name = beaconDetails.beaconName
        self.image.isHidden = false
       
        self.image.image = UIImage.init(named: beaconDetails.beaconName)
        self.labArtist = self.artDict[beaconDetails.beaconName]!.painter
        self.artworkdescription = self.artDict[beaconDetails.beaconName]!.description
        self.labArtwork = self.artDict[beaconDetails.beaconName]!.paint
        self.artistInfo = self.artDict[beaconDetails.beaconName]!.artistInfo
        
        self.label.text = "\(self.labArtwork), \(self.labArtist)"
        
        self.current = beaconDetails.beaconName
    }
    // Function for when I don't find the beacon
    func noBeaconFounded(){
        self.image.isHidden = false
        self.image.image = nil
        self.label.text = "BEACONS NOT FOUNDED, RETURN IN THE RANGES"
    }
    
    // Function that allows the setting of the following page after the touch of the button MORE INFO, withe the information about the artwork itself
    @IBAction func moreInfoTapped(_ sender: Any) {
        if labArtwork != "" {
            performSegue(withIdentifier: "segueArtwork", sender: self)
        }
    }
    // Function that allows the setting of the following page after the touch of the button ARTIST INFO, withe the information about the artist himself
    @IBAction func artistInfoTapped(_ sender: Any) {
        if labArtist != "" {
            performSegue(withIdentifier: "segueArtist", sender: self)
        }
    }
    
    // This function allows to define the contents of the following pages of the app, based on the values that we red from the json file in the web service and consequently set them basing on the beacon's range in which we entered
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        
        // Here I set the values for the element inside the Artwork page
        if segue.destination is ArtworkViewController
        {
            let artworkController = segue.destination as! ArtworkViewController
            artworkController.myLabel = self.labArtwork
            artworkController.myDescription = self.artworkdescription
            artworkController.myImage = self.beacon_name
        }
            
        // Here I set the values for the element inside the Artist page
        else if segue.destination is ArtistViewController
        {
            let artistController = segue.destination as! ArtistViewController
            artistController.myLabel = self.labArtist
            artistController.myArtistInfo = self.artistInfo
            artistController.myImage = self.labArtist

        }
        
    }
    
    
}
