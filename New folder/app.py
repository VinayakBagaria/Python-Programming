_author_='vinny'

# <span class="_1JT2XE" is="null">

import requests
from bs4 import BeautifulSoup

# request everything from the url
request=requests.get('https://www.flipkart.com/search?q=lenovo%20vibe%20k4%20note%20mobile&sid=tyy/4io&as=on&as-show=on&otracker=start&as-pos=1_3_ic_lenovo%20vibe%20k4%20note',verify='C:\Python35\Cyberoam_SSL_CA.pem')
# get html page of the url
content=request.content
soup=BeautifulSoup(content,"html.parser")
print(soup.prettify())
print(soup.title.text) 
