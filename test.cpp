#include <iostream>
#include "timer.hpp"

int main()
{
  timer time;
  time.start();
  for(int i=0;i<150000;i++)
    {
      ;
    }
  time.stop();
  time.print();
  
}
