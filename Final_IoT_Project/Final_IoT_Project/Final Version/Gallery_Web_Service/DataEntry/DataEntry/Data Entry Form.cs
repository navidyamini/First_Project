using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DataEntry
{
    public partial class DataEntryForm : Form
    {
        public DataEntryForm()
        {
            InitializeComponent();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void telegramToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Hide();
            var telegramForm = new Telegram_Form();
            telegramForm.Closed += (s, args) => this.Close();
            telegramForm.Show();

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
    }
}
