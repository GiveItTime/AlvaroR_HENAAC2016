// ================================================================================
// Author: Alvaro Rivas
// Date Due: 9/9/15
// Compiler: Visual Studios 2012
// Description:
//		Program Calculates Horsepower or Quarter mile time depending on selection.
//		Stores information about vehicle and displays it, max of six vehicles.
// =================================================================================
#include <iostream>
#include <cmath>
#include <cstring>
#include <iomanip>
using namespace std;

class Car
{
	// Private Stucture
	struct VehicleInfo
	{
		// Structure Variables
		char vehicleName[30];
		double vehicleWeight;
		double quarterMileTime;
		double horsePower;
	};

	int index;
	//Array of 6 Structures
	VehicleInfo vehicleArray[6];

	public:
		// Constructor initializes index to zero
		Car(){ index = 0;}
		// accessor function that increments private member index when called
		void IndexIncrement();
		// accessor function that copies name to structure variable
		void SetName(char name[]);
		// accessor function assigns weight to structure variable
		void SetVehicleWeight(double weight);
		// accessor function assigns time to structure variable
		void SetTime(double time);
		// accessor function assigns horsepower to structure variable
		void SetHorsePower(double hp);
		// accessor function Calculates horsepower and assigns it to structure variable
		void CalcHorsePower();
		// accessor function Calculates time and assigns it to structure variable
		void CalcTime();
		// accessor function that display structure variables
		void Display();

};


		// accessor function that increments private member index when called
		void Car::IndexIncrement(){++index;}
		// accessor function that copies name to structure variable
		void Car::SetName(char name[]){strncpy_s(vehicleArray[index].vehicleName,name,30);}
		// accessor function assigns weight to structure variable
		void Car::SetVehicleWeight(double weight){ vehicleArray[index].vehicleWeight = weight;}
		// accessor function assigns time to structure variable
		void Car::SetTime(double time){ vehicleArray[index].quarterMileTime = time;}
		// accessor function assigns horsepower to structure variable
		void Car::SetHorsePower(double hp){ vehicleArray[index].horsePower = hp;}
		// accessor function Calculates horsepower and assigns it to structure variable
		void Car::CalcHorsePower()
		{
			double temp = vehicleArray[index].quarterMileTime/5.825;
			vehicleArray[index].horsePower = vehicleArray[index].vehicleWeight/pow(temp,3);
		}
		// accessor function Calculates time and assigns it to structure variable
		void Car::CalcTime()
		{
			double temp = vehicleArray[index].vehicleWeight/vehicleArray[index].horsePower;
			double cubeRoot = pow(temp,.333);
			vehicleArray[index].quarterMileTime = (5.825 * cubeRoot);
		}
		// accessor function that display structure variables
		void Car::Display()
		{
			// Cycles through array list so that it can display each individual variable in structure VehicleInfo
			for(int counter = 0; counter <= index; ++counter)
			{

				cout << "Vehicle Name: " << vehicleArray[counter].vehicleName << endl;
				// Output is set to the second decimal place
				cout << "Vehicle Weight: " << setprecision(2) << fixed << vehicleArray[counter].vehicleWeight << endl;
				// Output is set to the first decimal place
				cout << "Quarter Mile Time: " << setprecision(1) << fixed << vehicleArray[counter].quarterMileTime << endl;
				cout << "Horse Power: " << setprecision(1) << fixed <<vehicleArray[counter].horsePower << endl << endl;
				
			}
		}


int main(void)
{
	// Local Variables
	char menu, subMenu, name[30];
	double weight, time, horsepower;
	int counter = 0;
	bool quit = true;

	// Variable of type Car, gives access to Class Car
	Car vehicle;
	// do while loop, will continue prompting user until user enters Q to quit
	do{
		//Prompts User for main menu selection and sub-menu selection
		cout << "Main Menu:\nPlease Select a Main Menu option:\nH) Calculates HorsePower T} Calculates Quarter Mile Time:"; 
		cin >> menu;
		// if Invalid selection, assigns menu a default selection
		if( (toupper(menu) != 'H') &&  (toupper(menu) != 'T'))
		{
			cout << "You've selected an invalid option, will Calculate Horsepower as default" << endl;
			menu = 'H';
		}
		cout << "Sub-Menu:\n Please Enter a Sub-Menu option\n(E)nter a vehicle data\n(D)isplay all vehicles in the database\n(Q)uit\nEnter Selection:";
		cin >> subMenu;
		// Checks if menu selection matches available options
		switch (toupper(menu))
		{
		case 'H':
			switch (toupper(subMenu))
			{
			case 'E':
				// if not entering sub-menu for first time and not out of array bounds increment Vehicle Array index
				if((counter != 0) && (counter < 6))
				{
					vehicle.IndexIncrement();
				}
				// if array bounds has been reached display message to user
				else if(counter > 5)
				{
					cout << " Vehicle Array is Full, will continue to replace last entry\n";
				}
				// Prompts user for information
				cout << "Enter vehicle name: ";
				cin >> name;
				cout << "Enter weight: ";
				cin >> weight;
				cout << "Enter quarter mile time: ";
				cin >> time;
				// Calls Accessor Functions
				vehicle.SetName(name);
				vehicle.SetVehicleWeight(weight);
				vehicle.SetTime(time);
				vehicle.CalcHorsePower();
				// Increments counter everytime 'E' is selected
				++counter;
				break;
			case 'D':
				// Calls Accessor Functions
				vehicle.Display();
				break;
			case 'Q':
				// ends do while loop
				quit = false;
				break;
			default:
				cout << "Invalid Selection returning to Main Menu\n";
			}
			break;
		case 'T':
			switch (toupper(subMenu))
			{
			case 'E':
				// if not entering sub-menu for first time and not out of array bounds increment Vehicle Array index
				if((counter != 0) && (counter < 6))
				{
					vehicle.IndexIncrement();
				}
				// if array bounds has been reached display message to user
				else if(counter > 5)
				{
					cout << " Vehicle Array is Full, will continue to replace last entry\n";
				}
				// Prompts user for information
				cout << "Enter vehicle name: ";
				cin >> name;
				cout << "Enter weight: ";
				cin >> weight;
				cout << "Enter horse power: ";
				cin >> horsepower;
				// Calls Accessor Functions
				vehicle.SetName(name);
				vehicle.SetVehicleWeight(weight);
				vehicle.SetHorsePower(horsepower);
				vehicle.CalcTime();
				// Increments counter everytime 'E' is selected
				++counter;
				break;
			case 'D':
				// Calls Accessor Functions
				vehicle.Display();
				system("pause");
				system("cls");
				break;
			case 'Q':
				// ends do while loop by setting boolean value to false
				quit = false;
				break;
			default:
				cout << "Invalid Selection returning to Main Menu\n";
			}
			break;
		}

	}while(quit); // End Loop if Q is entered
	//system("pause");
	return 0;
}

