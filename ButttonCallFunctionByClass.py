from tkinter import *
class processButtonEvent:
    def__init__(self):
        window=Tk()
        btok=Button(window,text="OK",fg="white",bg="green",command=processOk)
        btcancel=Button(window,text="Cancel",bg="red",fg="yellow",command=processcancel)
        btok.pack()
        btcancel.pack()
        window.mainloop()

    def processOk(self):
        print("you clicked a ok button")
    def processcancel(self):
        print("clicked a cancel button")

processButtonEvent()
