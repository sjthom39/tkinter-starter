from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk
 
window = ThemedTk(theme="elegance")
 
window.title("smiley face")
 
window.geometry('450x300')

lbl = Label(window, text="A strange event", font=("Arial Bold", 25))
lbl.pack()




def changeText():
    lbl.configure(text = "A strange event")
    # lbl['text'] = "new text"

btn = Button(window, text="start botton", command=nextScene)

btn.pack()

chk_state = BooleanVar()
 
chk_state.set(True) #set check state
 
chk = Checkbutton(window, text='welcome', var=chk_state)
chk.pack()


combo = Combobox(window)
combo.pack()
 
combo['values']= (1, 2, 3, 4, 5, 6, 7, "secret")
 
combo.current(0) #set the selected item


story = Label(window, text="2077, april 20, 3:00am A strange event is happening in a power plant the dark matter genorator malfunctioned and the test subject 225 came he seemed to have the same energy radiating off him as the generator he absorbed the blast which could of destroyed the city and left other critical damages to our other power units ,the subject had memory loss he said he regains memory evryday the subjects name is jordan carter he says he comes from 2020 thats when the disaster happens when the sky goes purple weapons of mass destruction used to kill that thing in the water it seems as though it was february 7 for him. sighning off doctor.  ")
story.pack()


def nextScene():
    story.configure(text = "this is where the next part of the story goes")

 

 











window.mainloop()     # Keep the window open