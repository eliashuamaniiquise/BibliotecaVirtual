from persona import Persona
from libro import Libro,libro1
class Lector(Persona):
    def __init__(self,listaFaboritos,historialLectura,libroActual):
        self.listaFaboritos=listaFaboritos
        self.historialLectura=historialLectura
        self.libroActual=libroActual
    def buscarLibro(self):
        buscador=input("ingresa el nombre del libro")
        encontrado=False
        for libro in lista_de_libros:
            if libro.titulo==buscador:
                encontrado=True
                break
            else:
                print("no lo encontro")
        print("encontrado libro que buscas")
    def mostrarInformacion(self):
        pass
    def modificarDatos(self):
        pass
lista_de_libros=[libro1]

lector1=Lector("1","2","3")
lector1.buscarLibro()


