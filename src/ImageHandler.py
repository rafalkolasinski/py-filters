import Gui
from PIL import Image

class ImageHandler(object):

    def __init__(self):
        # self.gui = Gui.Gui()
        self.imagePath = ""

    @staticmethod
    def openImage():
        """
        self.setImagePath(Gui.Gui)
        image = Image.open(self.getImagePath())
        print(image)
        print("Opened the image from path: " + self.imagePath)
        """
        print("Opened the image.")

    @staticmethod
    def saveImage():
        print("Saved the image.")

    def getImage(self):
        return self.img

    def setImage(self, img):
        self.img = img

    def getImagePath(self):
        return self.imagePath

    def setImagePath(self, imagePath):
        self.imagePath = imagePath
