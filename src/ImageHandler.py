import Gui
from PIL import Image, ImageTk
import numpy as np

class ImageHandler(object):

    def __init__(self):
        self.imagepath = ""
        self.imgraw = None
        self.imgtk = None
        self.red = []
        self.green = []
        self.blue = []
        self.pixels = []

    def openImage(self, guiRef):
        path = Gui.Gui.openFilePicker()
        if path:
            # setting image path
            self.setImagePath(path)

            # loading the image from specified path -> storing PIL version of image
            image = Image.open(self.getImagePath())
            self.setRawImage(image)

            # setting the image RGB channels/pixel list
            pixels = np.array(image)
            self.setPixels(pixels)
            self.setRGBChannels(pixels)

            # storing Tkinter version of image
            imageTk = ImageTk.PhotoImage(image)
            self.setImageTk(imageTk)

            # inserting image into GUI
            Gui.Gui.insertOriginalImage(guiRef, imageTk)

            print "CON: **Got image**", image
        else:
            print "CON: **Canceled image loading**"

    def saveImage(self):
        print "CON: **Saved the image**"

    def getRawImage(self):
        return self.imgraw

    def setRawImage(self, img):
        self.imgraw = img

    def getImageTk(self):
        return self.imgtk

    def setImageTk(self, img):
        self.imgtk = img

    def getImagePath(self):
        return self.imagepath

    def setImagePath(self, imagePath):
        self.imagepath = imagePath

    def setRGBChannels(self, image):
        self.red = np.copy(image)
        self.green = np.copy(image)
        self.blue = np.copy(image)
        self.red[:,:,1] *= 0
        self.red[:,:,2] *= 0
        self.green[:,:,0] *= 0
        self.green[:,:,2] *= 0
        self.blue[:,:,0] *= 0
        self.blue[:,:,1] *= 0

    def getRGBChannels(self):
        return np.array([self.red, self.green, self.blue])

    def setPixels(self, pixels):
        self.pixels = pixels

    def getPixels(self):
        return self.pixels