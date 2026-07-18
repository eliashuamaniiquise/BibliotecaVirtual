from modelos.libro import Libro


class Biblioteca:

    def __init__(self):
        self.listaLibros = []
        self.listaLectores = []
        self.sesionActual = None
        self.cargarLibros()
    def crearLibro(self, titulo, autor, categoria, year, estado, contenido):

        nuevo_libro = Libro(
            titulo,
            autor,
            categoria,
            year,
            estado,
            contenido
        )

        self.listaLibros.append(nuevo_libro)

        return nuevo_libro
    def cargarLibros(self):

        libro1 = Libro(
            "Los Tres Cerditos",
            "Anónimo",
            "Cuentos infantiles",
            1843,
            "Disponible",
            """
            Historia de tres cerditos que construyen casas
            para protegerse de un lobo.
            """
        )


        libro2 = Libro(
            "Drácula",
            "Bram Stoker",
            "Terror",
            1897,
            "Disponible",
            """
            Historia del Conde Drácula y su encuentro
            con Jonathan Harker.
            """
        )

        libro3 = Libro(
            "El Principito",
            "Antoine de Saint-Exupéry",
            "Fantasía",
            1943,
            "Disponible",
            """
            Un pequeño príncipe viaja por diferentes planetas descubriendo nuevos amigos
            y aprendiendo sobre la amistad, el amor y la importancia de ver más allá de
            las apariencias.
            """
        )

        libro4 = Libro(
            "Cien años de soledad",
            "Gabriel García Márquez",
            "Realismo mágico",
            "Disponible",
            """
            Relata la historia de la familia Buendía durante varias generaciones en el
            pueblo ficticio de Macondo, mezclando hechos reales con elementos mágicos.
            """
        )

        libro5 = Libro(
            "El Resplandor",
            "Stephen King",
            "Terror psicológico",
            1977,
            "Disponible",
            """
            Jack Torrance acepta trabajar como cuidador de un hotel aislado durante el
            invierno. Allí descubre fuerzas sobrenaturales que afectan a su familia.
            """
        )


        libro6 = Libro(
            "Harry Potter y la piedra filosofal",
            "J.K. Rowling",
            "Fantasía",
            1997,
            "Disponible",
            """
            Harry Potter descubre que pertenece al mundo mágico y comienza sus estudios
            en Hogwarts, donde conocerá amigos y enfrentará grandes peligros.
            """
        )

        libro7 = Libro(
            "Don Quijote de la Mancha",
            "Miguel de Cervantes",
            "Novela clásica",
            1605,
            "Disponible",
            """
            Narra las aventuras de Alonso Quijano, quien después de leer muchos libros de
            caballería decide convertirse en caballero andante junto a Sancho Panza.
            """
        )

        libro8 = Libro(
            "La Odisea",
            "Homero",
            "Mitología",
            -800,
            "Disponible",
            """
            Cuenta el largo viaje de regreso de Odiseo a su hogar después de la guerra de
            Troya, enfrentando criaturas y desafíos mitológicos.
            """
        )

        libro9 = Libro(
            "1984",
            "George Orwell",
            "Ciencia ficción",
            1949,
            "Disponible",
            """
            Una sociedad controlada por un gobierno totalitario vigila constantemente a
            sus ciudadanos. Winston Smith intenta descubrir la verdad.
            """
        )

        libro10 = Libro(
            "El Hobbit",
            "J.R.R. Tolkien",
            "Fantasía épica",
            1937,
            "Disponible",
            """
            Bilbo Bolsón emprende una aventura junto a un grupo de enanos para recuperar
            un reino perdido custodiado por el dragón Smaug.
            """
        )
        self.listaLibros.append(libro1)
        self.listaLibros.append(libro2)
        self.listaLibros.append(libro3)
        self.listaLibros.append(libro4)
        self.listaLibros.append(libro5)
        self.listaLibros.append(libro6)
        self.listaLibros.append(libro7)
        self.listaLibros.append(libro8)
        self.listaLibros.append(libro9)
        self.listaLibros.append(libro10)

    def obtenerLibros(self):

        return self.listaLibros



    def agregarLibro(self, libro):

        self.listaLibros.append(libro)