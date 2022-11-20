#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

import db


class TelamainApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.configure(height=200, width=200)
        self.toplevel1.geometry("480x320")
        self.toplevel1.title("Test Tkinter")
        self.progressbar1 = ttk.Progressbar(self.toplevel1)
        self.cvar = tk.StringVar()
        self.progressbar1.configure(orient="horizontal", variable=self.cvar)
        self.progressbar1.pack(side="top")
        self.entry1 = ttk.Entry(self.toplevel1)
        self.entry1.configure(
            font="{Arial} 12 {}",
            justify="left",
            textvariable=self.cvar)
        _text_ = '10'
        self.entry1.delete("0", "end")
        self.entry1.insert("0", _text_)
        self.entry1.pack(side="top")
        self.button1 = ttk.Button(self.toplevel1)
        self.button1.configure(takefocus=True, text='OK')
        self.button1.pack(side="top")
        self.button1.bind("<ButtonPress>", self.btClick, add="+")
        self.menu1 = tk.Menu(self.toplevel1)
        self.menu1.configure(
            font="{Arial} 14 {}",
            foreground="#ffffff",
            selectcolor="#c0c0c0",
            title='Menu')
        self.toplevel1.configure(menu=self.menu1)
        self.text2 = tk.Text(self.toplevel1)
        self.text2.configure(height=10, width=50, wrap="word")
        _text_ = 'variavel aqui'
        self.text2.insert("0.0", _text_)
        self.text2.pack(side="top")
        self.toplevel1.pack_propagate(0)

        # Main widget
        self.mainwindow = self.toplevel1

    def run(self):
        self.mainwindow.mainloop()

    def btClick(self, event=None):
        self.text2.delete("0.0", "1000.1000")
        self.text2.insert("0.0", db.connect()[0])


if __name__ == "__main__":
    app = TelamainApp()
    app.run()
