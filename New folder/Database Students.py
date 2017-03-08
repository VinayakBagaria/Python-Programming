import requests
from bs4 import BeautifulSoup

us='1417175'
ps='10740382'

print('Wait')

s=requests.session()
payload = {'username': us, 'password': ps}
url = 'http://courses.christuniversity.in/login/index.php'
check_url='http://courses.christuniversity.in/message/index.php'
x=requests.post(url, data=payload)
y=requests.post('http://courses.christuniversity.in/message/index.php')
soup=BeautifulSoup(x.content,"html.parser")

all_links=soup.find_all('a')

