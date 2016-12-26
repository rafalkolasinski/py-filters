from Tkinter import *


class GuiCSDropdownToolbar:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.menu = Menu(frame)
        master.config(menu = self.menu)

        # File menu
        self.subMenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="New project...", command=self.doNothing)
        self.subMenu.add_command(label="New...", command=self.doNothing)
        self.subMenu.add_separator()
        self.subMenu.add_command(label="Exit", command=frame.quit)

        # Edit menu
        self.editMenu = Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.editMenu)
        self.editMenu.add_command(label="Redo", command=self.doNothing)

        # Toolbar
        toolbar = Frame(master, bg="gray")

        open = Button(toolbar, text="Open image", command=self.doNothing)
        open.pack(side=LEFT, padx=2, pady=2)
        save = Button(toolbar, text="Save image", command=self.doNothing)
        save.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)

        # Status bar
        status = Label(master, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

    def doNothing(self):
        print("I won't, duh")

root = Tk()
gcsdt = GuiCSDropdownToolbar(root)
root.mainloop()