from bs4 import BeautifulSoup
import requests

def trade_spider(max_pages):
    page=1
    while(page<=max_pages):
        url='https://thenewboston.com/'
        source_code=requests.get(url)
        plain_text=source_code.text   #get the html codes
        soup=BeautifulSoup(plain_text,"html.parser")
        #Now find all titles in soup
        for link in soup.find_all('a'):   #get all titles
            href='https://thenewboston.com/'+link.get('href')
            if(href.find('videos')!=-1):
                print(href+"\n")
        page+=10
trade_spider(1)