class Vehiculo:
    color = None
    ruedas = None
    puertas = None

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    velocidad = None
    Cilindrada = None

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

miCoche = Coche("Azul", 4, 5, 130, 1.6)
print("Color: ", miCoche.color, "\nCantidad de ruedas: ", miCoche.ruedas, "\nCantidad de puertas: ", miCoche.puertas, "\nVelocidad máxima: ", miCoche.velocidad, "\nCilindrada: ", miCoche.cilindrada)