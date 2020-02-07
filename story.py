from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk
 
window = ThemedTk(theme="elegance")
 
window.title("smiley face")
 
window.geometry('450x300')

lbl = Label(window, text="A strange event", font=("Arial Bold", 30))
lbl.pack()




def changeText():
    lbl.configure(text = "A strange event")
    # lbl['text'] = "new text"

def firstScene():
    option = combo.get()
    if option == "1":
        story.configure(text = "civilian report: me and my family herd a loud explosion comming from the skyplant, the ground was shaking and a million colors flew everywhere now these crystals are all over the place and my house is ruined im pressing charges if someone doesnt come down and fix this since they taking crystals why dont they fix my house it still has energy coming from it. agents: code 115 in progress we have to question and evacuate the main blast range the energy shards. agent 2: set up perimeters an dont let water fire or electrcity touch them. general: I give the orders here but yeah unless yall want world war 5 mow get to workin. ")
        btn.configure(command = secondScene)

    if option == "2":
        story.configure(text="The fact that were refugees makes it harder to move around in this system but the outside war ")

def secondScene():
    pass

btn = Button(window, text="start botton", command= firstScene)

btn.pack()

chk_state = BooleanVar()
 
chk_state.set(True) #set check state
 
chk = Checkbutton(window, text='welcome', var=chk_state)
chk.pack()


combo = Combobox(window)
combo.pack()
 
combo['values']= (1, 2, 3, 4, 5, 6, 7, "secret")
 
combo.current(0) #set the selected item


story = Label(window, text="2077, april 20, 3:00am A strange event is happening in a power plant the dark matter genorator malfunctioned and the test subject 225 came he seemed to have the same energy radiating off him as the generator he absorbed the blast which could of destroyed the city and left other critical damages to our other power units ,the subject had memory loss he said he regains memory evryday the subjects name is jordan carter he says he comes from 2020 thats when the disaster happens when the sky goes purple weapons of mass destruction used to kill that thing in the water it seems as though it was february 7 for him. sighning off doctor.  ", wraplength = 300, font=("roman", 15))
story.pack()




 

 











window.mainloop()     # Keep the window open