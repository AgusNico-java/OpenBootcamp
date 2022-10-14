def __main__():
    f = open('MiArchivo.txt', 'w')
    textoArchivo = input("Ingrese el texto a guardar: ")
    f.write(textoArchivo)
    f.close()

    f = open('MiArchivo.txt', 'r')
    lecturaArchivo = f.readline()
    f.close()
    print(lecturaArchivo)

if __name__ == '__main__':
    __main__()

