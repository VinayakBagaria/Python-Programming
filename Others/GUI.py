from tkinter import *
# Create the root window
root=Tk()
# Modify the window
root.title('Simple GUI')
# Width X Height
root.geometry('200x100')
# Create a frame to hold other widgets (window gadgets)
app=Frame(root)
# grid() allows us to arrange the widgets where-ever we want -- Layout Manager
app.grid()

# Create a label
lbl=Label(app,text='Hi Shivu')
# Ensures that the label is visible
lbl.grid()

# Create a button
btn=Button(app)
btn['text']='Click here'
btn.grid()

# Start up the window's event loop by invoking the method ml()
root.mainloop()