import tkinter
from tkinter import ttk

def __main__():
    paisesDeOrigen = ["Argentina", "Brasil", "España", "Uruguay", "Italia", "Francia"]

    window = tkinter.Tk()
    window.columnconfigure(0, weight=2)
    window.columnconfigure(1, weight=2)
    window.columnconfigure(2, weight=2)

    label = tkinter.Label(window, text="Lista de Paises", )
    label.grid(column=1, row=0, sticky='N')

    mostrarLista = tkinter.StringVar(value=paisesDeOrigen)

    listbox = tkinter.Listbox(window, height=6, listvariable=mostrarLista)
    listbox.grid(column=0, row=1, sticky='W')

    window.mainloop()

if __name__ == '__main__':
    __main__()
