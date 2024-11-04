import tkinter as tk
from management import Management


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Management")
        self.geometry("800x600")
        Management(self)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
