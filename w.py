import tkinter as tk  
import numpy as np
import pandas as pd

class word(object):
    def __init__(self,DB):
        self.df = pd.read_excel(DB)
        self.window = tk.Tk()
        self.window.title('Remember a word better!')
        self.window.geometry('300x300')
        self.event()
        self.window.mainloop()

    def event(self):
        self.index = np.random.randint(1, len(self.df))
        self.word = self.df.loc[self.index]
        self.var = tk.StringVar()    
        self.l = tk.Label(self.window, bg='yellow', width=35, text=self.word['English'])
        self.ll = tk.Label(self.window, bg='yellow', width=35)
        self.l.pack()
        self.ll.pack()
        choice = []
        for i in range(4):
            choice.append(np.random.randint(1, len(self.df)))
        self.correct_answer = np.random.randint(1,5)
        choice[self.correct_answer - 1] = self.index
        self.r = [None,None,None,None]
        for i in range(1,5):
            self.r[i - 1] = tk.Radiobutton(self.window, text=self.df.loc[choice[i-1]]['Chinese'], variable=self.var, value=choice[i-1], command=self.check)
            self.r[i-1].pack()

        self.B = tk.Button(self.window, text='Next', width=10, height=2, command=self.next_word)
        self.B.pack()

    def check(self):
        if int(self.var.get()) != self.index:
            self.ll.config(text='Wrong')
        else:
            self.ll.config(text='Correct')
    
    def next_word(self):
        self.l.pack_forget()
        self.ll.pack_forget()
        for i in range(1,5):
            self.r[i-1].pack_forget()
        self.B.pack_forget()
        self.window.after(100, self.event)

if __name__ == '__main__':
    sa = word('word.xlsx')
    
