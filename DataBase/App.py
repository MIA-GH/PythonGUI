import tkinter as tk
import sqlite3


class MyApp():
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Database')
        self.parent.iconbitmap('DataBase/icono.ico')
        
    def initUI(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    App = MyApp(root)
    root.mainloop()
    