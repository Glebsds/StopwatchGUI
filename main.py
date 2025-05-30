import tkinter as tk
from StopwatchGUI import StopwatchGUI

def main():
    root = tk.Tk()
    root.title("Секундомер")
    app = StopwatchGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()