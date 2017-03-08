from os import listdir
from tkinter.filedialog import askdirectory
from os.path import isfile, join

from tkinter import Tk
import os

def show():
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    for x in onlyfiles:
        extension = os.path.splitext(x)[1]
        _dir = os.path.join(folder,extension)
        if not os.path.exists(_dir):
            os.makedirs(_dir)
        path_file=join(_dir,x)
        FILE=open(path_file,'w')
        try:
            os.remove(folder+'/'+x);
        except:
            pass;


Tk().withdraw()
folder=''
folder=askdirectory()
if (folder!=''):
    show()

