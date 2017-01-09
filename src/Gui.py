import Tkinter as tk
import ImageHandler as ih
from Colours import Palette
from Filters import Filters
from tkFileDialog import askopenfilename
from functools import partial


class Gui(object):

    def __init__(self, master):
        self.master = master
        self.imgHandler = ih.ImageHandler()
        self.tkinter = tk
        self.filters = Filters()

        # Grid responsiveness config
        # tk.Grid.rowconfigure(self.master, 0, weight=1)
        # tk.Grid.columnconfigure(self.master, 0, weight=1)

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.menu = tk.Menu(self.frame)
        self.master.config(menu=self.menu)
        self.master.title("py-filters")

        # File menu
        self.subMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="Open image", command=partial(self.imgHandler.openImage, self))
        self.subMenu.add_command(label="Save image", command=self.imgHandler.saveImage, state=tk.DISABLED)
        self.subMenu.add_separator()
        self.subMenu.add_command(label="Exit", command=self.frame.quit)

        # Edit menu
        self.editMenu = tk.Menu(self.menu)

        # Edit menu -> Filter menu
        # @TODO: list all of the filters and assign methods
        self.filterMenu = tk.Menu(self.editMenu)
        self.filterMenu.add_command(label="Blur...", command=partial(self.filters.blur, self.imgHandler, self))
        self.filterMenu.add_command(label="Grayscale...", command=partial(self.filters.grayscale, self.imgHandler, self))
        self.filterMenu.add_command(label="Invert colours...", command=partial(self.filters.invert, self.imgHandler, self))

        # Attach filtermenu to editmenu
        self.editMenu.add_cascade(label="Apply filter", menu=self.filterMenu)

        # Attach editmenu to menu
        self.menu.add_cascade(label="Edit", menu=self.editMenu, state=tk.DISABLED)

        # Toolbar
        self.toolbar = tk.Frame(self.frame, bg=Palette.GRAY)

        self.open = tk.Button(self.toolbar, text="Open image", command=partial(self.imgHandler.openImage, self))
        self.open.pack(side=tk.LEFT, padx=2, pady=2)
        self.save = tk.Button(self.toolbar, text="Save image", command=self.imgHandler.saveImage, state=tk.DISABLED)
        self.save.pack(side=tk.LEFT, padx=2, pady=2)

        self.toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Images frame
        self.imgFrame = tk.Frame(self.master)
        self.imgFrame.pack()

        # Original image frame
        self.original = tk.Frame(self.imgFrame)
        self.original.pack(side=tk.LEFT, padx=45)
        self.originalLabel = tk.Label(self.original, text="ORIGINAL IMAGE", anchor=tk.CENTER)
        self.originalLabel.pack(side=tk.TOP, fill=tk.BOTH)
        self.originalImage = tk.Label(self.original, text="No image opened", anchor=tk.CENTER, fg=Palette.GRAY)
        self.originalImage.pack(side=tk.BOTTOM)

        # Modified image frame
        self.modified = tk.Frame(self.imgFrame)
        self.modified.pack(side=tk.LEFT, padx=45)
        self.modifiedLabel = tk.Label(self.modified, text="MODIFIED IMAGE", anchor=tk.CENTER)
        self.modifiedLabel.pack(side=tk.TOP, fill=tk.BOTH)
        self.modifiedImage = tk.Label(self.modified, text="No image opened", anchor=tk.CENTER, fg=Palette.GRAY)
        self.modifiedImage.pack(side=tk.BOTTOM)

        # Status bar
        self.currentStatus = tk.StringVar()
        self.currentStatus.set("Preparing to do stuff...")
        self.status = tk.Label(self.master, textvariable=self.currentStatus, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    @staticmethod
    def openFilePicker():
        filename = askopenfilename()
        if filename:
            return filename

    @staticmethod
    def enableImageMenus(self, isEnabled):
        if isEnabled:
            self.save.config(state="normal")
            self.menu.entryconfig(2, state="normal")
            self.subMenu.entryconfig(2, state="normal")

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

    @staticmethod
    def insertModifiedImage(self, img):
        self.photo = img # keeping image reference for safety reasons

        if hasattr(self, 'modifiedImage'):
            # clearing old modified image
            # works only one-way for now - filters doesn't stack up
            self.modifiedImage.destroy()

            # inserting new modified image
            self.modifiedImage = tk.Label(self.modified, image=self.photo)
            self.modifiedImage.pack(side=tk.BOTTOM)

    @staticmethod
    def setStatus(self, filterName):
        if filterName:
            label = "Applying " + filterName + " filter..."
        else:
            label = "Preparing to do stuff..."
        self.currentStatus.set(label)
        self.status.update_idletasks()