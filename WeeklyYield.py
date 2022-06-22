import matplotlib.pyplot as plt
import numpy as np
import openpyxl
from openpyxl import Workbook

def HaftalıkVerimHesaplama():
    print("Günlerin önüne kaç saat çalıştığınızı yazın")

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

    gunlukort = float(a + b + c + d + e + f + g) / 7
    hours=[a,b,c,d,e,f,g]
    gunler=["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]
    dosya="rapor.xlsx"
    wb = openpyxl.Workbook()
    sheet = wb.active

    for i in range(7):
        c1=sheet.cell(row=i+1,column=1)
        c1.value=gunler[i]

        c2=sheet.cell(row=i+1,column=2)
        c2.value = hours[i]

        c3=sheet.cell(row=i+1,column=3)
        c3.value=hours[i]*60

    c4=sheet.cell(row=7,column=1)
    c4.value="Haftalık rapor"

    c5=sheet.cell(row=7,column=2)
    c5.value=gunlukort

    wb.save("rapor.xlsx")


    if gunlukort>=24:
        print("HATALI VERİ GİRMİŞ OLABİLİRSİNİZ.LÜTFEN GİRDİĞİNİZ VERİLERİ KONTROL EDİN VEYA UYGULAMAYI TEKRAR ÇALIŞTIRIN")
    else:
        saat = int(gunlukort)
        dakika = gunlukort - int(gunlukort)
        dk = (saat * 60) + dakika
        print("Bu hafta Günlük Ortalama ", int(dk), " dakika çalışıldı","\n")


    giris=input("Haftalık Verim Grafiğini Görmek için Q'ya,Haftalık Raporu Görmek için ise E'ye tıklayın --->")
    if giris=="Q":
        haftx = np.array(["PTESİ","SALI","ÇŞAMBA","PŞEMBE","CUMA","CTESİ","PAZAR"])
        saaty = np.array([a, b, c, d, e, f, g])
        plt.plot(haftx, saaty)
        plt.show()
    elif giris=="E":
        f = open("rapor.xlsx", "r")     # Burada kullanıcı için dosyanın açılması gerekiyor
        print(f.read())
    else:
        pass

HaftalıkVerimHesaplama()


"""
Bu uygulama geliştirilecektir
"""








