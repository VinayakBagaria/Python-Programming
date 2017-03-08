import glob
from tkinter import Tk
from tkinter.filedialog import askdirectory

Tk().withdraw()
#filename = askopenfilename()
folder=askdirectory()
#print(filename)
print(folder+"\n")
files=glob.glob(folder)
for f in files:
    print(f)
