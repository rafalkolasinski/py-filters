from Tkinter import *


class GuiCSCanvas:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        canvas = Canvas(root, width = 300, height = 200)
        canvas.pack()

        # startingPointX, startingPointY, endingPointX, endingPointY
        # (+ fill param)
        blackLine = canvas.create_line(0, 0, 200, 50)
        redLine = canvas.create_line(0, 100, 200, 50, fill="red")

        whiteBox = canvas.create_rectangle(25, 25, 130, 60, fill="white")

        canvas.delete(redLine)

root = Tk()
gcsc = GuiCSCanvas(root)
root.mainloop()