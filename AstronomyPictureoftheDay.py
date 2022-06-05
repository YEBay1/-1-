import json
from requests import Request, Session
import cv2
from translate import Translator
import urllib.request

url='https://api.nasa.gov/planetary/apod?api_key=         '
translator= Translator(to_lang="tr")

session = Session()
response = session.get(url)
veri=json.loads(response.content)

baslik=veri['title']
tarih=veri['date']
aciklama=veri['explanation']
resim=veri['hdurl']

imgurl=resim
urllib.request.urlretrieve(imgurl,"Astronomy.jpg")      # resmi indiririz

print(baslik,tarih,aciklama,resim,sep="\n")

img = cv2.imread ('Astronomy.jpg',1)                    # indirdiğimiz resmi gösteririz
cv2.imshow ('image',img)
cv2.waitKey(0)
