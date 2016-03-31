#include <iomanip>
#include <iostream>

int main(){
  double u[30];
  u[0] = 2;
  u[1] = -4;
  
  for(int i=2 ; i<30 ; i++){
    u[i] = 111. - 1130./u[i-1] + 3000./(u[i-1]*u[i-2]);
    std::cout<<"u"<<i<<" = "<<u[i]<<std::endl;
  }
  return 0;
}
