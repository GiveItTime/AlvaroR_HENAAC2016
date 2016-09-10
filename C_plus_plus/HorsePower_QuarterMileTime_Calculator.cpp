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