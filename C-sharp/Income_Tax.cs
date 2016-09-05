// Written by: Alvaro Rivas
// File Name: Income_Tax
// Version: MS Visual Studios 2013
// Date: 7/22/15
// Description:
//		Calculates income tax for four different tax payers
//		sorts tax payers in ascending order of income.
// =====================================================================
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Chap9b
{
    class TaxPayerDemo2
    {
        static void Main(string[] args)
        {
            TaxPayer[] user = new TaxPayer[4];
            for (int counter = 0; counter < 4; ++counter)
            {
                user[counter] = new TaxPayer();
                Console.Write("Enter Social Security Number for taxpayer " + (counter +1) + " ");
                user[counter].SocialSecurity = Console.ReadLine();
                Console.Write("Enter Gross income for taxpayer " + (counter + 1) + " ");
                user[counter].GrossIncome = Convert.ToDouble(Console.ReadLine());
            }
            for (int counter = 0; counter < 4; ++counter)
            {
                Console.WriteLine("Taxpayer #" + (counter + 1) + " SSN: " + user[counter].SocialSecurity
                + " income " + user[counter].GrossIncome.ToString("C2")
                + " Tax is " + user[counter].IncomeTax.ToString("C2"));
            }
            Console.WriteLine("\n-------------------------------------------------------");
            Array.Sort(user);
            for (int counter = 0; counter < 4; ++counter)
            {
                Console.WriteLine("Taxpayer #" + (counter + 1) + " SSN: " + user[counter].SocialSecurity
                + " income " + user[counter].GrossIncome.ToString("C2")
                + " Tax is " + user[counter].IncomeTax.ToString("C2"));
            }
            Console.ReadLine();
        }
    }
    class TaxPayer : IComparable
    {
        private double grossIncome;

        private string socialSecurity;

        public double GrossIncome { get { return grossIncome; } set { grossIncome = value; } }
        public string SocialSecurity { get { return socialSecurity; } set { socialSecurity = value; } }
        public double IncomeTax
        {
            get
            {
                if (grossIncome < 30000)
                {
                    return grossIncome * .15;
                }
                else
                {
                    return grossIncome * .28;
                }
            }
        }
        int IComparable.CompareTo(Object o)
        {
            int returnVal;
            TaxPayer temp = (TaxPayer)o;
            if (this.IncomeTax > temp.IncomeTax)
            {
                returnVal = 1;
            }
            else if (this.IncomeTax < temp.IncomeTax)
            {
                returnVal = -1;
            }
            else
            {
                returnVal = 0;
            }
            return returnVal;
        }
    }
}
