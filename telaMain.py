#!/usr/bin/python3
import pathlib
import pygubu
from db import *
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "telaMain.ui"


class TelamainApp:
    def __init__(self, uifile="telaMain.ui", master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)

        self.cvar = None
        self.ctexto = None
        builder.import_variables(self, ['cvar', 'ctexto'])

        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def btClick(self, event=None):
        texto = ''
        banco = ConectarDB()
        Id = self.cvar.get()
        texto = banco.consultar_registro_pela_id(Id)
        self.ctexto.set(texto)
        print(self.ctexto.get())
        print(texto)

    def entryMove(self, event=None):
        self.cvar.set(str(int(self.cvar.get()) + 10))
    
    def exit(self):
        self.mainwindow.tk.quit() 
    
if __name__ == "__main__":
    app = TelamainApp()
    app.run()
