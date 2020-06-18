import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class CounterApp():
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Counter')
        self.parent.geometry("500x500")
        self.parent.iconbitmap("FileCounter/icono.ico")
        self.parent.resizable(False, False)
        self.CreateUI()

    def CountWords(self):
        try:
            self.fulltext = open(self.fileName, 'r')
            self.content = self.fulltext.readlines()
            self.word_list = dict()
            self.user_words = self.WordEntry.get().split(',')            
            for self.word in self.user_words:
                self.word = self.word.strip().lower()
                for self.text in self.content:
                    if self.word in self.word_list:
                        self.word_list[self.word] = self.word_list[self.word] + self.text.count(self.word)
                    else:
                        self.word_list[self.word] = self.text.count(self.word)
            for self.k, self.v in self.word_list.items():
                try:
                    self.ResultBox.insert('1.0', "{0} : {1}\n".format(self.k, self.v))
                except IndexError:
                    print("error found")
        except ValueError:
            pass
                

    def OpenFile(self):
        self.fileName = filedialog.askopenfilename()

    def CreateUI(self):
        self.intruction = tk.ttk.Label(self.parent, text="Enter word(s) to count for")
        self.intruction.place(x=150, y=5)
        self.WordEntry = tk.ttk.Entry(self.parent, width=80)
        self.WordEntry.place(x=5, y=30)

        self.selectFileBtn = tk.ttk.Button(self.parent, text="Select File", width=80, command=self.OpenFile)
        self.selectFileBtn.place(x=5, y=65)

        self.CountWordsBtn = tk.ttk.Button(self.parent, text="Count Words", width=80, command=lambda: self.CountWords())
        self.CountWordsBtn.place(x=5, y=105)

        self.ClearBtn = tk.ttk.Button(self.parent, text="Clear", width=80, command=self.clearFields)
        self.ClearBtn.place(x=5, y=145)

        self.ResultBox = tk.Text(self.parent, height=19, width=60)
        self.ResultBox.place(x=5, y=180)

    def clearFields(self):
        self.WordEntry.delete(0, 'end')
        self.ResultBox.delete('1.0', 'end')
        

if __name__ == "__main__":
    root = tk.Tk()
    App = CounterApp(root)
    root.mainloop()
