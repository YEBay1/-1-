import time
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook

def Kronometre():
    gir=input("Kronometreyi başlatmak için T'ye tıklayın -->")
    if gir=="T":
        print("Başlangıç Zamanı -->",time.strftime('%X'))
        stop1=input("Kronometreyi durdurmak için Y'ye Tıklayın")
        if stop1=="Y":
            print("Bitiş Zamanı -->",time.strftime("%X"))

    else:
        pass


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



    for i in range(len(hours)-1):           
        if hours[i]>23:
            print("Hatalı Veri Girişi")
            HaftalıkVerimHesaplama()
        else:
            pass


    if gunlukort>=24:
        print("HATALI VERİ GİRMİŞ OLABİLİRSİNİZ.LÜTFEN GİRDİĞİNİZ VERİLERİ KONTROL EDİN")
        HaftalıkVerimHesaplama()
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
        dosya1 = load_workbook("rapor.xlsx")
        sheet = dosya1.active

        dosya = load_workbook("rapor.xlsx")
        sheet = dosya.active
        for row in sheet.iter_rows(min_row=1, min_col=1, max_row=7, max_col=2):
            for cell in row:
                print(cell.value, end=" ")
            print()

            dosya.close()

    else:
        pass

HaftalıkVerimHesaplama()
