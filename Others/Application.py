from tkinter import *
class Application(Frame):
    # Constructor
    def __init__(self,master):
        Frame.__init__(self,master)
        # grid() allows us to arrange the widgets where-ever we want -- Layout Manager
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.btn=Button(self)
        self.btn['text']='Hola'
        self.click=0
        # Command on a button is a click
        self.btn['command']=self.update_click
        self.btn.grid()
    def update_click(self):
        self.click+=1
        self.btn['text']=str(self.click)
# Create the root window
root=Tk()
root.title('Application Page')
root.geometry('200x200')
# Create a frame to hold other widgets (window gadgets) by call to constructor
app=Application(root)
# Start up the window's event loop by invoking the method ml()
root.mainloop()