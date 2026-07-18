import os


class VistaLectura:


    def limpiar(self):

        os.system(
            "cls" if os.name == "nt" else "clear"
        )


    def dibujar(self, titulo="Libro seleccionado"):

        self.limpiar()


        print("┌──────────────────────────────────────────────────────────────────────────────────────────────┐")
        print("│                                                                                              │")
        print("│                              LECTURA DEL LIBRO                                               │")
        print("│                                                                                              │")
        print("├──────────────────────────────────────────────────────────────────────────────────────────────┤")
        print("│                                                                                              │")
        print(f"│                              {titulo:<50}│")
        print("│                                                                                              │")
        print("│  ┌────────────────────────────────────────────────────────────────────────────────────────┐  │")
        print("│  │                                                                                        │  │")
        print("│  │                                                                                        │  │")
        print("│  │                                                                                        │  │")
        print("│  │                  CONTENIDO DEL LIBRO                                                    │  │")
        print("│  │                                                                                        │  │")
        print("│  │                                                                                        │  │")
        print("│  │                                                                                        │  │")
        print("│  └────────────────────────────────────────────────────────────────────────────────────────┘  │")
        print("│                                                                                              │")
        print("├──────────────────────────────────────────────────────────────────────────────────────────────┤")
        print("│                                                                                              │")
        print("│                              MENÚ DE COMANDOS                                                │")
        print("│                                                                                              │")
        print("│  ┌────────────────────────────────────────────────────────────────────────────────────────┐  │")
        print("│  │ 1. me_gusta_libro                                                                       │  │")
        print("│  │    Permite guardar tus libros favoritos                                                  │  │")
        print("│  │                                                                                        │  │")
        print("│  │ 2. devolver_libro                                                                        │  │")
        print("│  │    Devuelve el libro prestado y regresa al menú principal                                │  │")
        print("│  └────────────────────────────────────────────────────────────────────────────────────────┘  │")
        print("│                                                                                              │")
        print("├──────────────────────────────────────────────────────────────────────────────────────────────┤")
        print("│                                                                                              │")
        print("│                                                                                              │")
        print("│                                                                                              │")
        print("└──────────────────────────────────────────────────────────────────────────────────────────────┘")



    def pedirComando(self):

        comando = input(
            "\ncomando> "
        )

        return comando.lower().strip()