import random
#package to get data from websites
import urllib.request

def downloadWebImage(url):
    name=random.randrange(1,1000)
    full_name='image'+str(name)+'.jpg'
    #download url and save it as filename
    urllib.request.urlretrieve(url,full_name)

downloadWebImage('http://vignette4.wikia.nocookie.net/gameofthrones/images/d/de/Emilia-Clarke(1).jpg/revision/latest?cb=20140615201521')
#Given is a google URL of a pic of Emilia Clarke
