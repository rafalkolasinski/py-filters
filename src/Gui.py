import Tkinter as tk
import ImageHandler as ih
from tkFileDialog import askopenfilename
from functools import partial


class Gui(object):

    def __init__(self, master):
        self.master = master
        self.imgHandler = ih.ImageHandler()
        self.tkinter = tk

        # Grid responsiveness config
        # tk.Grid.rowconfigure(self.master, 0, weight=1)
        # tk.Grid.columnconfigure(self.master, 0, weight=1)

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.menu = tk.Menu(self.frame)
        self.master.config(menu=self.menu)

        # File menu
        self.subMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="Open image", command=partial(self.imgHandler.openImage, self))
        self.subMenu.add_command(label="Save image", command=self.imgHandler.saveImage)
        self.subMenu.add_separator()
        self.subMenu.add_command(label="Exit", command=self.frame.quit)

        # Edit menu
        self.editMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.editMenu)
        self.editMenu.add_command(label="Apply filter")

        # Edit menu -> Filter menu
        # @TODO: list all of the filters and assign methods
        # self.filterMenu = tk.Menu(self.editMenu)
        # self.editMenu.add_cascade(self.filterMenu)


        # Toolbar
        self.toolbar = tk.Frame(self.master, bg="gray")

        self.open = tk.Button(self.toolbar, text="Open image", command=partial(self.imgHandler.openImage, self))
        self.open.pack(side=tk.LEFT, padx=2, pady=2)
        self.save = tk.Button(self.toolbar, text="Save image", command=self.imgHandler.saveImage)
        self.save.pack(side=tk.LEFT, padx=2, pady=2)

        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # Images frame
        self.imgFrame = tk.Frame(self.master)
        self.imgFrame.pack()

        # Original image frame
        self.original = tk.Frame(self.imgFrame, bd=10, bg="red")
        self.original.pack(side=tk.LEFT, padx=75)
        self.originalLabel = tk.Label(self.original, text="ORIGINAL IMAGE", anchor=tk.CENTER)
        self.originalLabel.pack(side=tk.TOP, fill=tk.BOTH)
        self.originalImage = tk.Label(self.original, text="No image opened", anchor=tk.CENTER)
        self.originalImage.pack(side=tk.BOTTOM)

        # Modified image frame
        self.modified = tk.Frame(self.imgFrame, bd=10, bg="blue")
        self.modified.pack(side=tk.LEFT, padx=75)
        self.modifiedLabel = tk.Label(self.modified, text="MODIFIED IMAGE", anchor=tk.CENTER)
        self.modifiedLabel.pack(side=tk.TOP, fill=tk.BOTH)
        self.modifiedImage = tk.Label(self.modified, text="No image opened", anchor=tk.CENTER)
        self.modifiedImage.pack(side=tk.BOTTOM)

        # Status bar
        self.status = tk.Label(self.master, text="Preparing to do stuff...", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    @staticmethod
    def openFilePicker():
        filename = askopenfilename()
        if filename:
            return filename

    @staticmethod
    def insertOriginalImage(self, img):
        photo = img # keeping image reference for safety reasons

        if hasattr(self, 'originalImage') and hasattr(self, 'modifiedImage'):
            # clearing the images
            self.originalImage.destroy()
            self.modifiedImage.destroy()

            # inserting new images
            self.originalImage = tk.Label(self.original, image=photo)
            self.originalImage.pack(side=tk.BOTTOM)
            self.modifiedImage = tk.Label(self.modified, image=photo)
            self.modifiedImage.pack(side=tk.BOTTOM)
        print "CON: **Inserted image into GUI**"