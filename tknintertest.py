#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class Janela:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(height=200, width=200)
        toplevel1.geometry("320x200")
        progressbar1 = ttk.Progressbar(toplevel1)
        self.cvar = tk.StringVar()
        progressbar1.configure(orient="horizontal", variable=self.cvar)
        progressbar1.pack(side="top")
        entry1 = ttk.Entry(toplevel1)
        entry1.configure(textvariable=self.cvar)
        _text_ = '10'
        entry1.delete("0", "end")
        entry1.insert("0", _text_)
        entry1.pack(side="top")
        button1 = ttk.Button(toplevel1)
        button1.configure(text='OK')
        button1.pack(side="top")
        button1.bind("<ButtonPress>", self.la, add="")

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()

    def la(self, event=None):
        soma = int(self.cvar.get()) + 10
        print(type(soma))
        self.cvar.set(str(soma))


if __name__ == "__main__":
    app = Janela()
    app.run()
