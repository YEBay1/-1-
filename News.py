from GoogleNews import GoogleNews
import time
from time import gmtime,strftime

googlenews=GoogleNews()
googlenews=GoogleNews(lang="en")

arama=str(input("Konu Başlığı Giriniz:"))
googlenews.get_news(arama)

results=googlenews.results()

for i in range(len(results)-1):
    print(results[i]['title'])
    print(results[i]['date'])
    print(results[i]['link'],"\n","\n")
   

 

















