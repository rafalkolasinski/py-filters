from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import Image


class GuiCSImages:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        filename = askopenfilename()

        image = Image.open(filename)
        # @TODO: print different image details depending on image format
        # print("BITS " + str(image.bits) + " SIZE " + str(image.size) + " FORMAT " + image.format)

root = Tk()
gcsi = GuiCSImages(root)
root.mainloop()