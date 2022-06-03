import random
import tkinter

pencere=tkinter.Tk()

sozler1=["Hep denedin, hep yenildin. Olsun; gene dene, gene yenil. Bu sefer daha iyi yenil! - Samuel Beckett,"
        "Bugünü ve tüm yarınlarınızı hesaba katın; böylece dünleriniz için pişmanlık duymak için bir dakika daha harcamak zorunda kalmazsınız. - Lorri Faye",
        "Kendi hayat hikayenizi yazarken, kalemi başkasının tutmasına izin vermeyin!",
        "Senden nefret etmelerini durduracak tek bir şey var; yaptığın işte o kadar iyisin ki, seni görmezden gelemezler. - Orson Scott Card",
        "Yalnızca başarmayı arzularsanız başarılı olabilirsiniz; ancak başarısızlığa aldırmazsanız, başarısız olabilirsiniz. - Philippos",
        "Bütün ilerleme, konfor alanının dışında gerçekleşir. - Michael John Bobak",
        "Başarılı biri, başkalarının ona attığı tuğlalarla sağlam bir temel oluşturabilen kişidir. - David Brinkley",
        "Size yardım edecek kimse yokmuş gibi çalışın ve herkes yanınızdaymış gibi öğrenin. - Saransh Garg",
        "Neye tolerans gösterdiğine çok dikkat et. İnsanların sana nasıl davranmaları gerektiğini öğretiyorsun.",
        "Hayallerini açıklamak zorunda değilsin, onlar sadece sana aittir. - Paulo Coelho"]

a = random.choice(sozler1)
b = random.choice(sozler1)


def ButonTiklaması():
        yazi1 = tkinter.Label(pencere, text=a)
        yazi1.pack()

        yazi2 = tkinter.Label(pencere, text=b)
        yazi2.pack()


buton=tkinter.Button(pencere,text="Tıkla",command=ButonTiklaması)
buton.pack()

pencere.mainloop()
