import matplotlib.pyplot as plt
import numpy as np

for i in range(1):
    try:
        ptesi=float(input("Pazartesi -> "))
        sali=float(input("Salı -> "))
        csamba=float(input("Çarşamba -> "))
        psembe=float(input("Perşembe -> "))
        cuma=float(input("Cuma -> "))
        ctesi=float(input("Cumartesi -> "))
        pazar=float(input("Pazar -> "))

    except ValueError:
        print("Lütfen Bir Sayı Giriniz")

haftx = np.array([1,2,3,4,5,6,7])
saaty = np.array([ptesi,sali,csamba,psembe,cuma,ctesi,pazar])
plt.plot(haftx, saaty)
plt.show()

günlükort=float(ptesi+sali+csamba+psembe+cuma+ctesi+pazar)/7
saat=int(günlükort)
dakika=günlükort-int(günlükort)
sonuc=(saat*60)+dakika
print("Bu hafta Günlük Ortalama ",int(sonuc)," dakika çalışıldı")





