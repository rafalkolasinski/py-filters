import Gui
from PIL import Image, ImageTk
import numpy as np

class Filters(object):

    def __init__(self):
        # self.ih = ih.ImageHandler()
        print "CON: **Filters init**"

    def blur(self, imageHandlerRef, guiRef):
        # @TODO: drastically improve performance, implement threads

        # default values, controlled separately in future releases
        blurWidth = 7
        blurHeight = 7
        # testing motion blur; matrix rows/columns number must be odd to leave one pixel in the center
        matrix = np.array([
            [1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1]
        ])
        # matrix = np.array([
        #     [0, 0, 1, 0, 0],
        #     [0, 1, 1, 1, 0],
        #     [1, 1, 1, 1, 1],
        #     [0, 1, 1, 1, 0],
        #     [0, 0, 1, 0, 0]
        # ])
        # matrix = np.array([
        #     [0, 1, 0],
        #     [1, 1, 1],
        #     [0, 1, 0]
        # ])
        # change factor var to multiply the values (default: 1.0)
        factor = 1.0 / 7
        # change bias var to make image brighter/darker (default: 0.0)
        bias = 0.0
        image = imageHandlerRef.getRawImage()
        originalPixels = list(np.array(image))
        size = width, height = image.size
        result = np.copy(originalPixels)
        resultPixels = np.array(result)

        for x in range(height):
            for y in range(width):
                red = 0.0
                green = 0.0
                blue = 0.0

                for filterX in range(0, blurHeight):
                    for filterY in range(0, blurWidth):
                        imageX = (x - blurWidth / 2 + filterX + width) % width
                        imageY = (y - blurHeight / 2 + filterY + height) % height

                        red += originalPixels[imageX][imageY][0] * matrix[filterX, filterY]
                        green += originalPixels[imageX][imageY][1] * matrix[filterX, filterY]
                        blue += originalPixels[imageX][imageY][2] * matrix[filterX, filterY]

                resultPixels[x, y][0] = min(max((factor * red + bias), 0), 255)
                resultPixels[x, y][1] = min(max((factor * green + bias), 0), 255)
                resultPixels[x, y][2] = min(max((factor * blue + bias), 0), 255)

        result = Image.fromarray(resultPixels)
        image2 = ImageTk.PhotoImage(result)
        Gui.Gui.insertModifiedImage(guiRef, image2)
        print "CON: **Finished applying blur**"

    def grayscale(self, imageHandlerRef, guiRef):
        factor = 1.0 # @TODO: add custom factor handler (gui slider)
        originalPixels = imageHandlerRef.getPixels()
        image = imageHandlerRef.getRawImage()
        size = width, height = image.size
        resultPixels = np.copy(originalPixels)

        for x in range(0, height):
            for y in range(0, width):
                avg = 0.0

                for rgb in range(0, 3):
                    avg += originalPixels[x][y][rgb]

                originalPixels[x][y][:3] = avg / 3 * factor

        finalImage = Image.fromarray(originalPixels)
        resultTk = ImageTk.PhotoImage(finalImage)
        Gui.Gui.insertModifiedImage(guiRef, resultTk)
        print "CON: **Finished applying grayscale**"
