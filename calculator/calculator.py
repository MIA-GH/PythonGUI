import tkinter as tk
from tkinter import ttk

class Calculator():
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Calculator')
        self.parent.iconbitmap('calculator/icono.ico') # calculator\icono.ico
        self.add = False
        self.sub = False
        self.div = False
        self.mul = False
        self.CreateEntry()
        self.CreateButtons()


    def CreateEntry(self):
        self.entry = tk.ttk.Entry(self.parent, width=43)
        self.entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    def CreateButtons(self):
        self.Button_7 = tk.Button(self.parent, text='7', padx=40, pady=20, bg='gray', fg='white', command= lambda: self.ButtonClick(7))
        self.Button_7.grid(row=1, column=0)
        self.Button_8 = tk.Button(self.parent, text='8', padx=40, pady=20, bg='gray', fg='white', command= lambda: self.ButtonClick(8))
        self.Button_8.grid(row=1, column=1)
        self.Button_9 = tk.Button(self.parent, text='9', padx=40, pady=20, bg='gray', fg='white', command= lambda: self.ButtonClick(9))
        self.Button_9.grid(row=1, column=2)

        self.Button_4 = tk.Button(self.parent, text='4', padx=40, pady=20, bg='gray', fg='white', command= lambda: self.ButtonClick(4))
        self.Button_4.grid(row=2, column=0)
        self.Button_5 = tk.Button(self.parent, text='5', padx=40, pady=20, bg='gray', fg='white', command= lambda: self.ButtonClick(5))
        self.Button_5.grid(row=2, column=1)
        self.Button_6 = tk.Button(self.parent, text='6', padx=40, pady=20, bg='gray', fg='white', command= lambda: self.ButtonClick(6))
        self.Button_6.grid(row=2, column=2)

        self.Button_1 = tk.Button(self.parent, text='1', padx=40, pady=20, bg='gray', fg='white', command= lambda: self.ButtonClick(1))
        self.Button_1.grid(row=3, column=0)
        self.Button_2 = tk.Button(self.parent, text='2', padx=40, pady=20, bg='gray', fg='white', command= lambda: self.ButtonClick(2))
        self.Button_2.grid(row=3, column=1)
        self.Button_3 = tk.Button(self.parent, text='3', padx=40, pady=20, bg='gray', fg='white', command= lambda: self.ButtonClick(3))
        self.Button_3.grid(row=3, column=2)

        self.Button_add = tk.Button(self.parent, text='+', padx=40, pady=20, bg='purple', fg='white', command=self.AddButton)
        self.Button_add.grid(row=4, column=0)
        self.Button_0 = tk.Button(self.parent, text='0', padx=40, pady=20, bg='gray', fg='white', command= lambda: self.ButtonClick(0))
        self.Button_0.grid(row=4, column=1)
        self.Button_subtract = tk.Button(self.parent, text='-', padx=40, pady=20, bg='purple', fg='white', command=self.SubButton)
        self.Button_subtract.grid(row=4, column=2)

        self.Button_divide = tk.Button(self.parent, text='/', padx=41, pady=20, bg='purple', fg='white', command=self.DivButton)
        self.Button_divide.grid(row=5, column=0)
        self.Button_multiply = tk.Button(self.parent, text='x', padx=40, pady=20, bg='purple', fg='white', command=self.MulButton)
        self.Button_multiply.grid(row=5, column=1)
        self.Button_clear = tk.Button(self.parent, text='CE', padx=35, pady=20, bg='brown', fg='white', command=self.ClearField)
        self.Button_clear.grid(row=5, column=2)

        self.Button_equal = tk.Button(self.parent, text='=', padx=135, pady=20, bg='orange', fg='white', command=self.CalculateResults)
        self.Button_equal.grid(row=6, column=0, columnspan=3)

    def ClearField(self):
        self.entry.get()
        self.entry.delete(0, 'end')

    def ButtonClick(self, number):
        self.current = self.entry.get()
        self.entry.delete(0, 'end')
        self.entry.insert(0, str(self.current) + str(number))

    def AddButton(self):
        try:
            self.first = self.entry.get()
            self.first = float(self.first)
            self.entry.delete(0, 'end')
            self.add = True
        except ValueError:
            pass

    def SubButton(self):
        try :
            self.first = self.entry.get()
            self.first = float(self.first)
            self.entry.delete(0, 'end')
            self.sub = True
        except ValueError:
            pass

    def MulButton(self):
        try :
            self.first = self.entry.get()
            self.first = float(self.first)
            self.entry.delete(0, 'end')
            self.mul = True
        except ValueError:
            pass

    def DivButton(self):
        try:
            self.first = self.entry.get()
            self.first = float(self.first)
            self.entry.delete(0, 'end')
            self.div = True
        except ValueError:
            pass

    def CalculateResults(self):
        try :
            self.second = self.entry.get()
            self.second = float(self.second)
            self.entry.delete(0, 'end')
            if self.add == True:
                self.result = self.first + self.second
                self.add = False 
            elif self.sub == True:
                self.result = self.first - self.second 
                self.sub = False
            elif self.mul == True:
                self.result = self.first * self.second 
                self.mul = False
            elif self.div == True:
                self.result = self.first / self.second 
                self.div = False
            self.entry.insert(0, str(self.result))
        except ValueError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    MyApp = Calculator(root)
    root.mainloop()

        