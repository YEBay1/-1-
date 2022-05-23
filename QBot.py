"""
Bu Uygulama Bize sadece bitcoin fiyatını telegram üzerinden bir bot ile gönderecektir     --->  https://coinmarketcap.com/api/
Telegram'dan BotFather ile iletişim kurup,kendi botumuzu oluşturmamız gerekiyor

BOTU GELİŞTİRMEYİ DÜŞÜNÜYORUM.İLERLEME SAĞLADIĞIMDA DOSYAYI GÜNCELLEYECEĞİM.Şuan baya basit bir bot oldu :/ ve dandik
"""


import time
from telebot import TeleBot
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from GoogleNews import GoogleNews
from time import gmtime, strftime


bot = TeleBot(token=" Buraya BotFather ile oluşturduğunuz Botun token değerini giriyorsunuz ")               # Token değerini kimse ile paylaşmayınız






# COİN BİLGİLERİNİ ÇEKME

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
  'start':'1',
  'limit':'1',              # Bunu arttırarak coin sayısını arttırabilirsiniz 2 yazarsanız ETH bilgileride gelecektir 
  'convert':'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': ' https://coinmarketcap.com/api/   --> Bu siteden aldığınız İd'yi buraya yapıştırın  ',
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
veri= json.loads(response.content)
a=veri['data']    

donusum=json.dumps(a,indent=1)   # Json dizesine çeviriririz



# Bitcoin Haberlerini Alma
googlenews=GoogleNews()
googlenews=GoogleNews(lang="en")
a2=time.time()
s = strftime("%d/%b/%Y ", gmtime(a2))
googlenews=GoogleNews(start=s)
A=googlenews.get_news("btc")     # anahtar kelime girişi
G = googlenews.results()

a=G[1]['title']
c=G[1]['link']
d=G[2]['title']
f=G[2]['link']

@bot.message_handler(commands=['btc'])      #/btc komutu girildiğinde...
def botu_baslatma(start):
     bot.reply_to(start, a)
     bot.reply_to(start, c)
     bot.reply_to(start, d)
     bot.reply_to(start,f)



    
    
# BOT İLE MESAJ GÖNDERME

@bot.message_handler(commands=['start'])      # /start komutu girildiğinde
def botu_baslatma(start):
     bot.reply_to(start, donusum)    # Buraya kullanıcıya göstermek istediğiniz bilgileri girin 

bot.polling()        
