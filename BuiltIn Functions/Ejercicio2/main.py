from functools import reduce

def esImpar(num):
    if (num % 2) != 0:
        return True
    return False

def __main__():

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    listaImpar = filter(esImpar, lista)

    resultado = reduce(lambda num1, num2: num1 + num2, listaImpar)
    print(f'El resultado de sumar los numeros impares de la lista es {resultado}')

if __name__ == '__main__':
    __main__()