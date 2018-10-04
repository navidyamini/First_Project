namespace DataEntry
{
    partial class DataEntryForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.dataEntryToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.telegramToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.brokerTopicToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.artWokrsInfoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.exitToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.label1 = new System.Windows.Forms.Label();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.dataEntryToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(423, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // dataEntryToolStripMenuItem
            // 
            this.dataEntryToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.telegramToolStripMenuItem,
            this.brokerTopicToolStripMenuItem,
            this.artWokrsInfoToolStripMenuItem,
            this.exitToolStripMenuItem});
            this.dataEntryToolStripMenuItem.Name = "dataEntryToolStripMenuItem";
            this.dataEntryToolStripMenuItem.Size = new System.Drawing.Size(73, 20);
            this.dataEntryToolStripMenuItem.Text = "Data Entry";
            // 
            // telegramToolStripMenuItem
            // 
            this.telegramToolStripMenuItem.Name = "telegramToolStripMenuItem";
            this.telegramToolStripMenuItem.Size = new System.Drawing.Size(150, 22);
            this.telegramToolStripMenuItem.Text = "Telegram Info";
            this.telegramToolStripMenuItem.Click += new System.EventHandler(this.telegramToolStripMenuItem_Click);
            // 
            // brokerTopicToolStripMenuItem
            // 
            this.brokerTopicToolStripMenuItem.Name = "brokerTopicToolStripMenuItem";
            this.brokerTopicToolStripMenuItem.Size = new System.Drawing.Size(150, 22);
            this.brokerTopicToolStripMenuItem.Text = "Broker Topic";
            this.brokerTopicToolStripMenuItem.Click += new System.EventHandler(this.brokerTopicToolStripMenuItem_Click);
            // 
            // artWokrsInfoToolStripMenuItem
            // 
            this.artWokrsInfoToolStripMenuItem.Name = "artWokrsInfoToolStripMenuItem";
            this.artWokrsInfoToolStripMenuItem.Size = new System.Drawing.Size(150, 22);
            this.artWokrsInfoToolStripMenuItem.Text = "Art Wokrs Info";
            this.artWokrsInfoToolStripMenuItem.Click += new System.EventHandler(this.artWokrsInfoToolStripMenuItem_Click);
            // 
            // exitToolStripMenuItem
            // 
            this.exitToolStripMenuItem.Name = "exitToolStripMenuItem";
            this.exitToolStripMenuItem.Size = new System.Drawing.Size(150, 22);
            this.exitToolStripMenuItem.Text = "Exit";
            this.exitToolStripMenuItem.Click += new System.EventHandler(this.exitToolStripMenuItem_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.Color.Red;
            this.label1.Location = new System.Drawing.Point(9, 129);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(394, 20);
            this.label1.TabIndex = 1;
            this.label1.Text = "Welcome to the Artworks Data Entry Application";
            // 
            // DataEntryForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(423, 332);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "DataEntryForm";
            this.Text = "Data Entry Form";
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem dataEntryToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem telegramToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem brokerTopicToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem artWokrsInfoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem exitToolStripMenuItem;
        private System.Windows.Forms.Label label1;
    }
}