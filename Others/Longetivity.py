from tkinter import *
class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.inst_lbl=Label(self,text="Enter password for the secret of longitveity")
        # the label can take row 0 column 0 and row 0 column 1
        self.inst_lbl.grid(row=0,column=0,columnspan=2,sticky=W)

root=Tk()
app=Application(root)
root.mainloop()