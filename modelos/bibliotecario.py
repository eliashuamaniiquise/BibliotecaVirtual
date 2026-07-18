class Bibliotecario:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        
    def agregarLibros(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        categoria = input("Categoría: ")
        year = int(input("Año: "))
        estado = input("Estado: ")
        contenido = input("Contenido: ")
        nuevo_libro = self.biblioteca.crearLibro(
            titulo,
            autor,
            categoria,
            year,
            estado,
            contenido
        )
        print("Libro agregado correctamente")
    def clasificarLibro(self):
        libros = self.biblioteca.obtenerLibros()
        if len(libros) == 0:
            print("No hay libros disponibles")
            return
        print("\n====== LIBROS DISPONIBLES ======\n")
        for indice, libro in enumerate(libros, start=1):
            print(
                f"{indice}. {libro.titulo} "
                f"- Categoría: {libro.categoria}"
            )
        opcion = int(input("\nSeleccione libro: "))
        if opcion < 1 or opcion > len(libros):
            print("Opción incorrecta")
            return
        libroSeleccionado = libros[opcion - 1]
        print("\nLibro seleccionado:")
        print(libroSeleccionado.titulo)
        nuevaCategoria = input("Nueva categoría: ")
        libroSeleccionado.categoria = nuevaCategoria
        print("Libro clasificado correctamente")
        
    def eliminarLibro(self):
        libros = self.biblioteca.obtenerLibros()
        if len(libros) == 0:
            print("No hay libros disponibles")
            return
        print("\n====== LIBROS DISPONIBLES ======\n")
        for indice, libro in enumerate(libros, start=1):
            print(
                f"{indice}. {libro.titulo} "
                f"- Categoría: {libro.categoria}"
            )
        opcion = int(input("\nSeleccione el libro a eliminar: "))
        if opcion < 1 or opcion > len(libros):
            print("Opción inválida")
            return
        libroEliminado = libros[opcion - 1]
        libros.remove(libroEliminado)
        print(
            f"\nLibro eliminado correctamente: "
            f"{libroEliminado.titulo}"
        )