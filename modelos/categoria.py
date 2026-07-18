from modelos.libro import Libro
class Categoria:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.libros = []
        
    def agregarLibro(self, libro_objeto):
        if isinstance(libro_objeto, Libro):
            self.libros.append(libro_objeto)
            print(
                f"Libro agregado a la categoría: {self.nombre}"
            )
        else:
            print("El objeto no es un libro")
    def eliminarLibro(self, libro_objeto):
        if libro_objeto in self.libros:
            self.libros.remove(libro_objeto)
            print(f"Libro eliminado de la categoría: {self.nombre}")
        else:
            print("El libro no pertenece a esta categoría")
    def buscarLibro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None
    def mostrarLibros(self):
        print(
            f"\n====== LIBROS DE {self.nombre.upper()} ======"
        )

        if len(self.libros) == 0:
            print("No hay libros registrados")
            return
        for libro in self.libros:
            print(
                f"- {libro.titulo} ({libro.autor})"
            )
    def mostrarInformacion(self):
        print("\n====== INFORMACIÓN CATEGORÍA ======")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")