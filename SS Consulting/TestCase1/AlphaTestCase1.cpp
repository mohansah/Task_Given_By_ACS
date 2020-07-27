#include <iostream> 
#include <fstream> 
using namespace std; 
  
// Class with four properties 
class Info
{ 
	public:
		// Instance variables 
	    string FirstName, LastName, Address; 
	    int Age; 
};  
  
// Driver code 
int main() 
{ 
    // Creating object of the class Info
    Info object1, object2; 
  
    // Instantiating the object
    object1.FirstName = "Mohan";
	object1.LastName = "Sah";
	object1.Age = 22;
	object1.Address = "Kuwar Singh Chowk Main Road Jaynagar, Madhubani, Bihar - 847226";

	// Object to write in file 
    ofstream file_obj1; 
    
	// Opening file in output mode 
    file_obj1.open("Input.txt", ios::out);
    if(!file_obj1)
    {
      cout << "Error in creating file" << endl;
      return 0;
    }
    
	// Writing the object's data in file 
    file_obj1.write((char*)&object1, sizeof(object1));
    
    //close the file
    file_obj1.close();
    
    
	// Object to read from file 
    ifstream file_obj2; 
  
    // Opening file in input mode 
    file_obj2.open("Input.txt", ios::in);
    if(!file_obj2)
    {
        cout << "Error in Opening the file" << endl;
        return 0;
	}
    
    // Reading the object's data from the file
    file_obj2.read((char*)&object2, sizeof(object2));
    
    // Printing the Object's data in JSON format
	cout << "[" << endl;
    cout << "\t{" << endl;
	cout << "\t\t" << '"'<< "FirstName" << '"' << ": " << '"' << object2.FirstName << '"' << "," << endl;
	cout << "\t\t" << '"'<< "LastName" << '"' << ": " << '"' << object2.LastName << '"' << "," << endl;
	cout << "\t\t" << '"'<< "Age" << '"' << ": " << '"' << object2.Age << '"' << "," << endl;
	cout << "\t\t" << '"'<< "Address" << '"' << ": " << '"' << object2.Address << '"' << endl;
	cout << "\t}" << endl;
    cout << "]" << endl;
    
    //close the file
    file_obj2.close();
    
    return 0; 
}
