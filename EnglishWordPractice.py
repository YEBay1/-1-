from translate import Translator
import time
translator= Translator(to_lang="tr")

print("Uygulamamıza Hoşgeldiniz")
print("Lütfen Bekleyin")
print("Uygulama Başlatılıyor")

for i in range(5):
    time.sleep(1)
    print("*",end=" ")


a=["Chicken","Airport","Dog","Cat","Expensive"]

dogrucevap = 0
yanliscevap = 0

print("\n")

for i in a:
    tr = translator.translate(i)
    trceviri1=tr.lower()
    trceviri2=tr.upper()

    print("Lütfen Türkçesini Giriniz -->",i)
    veri = input("").lower()

    if veri==trceviri1:
        print("Doğru bildiniz","\n")
        dogrucevap+=1
        print("--------------------------------------------")
        print("Doğru Sayısı :",dogrucevap)
        print("Yanlış Sayısı :",yanliscevap)
        print("--------------------------------------------")

    elif veri==tr:
        print("Doğru bildiniz","\n")
        dogrucevap += 1
        print("--------------------------------------------")
        print("Doğru Sayısı :",dogrucevap)
        print("Yanlış Sayısı :",yanliscevap)



    elif veri==trceviri2:
        print("Doğru bildiniz","\n")
        dogrucevap += 1
        print("--------------------------------------------")
        print("Doğru Sayısı :",dogrucevap)
        print("Yanlış Sayısı :",yanliscevap)
        print("--------------------------------------------")

    else:
        print("Yanlış Cevap")
        print("Doğru Cevap -->",tr,"\n")
        yanliscevap += 1
        print("--------------------------------------------")
        print("Doğru Sayısı :",dogrucevap)
        print("Yanlış Sayısı :",yanliscevap)
        print("--------------------------------------------","\n")
