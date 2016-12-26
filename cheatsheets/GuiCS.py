from Tkinter import *

# RESPONSIVE - DEFAULT LAYOUT
"""
# creates a new window
root = Tk()

one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="Two", bg="green", fg="white")
two.pack(fill=X)
three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)

# displays window infinitely
root.mainloop()
"""

# RESPONSIVE - GRID LAYOUT + FORM FIELDS
"""
root = Tk()

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E) # by default the col is always eq to 0
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

checkbox = Checkbutton(root, text="Keep me logged in")
checkbox.grid(columnspan=2)

root.mainloop()
"""

# RESPONSIVE - GRID LAYOUT + FUNCTIONS
"""
root = Tk()

def printName(event):
    print("Hello, my name is RK.")

button_1 = Button(root, text="Print my name")
button_1.bind("<Button-1>", printName)
button_1.pack()

root.mainloop()
"""

#RESPONSIVE - GRID LAYOUT + MOUSE EVENTS
"""
root = Tk()

def leftClick(event):
    print("LEFT")

def middleClick(event):
    print("MIDDLE")

def rightClick(event):
    print("RIGHT")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

root.mainloop()
"""

# CLASSES - GUI
class GuiCS:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("It werks!")

root = Tk()
gcs = GuiCS(root)
root.mainloop()