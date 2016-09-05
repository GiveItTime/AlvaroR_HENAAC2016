// Written by: Alvaro Rivas
// File Name: PC_Store
// Date: 8/2/15
// Version: MS Visual Studios 2013
// Description:
//		Computer Store text box window, uses a combination of buttons and check 
//		boxes to calculate the total purchase price.
// ============================================================================================
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Final
{
    public partial class Form1 : Form
    {
        private double total = 0;// stores running total
        public Form1()
        {
            InitializeComponent();
        }
        // Listener: If Acer is selected add $700 to total, un-selected subtract $700 from total
        private void AcerButton_CheckedChanged(object sender, EventArgs e)
        {
            const double ACER = 700;
            if (AcerButton.Checked)
            {
                total += ACER;
            }
            else
            {
                total -= ACER;
            }
        }
        // Listener: If HP is selected add $1250 to total, un-selected subtract $1250 from total
        private void HPButton_CheckedChanged(object sender, EventArgs e)
        {
            const double HP = 1250;
            if (HPButton.Checked)
            {
                total += HP;
            }
            else
            {
                total -= HP;
            }
        }
        // Listener: If Sony is selected add $1500 to total, un-selected subtract $1500 from total
        private void SonyButton_CheckedChanged(object sender, EventArgs e)
        {
            const double SONY = 1500;
            if (SonyButton.Checked)
            {
                total += SONY;
            }
            else
            {
                total -= SONY;
            }
        }
        // Listener: If Calculate Total button clicked display current total
        private void TotalButton_Click(object sender, EventArgs e)
        {
            TotalLabel.Text = "Total is " + total.ToString("C2");
        }
        // Listener: If Hard Drive checked add $50 to total, unchecked subtract $50 from total
        private void HardDriveCheckBox_CheckedChanged(object sender, EventArgs e)
        {
            const double HARDDRIVE = 50;
            if (HardDriveCheckBox.Checked)
            {
                total += HARDDRIVE;
            }
            else
            {
                total -= HARDDRIVE;
            }
        }
        // Listener: If External Drive checked add $75 to total, unchecked subtract $75 from total
        private void ExternalDriveCheckBox_CheckedChanged(object sender, EventArgs e)
        {
            const double EXTERNALDRIVE = 75;
            if (ExternalDriveCheckBox.Checked)
            {
                total += EXTERNALDRIVE;
            }
            else
            {
                total -= EXTERNALDRIVE;
            }
        }
        // Listener: If Internal Blu Ray ROM checked add $70 to total, unchecked subtract $70 from total
        private void InternalBluRayheckBox_CheckedChanged(object sender, EventArgs e)
        {
            const double INTERNALBLURAY = 70;
            if (InternalBluRayCheckBox.Checked)
            {
                total += INTERNALBLURAY;
            }
            else
            {
                total -= INTERNALBLURAY;
            }
        }
    }
}
