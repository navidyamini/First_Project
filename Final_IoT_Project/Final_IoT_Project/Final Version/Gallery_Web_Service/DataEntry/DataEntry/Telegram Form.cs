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
    public partial class Telegram_Form : Form
    {
        public Telegram_Form()
        {
            InitializeComponent();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void brokerTopicToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Hide();
            var broekrForm = new Broker_Topic_Form();
            broekrForm.Closed += (s, args) => this.Close();
            broekrForm.Show();


        }

        private void artWokrsInfoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Hide();
            var artForm = new Art_Work_Info();
            artForm.Closed += (s, args) => this.Close();
            artForm.Show();

        }

        private void Telegram_Form_Load(object sender, EventArgs e)
        {
            string json = File.ReadAllText("map_beac_paints.json");
            dynamic jsonObj = Newtonsoft.Json.JsonConvert.DeserializeObject(json);
            string port = jsonObj["telegram"]["Port"];
            string chatId = jsonObj["telegram"]["chatID"];
            txtPort.Text = port;
            txtChatId.Text = chatId;
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            string json = File.ReadAllText("map_beac_paints.json");
            dynamic jsonObj = Newtonsoft.Json.JsonConvert.DeserializeObject(json);
            jsonObj["telegram"]["Port"] = txtPort.Text.ToString();
            jsonObj["telegram"]["chatID"] = txtChatId.Text.ToString();
            string output = Newtonsoft.Json.JsonConvert.SerializeObject(jsonObj, Newtonsoft.Json.Formatting.Indented);
            File.WriteAllText("map_beac_paints.json", output);
            MessageBox.Show("Submitted Successfully");
            this.Hide();
            var dataEntry = new DataEntryForm();
            dataEntry.Closed += (s, args) => this.Close();
            dataEntry.Show();
        }

        private void btnCansel_Click(object sender, EventArgs e)
        {
            this.Hide();
            var dataEntry = new DataEntryForm();
            dataEntry.Closed += (s, args) => this.Close();
            dataEntry.Show();
        }
    }
}
