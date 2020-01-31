# A starter program for Python with Tkinter
# A starter program for Python with Tkinter


from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk
 
window = ThemedTk(theme="elegance")
 
window.title("smiley face")
 
window.geometry('350x200')
chk_state = BooleanVar()
 
chk_state.set(True) #set check state
 
chk = Checkbutton(window, text='Choose', var=chk_state)
 
chk.grid(column=0, row=0)
combo = Combobox(window)
 
combo['values']= (1, 2, 3, 4, 5, "secret")
 
combo.current(1) #set the selected item
 
combo.grid(column=0, row=0)
 

lbl = Label(window, text="a weird botton")
 
lbl.grid(column=0, row=0)
 
txt = Entry(window,width=15, state='enabled')
 
txt.grid(column=1, row=0)
 
def clicked():
 res="welcome to happy space"+txt.get()
 lbl.configure(text=res)  
    
 
# btn = Button(window, text="happy botton", command=clicked, bg="blue", fg="cyan")
 
# btn.grid(column=2, row=0)

score = 0 

def addToScore():
  message = txt.get()
  if message == "Jon":
    lbl['text'] = "go away"
  else:
    lbl['text'] = "this is a virus"

 #Add a label with the text "Hello"
lbl = Label(window, text=score, font=("Arial Bold", 50))
lbl.grid(column=1, row=2)

btn = Button(window, text="clicker", command=addToScore)
btn.grid(column = 0 , row = 1)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)



window.mainloop()     # Keep the window open