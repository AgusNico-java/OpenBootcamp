import pickle

def __main__():
    auto = Vehiculo(2, 140)
    f = open ('datos.bin', 'wb')
    pickle.dump(auto, f)
    f.close()

    f = open('datos.bin', 'rb')
    auto2 = pickle.load(f)
    f.close()
    print(f'Cantidad de Ruedas: {auto2.getCantidadDeRuedas()}\nVelocidad Maxima: {auto2.getVelocidadMaxima()}')

class Vehiculo():
    __cantidadDeRuedas__ = None
    __velocidadMaxima__ = None
    pass

    def __init__(self, cantidadDeRuedas, velocidadMaxima):
        self.__cantidadDeRuedas__ = cantidadDeRuedas
        self.__velocidadMaxima__ = velocidadMaxima

    def getCantidadDeRuedas(self):
        return self.__cantidadDeRuedas__

    def getVelocidadMaxima(self):
        return self.__velocidadMaxima__

if __name__ == '__main__':
    __main__()


