/*
Alıştırmalar

2-card adında kütüphane kartı verilerini saklayan bir sınıf oluşturun.
Bu sınıf kitap adı,yazar ve elde bulunan kitap adedi verilerini saklasın.
Kitap adı ve yazarı katar olarak,eldeki adedi de tamsayı olarak saklayın.
Kitap bilgilerini saklamak için store() adında ve bilgileri göstermek için ise show() adında birer public(genel) fonksiyon kullanın
Sınıfı göstermek için kısa bir main() fonksiyonu kullanın.
*/ 

#include<iostream>
#include<cstring>
using namespace std;

class card{
	char title[80];		// Kitap Adı
	char author[40];	// Yazar
	int number;			  // Kütüphane Numarası
	
public:
	void store(char *t,char *name,int num);
	void show();
};

void card::store(char *t,char *name,int num)
{
	strcpy(title, t); 
	strcpy(author, name);
	number=num;
}

void card::show()
{
	cout<<"Kitap Adi: "<<title<<"\n";
	cout<<"Yazar: "<<author<<"\n";
	cout<<"Eldeki Sayi: "<<number<<"\n";
}

int main()
{
	card book1,book2,book3;
	
	book1.store("Dune","Frank Herbert",2);
	book2.store("The Foundation Trigology","Isaac Asimov",2);
	book3.store("The Rainbow","D.H.Lawrence",1);
	
	book1.show();
	book2.show();
	book3.show();
	
	return 0;
}
