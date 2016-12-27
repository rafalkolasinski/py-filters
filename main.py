import Tkinter as tk
from src.Gui import Gui

# main func running all of the stuff
def main():
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
