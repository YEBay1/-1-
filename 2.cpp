/*
Fiti inçe çeviren bir program yazın
Kullanıcıya kaç fit olduğunu sorun ve bunun inç cinsinden eşdeğerini ekranda gösterin
Programınız,bu işleme kullanıcı fit için 0 girene kadar devam etsin 
*/

#include<iostream>
using namespace std;

int main(){
	//  1 fit 12 ince eşit olur.
	double feet;
	
 	do{
 	cout<<"Fiti Girin(cikis icin 0): ";
	cin>>feet;
	
	cout<<feet*12<<"inc\n";
	}while(feet !=0.0);
	
	return 0;

}
