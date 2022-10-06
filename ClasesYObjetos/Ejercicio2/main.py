class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrarAlumno(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def isAprobado(self):
        if self.nota >= 7 and self.nota <= 10:

            print("Nota:", self.nota ,". El alumno ha aprobado.")
        elif self.nota >= 1 and self.nota < 7:
            print("Nota:", self.nota ,". El alumno ha desaprobado")
        else:
            print("La nota no es válida.")