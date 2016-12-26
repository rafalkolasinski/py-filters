from Tkinter import *
import tkMessageBox


class GuiCSMessagebox:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        tkMessageBox.showinfo("Supertitle", "Hurr durr test message!")

        answer = tkMessageBox.askquestion("Question 1", "Do you like sth?")
        if answer == "yes":
            print(" yay ")
        else:
            print(" nay ")

root = Tk()
gcsm = GuiCSMessagebox(root)
root.mainloop()