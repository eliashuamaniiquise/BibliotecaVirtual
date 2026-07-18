import os


class VistaBiblioteca:


    def limpiar(self):

        os.system(
            "cls" if os.name == "nt" else "clear"
        )


    def dibujar(self):

        self.limpiar()


        print("┌──────────────────────────────────────────────────────────────────────────────────────────────┐")
        print("│                                                                                              │")
        print("│                                  LA BIBLIOTECA                                               │")
        print("│                                                                                              │")
        print("├───────────────────────────────────────────────────────────────┬──────────────────────────────┤")
        print("│                                                               │                              │")
        print("│                     CATEGORÍA DE LIBROS                      │           USUARIO            │")
        print("│                                                               │                              │")
        print("│ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌────────┐ │ ┌──────────────────────────┐ │")
        print("│ │ categoria 1  │ │ categoria 2  │ │ categoria 3  │ │ cat 4  │ │ │ Usuario activo           │ │")
        print("│ │              │ │              │ │              │ │        │ │ └──────────────────────────┘ │")
        print("│ └──────────────┘ └──────────────┘ └──────────────┘ └────────┘ │                              │")
        print("│                                                               │                              │")
        print("├───────────────────────────────────────────────────────────────┤ ┌──────────────────────────┐ │")
        print("│                                                               │ │ FILTROS                 │ │")
        print("│                       LIBROS FAVORITOS                        │ └──────────────────────────┘ │")
        print("│                                                               │                              │")
        print("│ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌────────┐ │ ┌──────────────────────────┐ │")
        print("│ │   libro 1    │ │   libro 2    │ │   libro 3    │ │libro 4 │ │ │ FILTROS                 │ │")
        print("│ │              │ │              │ │              │ │        │ │ └──────────────────────────┘ │")
        print("│ └──────────────┘ └──────────────┘ └──────────────┘ └────────┘ │                              │")
        print("│                                                               │ ┌──────────────────────────┐ │")
        print("│                                                               │ │ FILTROS                 │ │")
        print("│                                                               │ └──────────────────────────┘ │")
        print("│                                                               │                              │")
        print("│                                                               │ ┌──────────────────────────┐ │")
        print("│                                                               │ │ FILTROS                 │ │")
        print("│                                                               │ └──────────────────────────┘ │")
        print("├───────────────────────────────────────────────────────────────┴──────────────────────────────┤")
        print("│                                                                                              │")
        print("│                              MENÚ DE COMANDOS                                                │")
        print("│                                                                                              │")
        print("│  filtro           → Permite ingresar filtros que deseas                                      │")
        print("│  nombre_libro     → Permite leer un libro específico                                         │")
        print("│  salir            → Permite salir del sistema                                                │")
        print("│                                                                                              │")
        print("├──────────────────────────────────────────────────────────────────────────────────────────────┤")
        print("│                                                                                              │")
        print("│                                                                                              │")
        print("└──────────────────────────────────────────────────────────────────────────────────────────────┘")



    def pedirComando(self):

        comando = input(
            "\ncomando> "
        )

        return comando.lower().strip()