/*
Çalışan bir kişinin toplam mesai saatinin ve maaşının girildiği bir program yazın.
Sonra çalışanın net maaşını ekranda gösterin 
Saat sayısı ve maaşı kullanıcı tarafından girilsin 
*/

#include<iostream>
using namespace std;

int main(){
	int mesaisaat,maas,sonuc;
	
	cout<<"Mesai saat sayisini giriniz -->";
	cin>>mesaisaat;
	
	cout<<"Maasi girin -->";
	cin>>maas;
	
	sonuc=((maas/30)*mesaisaat)+maas;
	cout<<sonuc;
}
