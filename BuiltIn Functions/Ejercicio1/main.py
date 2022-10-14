
def __main__():
    string = input("Ingrese una lista de paises separados por comas: ")

    listaDePaises = string.title().split(',')

    setDePaises = convertirASet(listaDePaises)
    listaDePaises = sorted(convertirALista(setDePaises))

    string = ', '.join(listaDePaises)

    print(string)


def convertirASet(lista):
    set = {''}
    for elemento in lista:
        set.add(elemento.strip())
    set.remove('')
    return set

def convertirALista(set):
    lista = []
    for elemento in set:
        lista.append(elemento)
    return lista

if __name__ == '__main__':
    __main__()
