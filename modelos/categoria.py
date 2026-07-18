from libro import Libro,libro1
class Categoria:
    def __init__(self,nombre=str,descripcion=str,libros=[]):
        self.nombre=nombre
        self.descripcion=descripcion
        self.libros=libros
    def agregarLibro(self,libro_objeto):
        if isinstance(libro_objeto,Libro):
            self.libros.append(libro_objeto)
            print(f"guardaste los libros")
        else:
            print("no se guarado los libros")
# eliminarLibro()
#   Elimina un libro de la categoría.
# buscarLibro()
#   Busca un libro dentro de esa categoría.
# mostrarLibros()
#   Muestra todos los libros pertenecientes a la categoría.
# mostrarInformacion()
#   Muestra el nombre y la descripción de la categoría.
mi_categoria=Categoria("cuentos infantiles")
mi_categoria.agregarLibro(libro1)
print("\nContenido de la lista de libros:")
for libro in mi_categoria.libros:
    print(f"- {libro.titulo} ({libro.autor})")