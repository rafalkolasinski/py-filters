import Gui
from PIL import Image, ImageTk
import Tkinter as tk

class ImageHandler(object):

    def __init__(self):
        self.imagePath = ""

    def openImage(self, gui):
        path = Gui.Gui.openFilePicker()
        if path:
            # setting image path
            self.setImagePath(path)

            # loading the image from specified path
            image = Image.open(self.getImagePath())
            imageTk = ImageTk.PhotoImage(image)
            self.setImage(imageTk)
            print "CON: **Got image**", image

            # inserting image into GUI
            Gui.Gui.insertOriginalImage(gui, imageTk)
        else:
            print "CON: **Canceled image loading**"

    def saveImage(self):
        print "CON: **Saved the image**"

    def getImage(self):
        return self.img

    def setImage(self, img):
        self.img = img

    def getImagePath(self):
        return self.imagePath

    def setImagePath(self, imagePath):
        self.imagePath = imagePath
