#include<iostream>
#include<string>
using namespace std;

int main(){
	setlocale(LC_ALL, "Turkish");   
	system("color f4");
	
	string islem;
	float a;
	float b;
	
	cout<<"Lütfen işlem kodu girin"<<endl;
	cout<<"Toplama için -> 1"<<endl;
	cout<<"Çıkarma için -> 2"<<endl;
	cout<<"Çarpma için  -> 3"<<endl;
	cout<<"Bölme için   -> 4"<<endl;
	cin>>islem;
	cout<<"1.sayiyi girin"<<endl;
	cin>>a;
	cout<<"2.sayiyi girin"<<endl;
	cin>>b;
	cout<<"\n";
	
	if (islem=="1"){
		cout<<a+b<<endl;	
	}
	else if(islem=="2"){
		cout<<a-b<<endl;
	}
	else if(islem=="3"){
		cout<<a*b<<endl;
	}
	else{
		cout<<float(a/b)<<endl;
	}
}
