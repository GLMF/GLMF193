#include <iomanip>
#include <iostream>

int main(){
	double x;
	std::cout<<"Entrez la valeur de x"<<std::endl;
	std::cin>>x;
	double res = 0.0;
  	for (int i=0;i<1000;i++){
		res += x;
	}
	std::cout<<"Somme de 1000 fois "<<x<<" = "<<std::setprecision(20)<<res<<std::endl;
	return 0;
}
