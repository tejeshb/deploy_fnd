import requests
url = 'http://localhost:8910/submit'
r = requests.post(url,json={'exp':'teja is a good boy',})
#print(r.json())