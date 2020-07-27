#include <iostream>
using namespace std;

// Parent CLass
class Employee
{
	public:
		int BaseAmount; // Basic Salary
		int ExtraAmount; // Extra Salary for Senior Post
		
		// Pure Virtual Function
		virtual float getSalary() = 0;
		
		// Assigning value to BaseAmount
		void setBaseAmount(float sal)
		{
			BaseAmount = sal;
		}
		
		// Assigning value to ExtraAmount
		void setExtraAmount(float sal)
		{
			ExtraAmount = sal;
		}
};

// Child Class 1
class GolangDeveloper: public Employee
{
	public:
		// Overridng the parent function to get Salary
		float getSalary()
		{
			return BaseAmount;
		}
};

// Child Class 2
class SeniorGolangDeveloper: public Employee
{
	public:
		// Overridng the parent function to get Salary
		float getSalary()
		{
			return BaseAmount + ExtraAmount;
		}
};

int main()
{
	GolangDeveloper GD; //Object Creation for Child Class 1
	SeniorGolangDeveloper SGD; // Object Creation for Child Class 2
	
	GD.setBaseAmount(540000);
	cout << "Salary of Golang Developer is " << GD.getSalary() << " LPA" << endl;
	
	SGD.setBaseAmount(540000);
	SGD.setExtraAmount(105000);
	cout << "Salary of Senior Golang Developer is " << SGD.getSalary() << " LPA" << endl;

	return 0;	
}
