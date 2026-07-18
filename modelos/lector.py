from modelos.favoritos import Favoritos
class Lector:
    def __init__(self, nombre, correo, contrasenia, biblioteca):
        self.nombre = nombre
        self.correo = correo
        self.contrasenia = contrasenia
        self.historialLectura = []
        self.listaFavoritos = Favoritos()
        self.biblioteca = biblioteca
    def registrarse(self):
        print("\n====== REGISTRO DE LECTOR ======")
        self.nombre = input("Nombre: ")
        self.correo = input("Correo: ")
        self.contrasenia = input("Contraseña: ")
        self.biblioteca.listaLectores.append(self)
        print("Usuario registrado correctamente")
        
    def filtrarLibros(self):
        libros = self.biblioteca.obtenerLibros()
        categoria = input("Ingrese categoría a buscar: ")
        encontrados = []
        for libro in libros:
            if libro.categoria.lower() == categoria.lower():
                encontrados.append(libro)
        if len(encontrados) == 0:
            print("No existen libros con esa categoría")
        else:
            print("\nLibros encontrados:")
            for libro in encontrados:
                print(
                    f"- {libro.titulo}"
                )
    def leerLibro(self):
        libros = self.biblioteca.obtenerLibros()
        print("\n====== LIBROS DISPONIBLES ======")
        for indice, libro in enumerate(libros, start=1):
            print(
                f"{indice}. {libro.titulo}"
            )
        opcion = int(
            input("Seleccione libro: ")
        )
        if opcion < 1 or opcion > len(libros):
            print("Opción incorrecta")
            return
        libro = libros[opcion - 1]
        self.historialLectura.append(libro)
        print("\nLeyendo:")
        print(libro.titulo)
    def agregarFavoritos(self):
        libros = self.biblioteca.obtenerLibros()
        print("\n====== LIBROS ======")
        for indice, libro in enumerate(libros, start=1):
            print(
                f"{indice}. {libro.titulo}"
            )
        opcion = int(
            input("Seleccione libro favorito: ")
        )
        libro = libros[opcion - 1]
        self.listaFavoritos.guardarLibro(libro)
        print(
            "Libro agregado a favoritos"
        )
    def modificarDatos(self):
        print("\n====== MODIFICAR DATOS ======")
        nuevoNombre = input(
            "Nuevo nombre: "
        )
        nuevoCorreo = input(
            "Nuevo correo: "
        )
        self.nombre = nuevoNombre
        self.correo = nuevoCorreo
        print(
            "Datos modificados correctamente"
        )