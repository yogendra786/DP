#include <iostream>
#include <fstream>
#include <string>

#include "vector.hpp"
#include "sorter.hpp"
#include "timer.hpp"

using namespace adsa;
using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::ifstream;
using std::ofstream;


int main()
{
  sorter<int> s;
  timer time;
  int ch,n,i=0;
  int element;
  cout<< "Enter 1 to enter the elements manually" <<endl;
  cout<< "Enter 2 to enter the elements through file"<<endl;
  cin >> ch;
  if(ch == 1)
    {
      cout << "Enter the number of elements"<<endl;
      cin >> n;
      vector<int> vec(n,0); 
      cout << "Enter the elements"<<endl;
      
       
      while(i<n)
	{
	  cin >> element;
	  vec.push_back(element);
	  i++;
	
	}
      
  
      /* for(i = 0; i < n; i++)
     {
       cout << "value of vec [" << i << "] = " <<vec[i] << endl;
      }*/
   
   time.start();
   s.merge_sort(vec,0,n-1);
   time.stop();

   time.print();
   cout << "\nSorted elements are as follows :" <<endl;
    for(i = 0; i < n; i++)
     {
       cout << vec[i] << endl;
      }
   
    }



  
if(ch == 2)
    {
       string filename;
      cout << "Input name of the file " <<endl;
      cin >> filename;
      
      ifstream input_file;
      ofstream output_file;

      input_file.open(filename.c_str());
      output_file.open("output.txt");
      
if (!input_file.is_open())
  { 
 cout << "File could not be opened\n" << endl;
 return 0;
 }
 

 int count=0,datum;
 vector<int> vec;

 while (input_file >> datum)
  {
    vec.push_back(datum);
    count++;
  }



   time.start();
   s.rank_sort(vec,0,count-1);
   time.stop();

   cout <<"\nsorting complete"<<endl;
   time.print();
      
  for(i = 0; i < count; i++)
     {
       output_file << vec[i] <<endl;
      }
  cout <<"file has been written";  
 
input_file.close();
output_file.close();

    }

   return 0;
}













