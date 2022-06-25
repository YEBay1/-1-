"""
Bu kütüphane harici daha kaliteli bir APİ kullanabilirsiniz

Mesela random yüzünden kelimelerin arka arkaya gelmesini engelleyebilirsiniz ama kelime sayısı arttıkça bu olasılık düşecektir.
Uygulamayı geliştirebilirsiniz.Farklı modlar ekleyebilirsiniz.Daha temiz kod yazabilirsiniz.

Benden bu kadar
"""


import random

from translate import Translator
import time
import random
translator= Translator(to_lang="tr")

print("Uygulamamıza Hoşgeldiniz")
print("Lütfen Bekleyin")
print("Uygulama Başlatılıyor")

for i in range(4):
    time.sleep(1)
    print("*",end=" ")

print("\n","Lütfen İmla Kurallarına dikkat ediniz!")

for i in range(4):
    time.sleep(1)
    print("*",end=" ")


kelimeler=["Chicken","Airport","Dog","Cat","Expensive","Fat","Long","Short","Civilization","War","Sun","Moon","Rain","Snow","Ice","Frozen","Peas","Apricot","Beef","Banana"]

dogrucevap = 0
yanliscevap = 0

print("\n")

for i in kelimeler:
    a=random.choice(kelimeler)


    tr = translator.translate(a)
    trceviri1 = tr.lower()
    trceviri2 = tr.upper()

    print("Lütfen Türkçesini Giriniz -->", a)
    veri = input("").lower()

    if veri == trceviri1:
        print("Doğru bildiniz", "\n")
        dogrucevap += 1
        print("--------------------------------------------")
        print("Doğru Sayısı :", dogrucevap)
        print("Yanlış Sayısı :", yanliscevap)
        print("--------------------------------------------")

    elif veri == tr:
        print("Doğru bildiniz", "\n")
        dogrucevap += 1
        print("--------------------------------------------")
        print("Doğru Sayısı :", dogrucevap)
        print("Yanlış Sayısı :", yanliscevap)



    elif veri == trceviri2:
        print("Doğru bildiniz", "\n")
        dogrucevap += 1
        print("--------------------------------------------")
        print("Doğru Sayısı :", dogrucevap)
        print("Yanlış Sayısı :", yanliscevap)
        print("--------------------------------------------")

    else:
        print("Yanlış Cevap")
        print("Doğru Cevap -->", tr, "\n")
        yanliscevap += 1
        print("--------------------------------------------")
        print("Doğru Sayısı :", dogrucevap)
        print("Yanlış Sayısı :", yanliscevap)
        print("--------------------------------------------", "\n")
