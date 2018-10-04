using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DataEntry
{
    public partial class Art_Work_Info : Form
    {
        public Art_Work_Info()
        {
            InitializeComponent();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void telegramToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            this.Hide();
            var telegramForm = new Telegram_Form();
            telegramForm.Closed += (s, args) => this.Close();
            telegramForm.Show();
        }

        private void brokerTopicToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            this.Hide();
            var broekrForm = new Broker_Topic_Form();
            broekrForm.Closed += (s, args) => this.Close();
            broekrForm.Show();
        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.Hide();
            var dataEntry = new DataEntryForm();
            dataEntry.Closed += (s, args) => this.Close();
            dataEntry.Show();
        }

        private void btnRead_Click(object sender, EventArgs e)
        {
            comboBoxItems.Items.Clear();
            string json = File.ReadAllText(@"map_beac_paints.json");
            dynamic jsonObj = Newtonsoft.Json.JsonConvert.DeserializeObject(json);
            foreach (var item in jsonObj["roomArtworks"])
            {
                comboBoxItems.Items.Add(item["paint"]);
            }
            MessageBox.Show("File Loaded Successfully");

        }

        private void btnEdit_Click(object sender, EventArgs e)
        {
            if (comboBoxItems.SelectedIndex > -1)
            {
                string item = comboBoxItems.GetItemText(comboBoxItems.SelectedItem);
                string json = File.ReadAllText(@"map_beac_paints.json");
                dynamic jsonObj = Newtonsoft.Json.JsonConvert.DeserializeObject(json);
                foreach (var i in jsonObj["roomArtworks"])
                {
                    if(item.Equals(i["paint"].ToString()))
                    {
                        txtArtisInfo.Text = i["artistInfo"];
                        txtArtist.Text = i["painter"];
                        txtArtWork.Text = i["paint"];
                        txtBecoansId.Text = i["beacon_id"];
                        txtBecoansName.Text = i["beacon_name"];
                        txtDescription.Text = i["description"];
                    }
                }
            }
            else
            {
                MessageBox.Show("Please Select one of The Items");
            }

        }

        private void btnClean_Click(object sender, EventArgs e)
        {
            txtArtisInfo.Text = "";
            txtArtist.Text = "";
            txtArtWork.Text = "";
            txtBecoansId.Text = "";
            txtBecoansName.Text = "";
            txtDescription.Text = "";
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            bool flag = false;
            string item = comboBoxItems.GetItemText(comboBoxItems.SelectedItem);
            string json = File.ReadAllText(@"map_beac_paints.json");
            dynamic jsonObj = Newtonsoft.Json.JsonConvert.DeserializeObject(json);
            if (txtArtWork.Text.Equals("")) {
                MessageBox.Show("Please Enter the Name of the Artwork");
            }
            else{
                foreach (var i in jsonObj["roomArtworks"])
                {
                    if (txtArtWork.Text.Equals(i["paint"].ToString()))
                    {
                        flag = true;
                        i["artistInfo"] = txtArtisInfo.Text.ToString();
                        i["painter"] = txtArtist.Text.ToString();
                        i["paint"] = txtArtWork.Text.ToString();
                        i["beacon_id"] = txtBecoansId.Text.ToString();
                        i["beacon_name"] = txtBecoansName.Text.ToString();
                        i["description"] = txtDescription.Text.ToString();
                        string output = Newtonsoft.Json.JsonConvert.SerializeObject(jsonObj, Newtonsoft.Json.Formatting.Indented);
                        File.WriteAllText(@"map_beac_paints.json", output);
                        MessageBox.Show("Submitted Successfully");
                    }

                }
                if (flag.Equals(false))
                {
                    Dictionary<string, string> newList = new Dictionary<string, string>();
                    newList.Add("artistInfo", txtArtisInfo.Text.ToString());
                    newList.Add("painter", txtArtist.Text.ToString());
                    newList.Add("paint", txtArtWork.Text.ToString());
                    newList.Add("beacon_id", txtBecoansId.Text.ToString());
                    newList.Add("beacon_name", txtBecoansName.Text.ToString());
                    newList.Add("description", txtDescription.Text.ToString());

                    var jsonResponse = JObject.Parse(json);
                    JArray myarray = (JArray)jsonResponse["roomArtworks"];

                    JObject items = new JObject();
                    items.Add(new JProperty("artistInfo", txtArtisInfo.Text.ToString()));
                    items.Add(new JProperty("painter", txtArtist.Text.ToString()));
                    items.Add(new JProperty("paint", txtArtWork.Text.ToString()));
                    items.Add(new JProperty("beacon_id", txtBecoansId.Text.ToString()));
                    items.Add(new JProperty("beacon_name", txtBecoansName.Text.ToString()));
                    items.Add(new JProperty("description", txtDescription.Text.ToString()));
                    myarray.Add(items);
                    jsonResponse["roomArtworks"] = myarray;
                    string output = Newtonsoft.Json.JsonConvert.SerializeObject(jsonResponse, Newtonsoft.Json.Formatting.Indented);
                    File.WriteAllText(@"map_beac_paints.json", output);
                    MessageBox.Show("Submitted Successfully");
                    
                }
            }
        }
    }
}
