/*
Arkadaşlar cin kısmında Türkçe karakter sorunu var.Bu sebeple Python'da daha gelişmiş bir uygulama yapacağım.
Cin Türkçe karakter sorununu aşamadım malesef :/ 
Bu sebeple burada bu uygulamayı bırakıyorum.
*/

#include<iostream>
#include<locale.h>
#include<string>
using namespace std; 


int main(){
	setlocale(LC_ALL, "Turkish");
	system("color f5");
	
	string kelimeler1[4]={"Mother","Human","Cat","Air",};
	string ceviriler1[4]={"Anne","insan","Kedi","Hava"};
	string ceviriler2[4]={"anne","insan","kedi","hava"};
	string ceviriler3[4]={"ANNE","INSAN","KEDİ","HAVA"};
	string c1;

	
	for(int i=0;i<4;i++){
		cout<<i+1<<" - "<<kelimeler1[i]<<endl;
		cin>>c1;
		cout<<"Girilen Cevap -> "<<c1<<endl;
		
		if (c1==ceviriler1[i]){
			cout<<"Dogru Cevap --> "<<ceviriler1[i]<<endl;
			cout<<"Dogru Bildiniz!"<<"\n"<<endl;
		}
		else if(c1==ceviriler2[i]){
			cout<<"Dogru Cevap --> "<<ceviriler1[i]<<endl;
			cout<<"Dogru Bildiniz!"<<"\n"<<endl;
		}
		else if(c1==ceviriler3[i]){
			cout<<"Dogru Cevap --> "<<ceviriler1[i]<<endl;
			cout<<"Dogru Bildiniz!"<<"\n"<<endl;
		}
		else{
			cout<<"Yanlis Cevap \n"<<endl;
			cout<<"Dogru Cevap --> "<<ceviriler1[i]<<"\n"<<endl;;
		}
	}
	
	return 0;
}




