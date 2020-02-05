from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk
 
window = ThemedTk(theme="elegance")
 
window.title("smiley face")
 
window.geometry('350x200')

lbl = Label(window, text="start the story")
lbl.pack()

def changeText():
    lbl.configure(text = "A strange event")
    # lbl['text'] = "new text"

btn = Button(window, text="start botton", command=changeText)
btn.geometry('50x20')
btn.pack()

chk_state = BooleanVar()
 
chk_state.set(True) #set check state
 
chk = Checkbutton(window, text='welcome', var=chk_state)
chk.pack()


combo = Combobox(window)
combo.pack()
 
combo['values']= (1, 2, 3, 4, 5, 6, 7, "secret")
 
combo.current(0) #set the selected item
 

 











window.mainloop()     # Keep the window open