import Tkinter as tk
from src.Gui import Gui

# main func running all of the stuff
def main():
    root = tk.Tk()
    # commented for dev purposes
    # root.wm_state("zoomed")

    # window size hardcoded for dev purposes
    root.geometry("{}x{}".format(640, 480))
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.wm_geometry("+" + str(w-750) + "+" + str(h-650))


    app = Gui(root)
    print "CON: Running main window"
    root.mainloop()

if __name__ == "__main__":
    main()
