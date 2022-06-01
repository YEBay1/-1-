import matplotlib.pyplot as plt
import numpy as np

def HaftalıkVerimHesaplama():
    for i in range(1):
        try:
            a=float(input("Pazartesi -> "))
            b=float(input("Salı -> "))
            c=float(input("Çarşamba -> "))
            d=float(input("Perşembe -> "))
            e=float(input("Cuma -> "))
            f=float(input("Cumartesi -> "))
            g=float(input("Pazar -> "))

        except ValueError:
            print("Lütfen Bir Sayı Giriniz")


    günlükort=float(a+b+c+d+e+f+g)/7

    if günlükort>=24:
        print("HATALI VERİ GİRMİŞ OLABİLİRSİNİZ.LÜTFEN GİRDİĞİNİZ VERİLERİ KONTROL EDİN VEYA UYGULAMAYI TEKRAR ÇALIŞTIRIN")
    else:
        saat = int(günlükort)
        dakika = günlükort - int(günlükort)
        dk = (saat * 60) + dakika
        print("Bu hafta Günlük Ortalama ", int(dk), " dakika çalışıldı","\n")


    Q=input("Haftalık Verim Grafiğini Görmek için Q'ya tıklayın ve Girin --->")
    if Q=="Q":
        haftx = np.array(["PTESİ","SALI","ÇŞAMBA","PŞEMBE","CUMA","CTESİ","PAZAR"])
        saaty = np.array([a, b, c, d, e, f, g])
        plt.plot(haftx, saaty)
        plt.show()
    else:
        pass
