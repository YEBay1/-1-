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
        "Hayallerini açıklamak zorunda değilsin, onlar sadece sana aittir. - Paulo Coelho",
        "Senin almaya cesaret edemediğin riskleri alanlar, senin yaşamak istediğin hayatı yaşarlar.",
        "Yüzüstü yere serilseniz bile, hala ileriye doğru hareket ediyorsunuzdur.",
        "Bırakma. Şimdi acı çek ve hayatının geri kalanını bir şampiyon olarak yaşa.",
        "Bu para ya da bağlantılarla ilgili değil - bu, herkesten daha fazla çalışma ve öğrenme isteğidir-Mark Cuban",
        "Başarıya giden tüm yollar bir noktada çok çalışma bulvarından geçmek zorundadır-Eric Thomas",
        "Sahip olmaya değer hiçbir şey kolay gelmez-Theodore Roosevelt",
        "Fırsatlar genellikle sıkı çalışma kılığına girer, bu yüzden çoğu insan onları tanımaz-Ann Landers",
        "Neredeyse her durumda sıkı çalışmanın ödüllendirildiği türden bir toplumda yaşıyoruz-Neil deGrassa Tyson",
        "Günde 23 veya 24 saat sıkı çalışmanın yerini hiçbir şey tutamaz. Ve sabrın ve kabulün yerini hiçbir şey tutamaz-Cesar Chavez",
        "Çalışkan bir işçinin işareti, şikayet etmeden çalışan kişidir-Sarah Price",
        "Azim, zaten yaptığınız zor işi yapmaktan yorulduktan sonra yaptığınız zor iştir-Newt Gingrich",""
        "Acele etmeden, yetenek sizi ancak bir yere kadar götürür-Gary Vaynerchuk",
        "Başarının sırrı yoktur. Hazırlık, sıkı çalışma ve başarısızlıktan öğrenmenin sonucudur-Colin Powell",
        "Sahip olduğum herhangi bir başarıya en büyük özelliğimin çok çalışmak olduğunu düşünüyorum. Gerçekten çok çalışmanın yerini hiçbir şey tutamaz-Maria Bartiromo",
        "Şansa daha çok inanırım ve ne kadar çok çalışırsam o kadar çok şansım olur-Thomas Jefferson",
        "Yetenek sofra tuzundan daha ucuzdur. Yetenekli bireyi başarılı olandan ayıran şey çok çalışmasıdır-Stephen King",
        "Asla pes etmeyen birini yenmek zordur-Babe Ruth",
        "Başarılı olmak, çok çalışmak, asla pes etmemek ve hepsinden önemlisi muhteşem bir saplantıya sahip olmak-Walt Disney",
        "İnsanlar ustalığımı elde etmek için ne kadar çok çalıştığımı bilselerdi, o kadar da harika görünmezdi-Michelangelo",
        "Sessizce çok çalışın; Başarının gürültüyü yapmasına izin verin-Frank Ocean",
        "Gençken, yaptığım on şeyden dokuzunun başarısızlık olduğunu gözlemledim. Böylece on kat daha fazla iş yaptım-George Bernard Shaw",
        "Antrenmanın her dakikasından nefret ettim ama 'Bırakma' dedim. Şimdi acı çek ve hayatının geri kalanını bir şampiyon olarak yaşa-Muhammed Ali",
        "Başarı, zeka kadar çalışmakla elde edilir. Sebat lazım, inat etmek lazım ve çalışmak lazım. Üzerinde çalışacağınız bir konu belirleyin, literatür de okuyun, gerektiği kadar öğrenin. Okumanın yanı sıra düşünmek için de kendinize zaman ayırın-Aziz Sancar",
        "Ben hayatımın hiçbir anında karamsarlık nedir tanımadım-Mustafa Kemal Atatürk"]


def ButonTiklaması():
        for i in range(1):
                a = random.randint(0, len(sozler1))
                yazi1 = tkinter.Label(pencere, text=sozler1[a])
                yazi1.pack()

buton=tkinter.Button(pencere,text="Tıkla",command=ButonTiklaması)
buton.pack()

pencere.mainloop()
