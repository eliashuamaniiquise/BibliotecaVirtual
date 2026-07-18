class Favoritos:
    def __init__(self):
        self.librosFavoritos = []
    def guardarLibro(self, libro):
        self.librosFavoritos.append(libro)
        print(
            f"Libro agregado a favoritos: {libro.titulo}"
        )
    def quitarLibro(self, libro):
        if libro in self.librosFavoritos:
            self.librosFavoritos.remove(libro)
            print(
                f"Libro eliminado de favoritos: {libro.titulo}"
            )
        else:
            print("El libro no está en favoritos")
    def mostrarFavoritos(self):
        if len(self.librosFavoritos) == 0:
            print("No tienes libros favoritos")
            return
        print("\n====== MIS FAVORITOS ======")
        for indice, libro in enumerate(self.librosFavoritos, start=1):
            print(f"{indice}. {libro.titulo}" )