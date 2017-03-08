import requests
from bs4 import BeautifulSoup
import getpass

us=input("Enter your reg no : ")
ps=getpass.getpass("Enter your password : ")

print("Wait")

payload = {'username': us, 'password': ps}
url = 'http://courses.christuniversity.in/login/index.php'
x=requests.post(url, data=payload)

soup=BeautifulSoup(x.content,"html.parser")

try:
    string=soup.find('span',attrs={'class':'usertext'}).text
    print(string.rsplit(' ',1)[0])
except:
    print('Wrong input')
