import tkinter as tk
from tkinter import ttk

class MainApp():
    def __init__(self, master):
        self.master = master
        self.master.title('Food Price')
        self.master.geometry("300x200")
        self.master.resizable(False, False)
        self.master.iconbitmap("FoodPrice/icono.ico")
        self.v = tk.IntVar()
        self.result = tk.IntVar()
        self.MainLabel()
        self.DesignUI()
        self.createInputBox()

    def calculatePrice(self):
        self.value = self.v.get()
        try:
            self.NumberToBuy = int(self.QuantityBox.get())
            if self.value == 0:
                self.amount = self.NumberToBuy * 4 
                self.result.set(self.amount)           
            elif self.value == 1:
                self.amount = self.NumberToBuy * 6 
                self.result.set(self.amount)  
            elif self.value == 2:
                self.amount = self.NumberToBuy * 10 
                self.result.set(self.amount)  
            else:
                return None
        except ValueError:
            pass

    def MainLabel(self):
        self.titleLabel = tk.ttk.Label(self.master, text="Select a food Item")
        self.titleLabel.place(x=95, y=5)

    def DesignUI(self):
        self.itemOne = tk.ttk.Radiobutton(self.master, text="Banana", variable=self.v, value=0)
        self.itemOne.place(x=5, y=30)

        self.itemtwo = tk.ttk.Radiobutton(self.master, text="Orange", variable=self.v, value=1)
        self.itemtwo.place(x=5, y=60)

        self.itemthree = tk.ttk.Radiobutton(self.master, text="Apple", variable=self.v, value=2)
        self.itemthree.place(x=5, y=90)

    def createInputBox(self):
        self.priceLabel = tk.ttk.Label(self.master, text="Price")
        self.priceLabel.place(x=30, y=130)

        self.priceBox = tk.ttk.Entry(self.master, width=25, textvariable=self.result)
        self.priceBox.place(x=100, y=130)

        self.calButton = tk.ttk.Button(self.master, text="Cal", command=lambda: self.calculatePrice())
        self.calButton.place(x=20, y=165)

        self.QuantityBox = tk.ttk.Entry(self.master, width=25)
        self.QuantityBox.place(x=100, y=165)


if __name__ == "__main__":
    root = tk.Tk()
    myApp = MainApp(root)
    root.mainloop()

