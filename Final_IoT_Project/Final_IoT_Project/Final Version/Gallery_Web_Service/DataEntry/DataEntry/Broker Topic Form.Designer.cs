namespace DataEntry
{
    partial class Broker_Topic_Form
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
            this.panel1 = new System.Windows.Forms.Panel();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.btnCansel = new System.Windows.Forms.Button();
            this.btnSave = new System.Windows.Forms.Button();
            this.txtPort = new System.Windows.Forms.TextBox();
            this.txtIp = new System.Windows.Forms.TextBox();
            this.txtTopic = new System.Windows.Forms.TextBox();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.label3);
            this.panel1.Controls.Add(this.label2);
            this.panel1.Controls.Add(this.label1);
            this.panel1.Controls.Add(this.btnCansel);
            this.panel1.Controls.Add(this.btnSave);
            this.panel1.Controls.Add(this.txtPort);
            this.panel1.Controls.Add(this.txtIp);
            this.panel1.Controls.Add(this.txtTopic);
            this.panel1.Location = new System.Drawing.Point(2, 12);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(419, 279);
            this.panel1.TabIndex = 0;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(6, 198);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(60, 13);
            this.label3.TabIndex = 7;
            this.label3.Text = "Broker Port";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(6, 120);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(51, 13);
            this.label2.TabIndex = 6;
            this.label2.Text = "Broker IP";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(6, 50);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(34, 13);
            this.label1.TabIndex = 5;
            this.label1.Text = "Topic";
            // 
            // btnCansel
            // 
            this.btnCansel.Location = new System.Drawing.Point(287, 195);
            this.btnCansel.Name = "btnCansel";
            this.btnCansel.Size = new System.Drawing.Size(89, 23);
            this.btnCansel.TabIndex = 4;
            this.btnCansel.Text = "Cansel";
            this.btnCansel.UseVisualStyleBackColor = true;
            this.btnCansel.Click += new System.EventHandler(this.btnCansel_Click);
            // 
            // btnSave
            // 
            this.btnSave.Location = new System.Drawing.Point(287, 117);
            this.btnSave.Name = "btnSave";
            this.btnSave.Size = new System.Drawing.Size(89, 23);
            this.btnSave.TabIndex = 3;
            this.btnSave.Text = "Save";
            this.btnSave.UseVisualStyleBackColor = true;
            this.btnSave.Click += new System.EventHandler(this.btnSave_Click);
            // 
            // txtPort
            // 
            this.txtPort.Location = new System.Drawing.Point(78, 195);
            this.txtPort.Name = "txtPort";
            this.txtPort.Size = new System.Drawing.Size(136, 20);
            this.txtPort.TabIndex = 2;
            // 
            // txtIp
            // 
            this.txtIp.Location = new System.Drawing.Point(78, 117);
            this.txtIp.Name = "txtIp";
            this.txtIp.Size = new System.Drawing.Size(136, 20);
            this.txtIp.TabIndex = 1;
            // 
            // txtTopic
            // 
            this.txtTopic.Location = new System.Drawing.Point(78, 47);
            this.txtTopic.Name = "txtTopic";
            this.txtTopic.Size = new System.Drawing.Size(298, 20);
            this.txtTopic.TabIndex = 0;
            // 
            // Broker_Topic_Form
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(421, 316);
            this.Controls.Add(this.panel1);
            this.Name = "Broker_Topic_Form";
            this.Text = "Broker Topic Form";
            this.Load += new System.EventHandler(this.Broker_Topic_Form_Load);
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnCansel;
        private System.Windows.Forms.Button btnSave;
        private System.Windows.Forms.TextBox txtPort;
        private System.Windows.Forms.TextBox txtIp;
        private System.Windows.Forms.TextBox txtTopic;
    }
}