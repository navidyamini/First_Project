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
    public partial class Broker_Topic_Form : Form
    {
        public Broker_Topic_Form()
        {
            InitializeComponent();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void artWokrsInfoToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            this.Hide();
            var artForm = new Art_Work_Info();
            artForm.Closed += (s, args) => this.Close();
            artForm.Show();
        }

        private void telegramToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            this.Hide();
            var telegramForm = new Telegram_Form();
            telegramForm.Closed += (s, args) => this.Close();
            telegramForm.Show();
        }

        private void btnCansel_Click(object sender, EventArgs e)
        {
            this.Hide();
            var dataEntry = new DataEntryForm();
            dataEntry.Closed += (s, args) => this.Close();
            dataEntry.Show();
        }

        private void Broker_Topic_Form_Load(object sender, EventArgs e)
        {
            string json = File.ReadAllText("map_beac_paints.json");
            dynamic jsonObj = Newtonsoft.Json.JsonConvert.DeserializeObject(json);
            string topic = jsonObj["broker"]["topic"];
            string ip = jsonObj["broker"]["Broker_IP"];
            string port = jsonObj["broker"]["Broker_port"];
            txtTopic.Text = topic;
            txtIp.Text = ip;
            txtPort.Text = port;
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            string json = File.ReadAllText("map_beac_paints.json");
            dynamic jsonObj = Newtonsoft.Json.JsonConvert.DeserializeObject(json);
            jsonObj["broker"]["topic"] = txtTopic.Text.ToString();
            jsonObj["broker"]["Broker_IP"] = txtIp.Text.ToString();
            jsonObj["broker"]["Broker_port"] = txtPort.Text.ToString();
            string output = Newtonsoft.Json.JsonConvert.SerializeObject(jsonObj, Newtonsoft.Json.Formatting.Indented);
            File.WriteAllText("map_beac_paints.json", output);
            MessageBox.Show("Submitted Successfully");
            this.Hide();
            var dataEntry = new DataEntryForm();
            dataEntry.Closed += (s, args) => this.Close();
            dataEntry.Show();
        }
    }
}
