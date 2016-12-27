import Tkinter as tk
import ImageHandler as ih
from tkFileDialog import askopenfilename


class Gui(object):

    def __init__(self, master):
        self.master = master
        self.imgHandler = ih.ImageHandler()

        frame = tk.Frame(self.master)
        frame.pack()

        self.menu = tk.Menu(frame)
        self.master.config(menu=self.menu)

        # File menu
        self.subMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="Open image", command=ih.ImageHandler().openImage)
        self.subMenu.add_command(label="Save image", command=ih.ImageHandler().saveImage)
        self.subMenu.add_separator()
        self.subMenu.add_command(label="Exit", command=frame.quit)

        # Edit menu
        self.editMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.editMenu)
        # @TODO: list all of the filters and assign methods
        # self.editMenu.add_command(label="Redo", command=self.doNothing)

        # Toolbar
        toolbar = tk.Frame(self.master, bg="gray")

        open = tk.Button(toolbar, text="Open image", command=ih.ImageHandler().openImage)
        open.pack(side=tk.LEFT, padx=2, pady=2)
        save = tk.Button(toolbar, text="Save image", command=ih.ImageHandler().saveImage)
        save.pack(side=tk.LEFT, padx=2, pady=2)

        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Status bar
        status = tk.Label(self.master, text="Preparing to do stuff...", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        status.pack(side=tk.BOTTOM, fill=tk.X)

    def openFilePicker(self):
        frame = tk.Frame(self.master)
        frame.pack()
        filename = askopenfilename()
        return filename
