# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window

# Add a label with the text "Hello"
window.title("SCHOOL MONITOR.EXE")
lbl = Label(window, text="Hello", font=("Courier New", 50))
# Place the label in the window at 0, 0

btn = Button(window, text="Click Me", bg="white", fg="blue")
btn.grid(column=1, row=0)
lbl.grid(column=0, row=0)
def clicked():
 
    lbl.configure(text="a virus has been installed")


window.mainloop()     # Keep the window open
