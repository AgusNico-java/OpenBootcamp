import tkinter
from tkinter import ttk

def __main__():

    def selection():
        texto = f'Ha seleccionado la {str(selected.get())}'
        label.config(text=texto)

    def uncheck():
        selected.set(None)
        label.config(text="")

    window = tkinter.Tk()

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=4)

    selected = tkinter.StringVar()

    radioButton1 = ttk.Radiobutton(window, text="Opcion1", variable=selected, value="Opcion 1", command=selection)
    radioButton1.grid(column=0, row=0, sticky='w')

    radioButton2 = ttk.Radiobutton(window, text="Opcion2", variable=selected, value="Opcion 2", command=selection)
    radioButton2.grid(column=0, row=1, sticky='w')

    radioButton3 = ttk.Radiobutton(window, text="Opcion3", variable=selected, value="Opcion 3", command=selection)
    radioButton3.grid( column=0, row=2, sticky='w')

    button = ttk.Button(window, text="Eliminar todo", command=uncheck)
    button.grid(column=0, row=4, sticky='w')

    label = tkinter.Label(window)
    label.grid(column=0, row=3)

    window.mainloop()

if __name__ == '__main__':
    __main__()
