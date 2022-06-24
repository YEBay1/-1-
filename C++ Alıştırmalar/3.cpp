#include<iostream>
using namespace std;

int main(){
	int num;
	
	do{
	cout<<"Test Edilecek Sayiyi Girin (Cikmak icin 0): ";
	cin>>num;
	
	if((num%2)==0) 
	cout<<"Bu bir çift sayidir \n";
	else cout<<"Bu bir tek sayidir \n";
	}while(num != 0);
	
	return 0;
}
