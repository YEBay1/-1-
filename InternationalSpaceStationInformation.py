import json
from requests import Request, Session


# Uzayda Bulunan İnsan Sayısı
url = 'http://api.open-notify.org/astros.json'
session = Session()
response = session.get(url)
veri= json.loads(response.content)
human=veri['people']

for i in range(0,len(human)-1):
    print(veri['people'][i]['craft'],"  ",veri['people'][i]['name'])



# ISS'in konumu
url1 = 'http://api.open-notify.org/iss-now.json'
session1 = Session()
response1 = session.get(url1)
veri1= json.loads(response1.content)
print("Boylam:",veri1['iss_position']['longitude']," , ","Enlem:",veri1['iss_position']['latitude'])






"""
https://www.geeksforgeeks.org/session-objects-python-requests/
"""

