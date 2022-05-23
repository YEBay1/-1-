"""
Kodları iyice bir elden geçirmem gerekiyor.
Kullanıcı arayüzü ekleyebilirim.
Diğer Projeler gibi bu uygulamayıda geliştireceğim


Açıkcası çoğu işi GoogleNews kütüphanesi yapıyor.
Ben database'den kullanıcı verilerini alıp,onaylayıp,verileri düzenliyorum ve kullanıcıya sunuyorum.Ne kadar kötü de olsa :D
"""

from GoogleNews import GoogleNews
import time
from time import gmtime, strftime
import mysql.connector

googlenews=GoogleNews()

veritabanı=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=""
)

mycursor=veritabanı.cursor()
mycursor.execute("SELECT * FROM kullanıcı ")
veriler=mycursor.fetchall()


def ŞifreKontrolü():
    kontrol = int(input("Lütfen Şifrenizi Giriniz ---> "))
    for i in veriler:
        if kontrol==i[2]:
            uygulama()
        else:
            pass


def uygulama():
    print("\n")
    googlenews=GoogleNews(lang="en")

    a2=time.time()
    s = strftime("%d/%b/%Y ",gmtime(a2))
    googlenews=GoogleNews(start=s)

    arama=str(input("Hangi Konu Başlığını Aramak İstersiniz ---> "))
    googlenews.get_news(arama)

    results=googlenews.results()

    print("\n")
    for i in range(1,len(results)-1):
        print(results[i]['title'])
        print(results[i]['date'])
        print(results[i]['link'], "\n", "\n")


def kullanıcıkayıt():
    a1=str(input("Kullanıcı Adınızı Oluşturun --> "))
    a2=str(input("Lütfen Şifrenizi Belirleyin --> "))
    sql1="INSERT INTO kullanıcı (ad, sifre) VALUES (%s,%s)"
    kayıt=(a1,a2)
    mycursor.execute(sql1,kayıt)
    veritabanı.commit()

def Giris():
    print("Hoşgeldiniz")
    a6 = input("Kayıt olmak için K tuşuna basın,Kayıtlı iseniz Enter'e basın ---> ")

    if a6 == "K":
        kullanıcıkayıt()
    else:
        pass

    a5 = input("Lütfen Kullanıcı Adınızı Giriniz ---> ")
    for x in veriler:
        if a5==x[1]:
            print("Kullanıcı Adınız Doğru")
            ŞifreKontrolü()
        else:
            pass



Giris()
