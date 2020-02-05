from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk
 
window = ThemedTk(theme="elegance")
 
window.title("smiley face")
 
window.geometry('350x200')

lbl = Label(window, text="start the story")
lbl.pack()

def changeText():
    lbl.configure(text = "new text")
    # lbl['text'] = "new text"

btn = Button(window, text="start botton", command=changeText)
btn.pack()

chk_state = BooleanVar()
 
chk_state.set(True) #set check state
 
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=0)

combo.grid(column=0, row=0)
combo = Combobox(window)
 
combo['values']= (1, 2, 3, 4, 5, "secret")
 
combo.current(1) #set the selected item
 

 











window.mainloop()     # Keep the window open