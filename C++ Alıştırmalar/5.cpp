/*
3-Tamsayıların saklanması için queue(kuyruk) adında bir sınıf oluşturun.
Kuyruğun büyüklüğünü 100 tamsayı uzunluğunda yapın.
Bu işlemi gösteren kısa bir main() fonksiyonu oluşturun.
*/ 

#include<iostream>
using namespace std;

#define SIZE 100

class q_type{
	int queue[SIZE];	// Kuyruğu tutuyor
	int head,tail;		// Kafa ve kuyruğun indisi 
	
public:
	void init();		// Hazırlık
	void q(int num);	// Kayıt
	int deq();			// Tekrar alma 
};

// Hazırlık 
void q_type::init()
{
	head=tail=0;
}

// Kuyruğa değer veriliyor
void q_type::q(int num)
{
	if(tail+1==head || (tail+1==SIZE && !head))
	{
		cout<<"Kuyruk Dolu \n";
		return;		
	}
	tail++;
	if(tail==SIZE) tail=0; 	// çevrim
	queue[tail]=num;
}

// Kuyruktan bir değer çıkarılıyor 
int q_type::deq()
{
	if(head==tail)
	{
		cout<<"Kuyruk Boş \n";
		return 0;		// veya başka bir hata gösterici 
	}
	
	head++;
	if(head==SIZE) head=0; 	// çevrim 
	return queue[head];
}

int main(){
	q_type q1,q2;
	int i;
	
	q1.init();
	q2.init();
	
	for(i=1;i<=10;i++){
		q1.q(i);
		q2.q(i*i);
	}
	
	for(i=1;i<=10;i++){
		cout<<"Dequeue 1: "<<q1.deq()<<"\n";
		cout<<"Dequeue 2: "<<q2.deq()<<"\n";
	}
	
	return 0;
}
