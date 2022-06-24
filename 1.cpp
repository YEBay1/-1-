/*
Çalışanın toplam mesai saati ve saatlik ücreti kullanıcı tarafından girilecek 
Kullanıcıya Ödenecek tutar gösterilecek 
*/

#include<iostream>
using namespace std;

int main(){
	double saat,ucret;
	
	cout<<"Calisilan Toplam Saati Girin: ";
	cin>>saat;
	
	cout<<"Saat basi ucreti girin: ";
	cin>>ucret;
	
	cout<<"Odenecek: $" << saat*ucret;
	
	return 0;
}
