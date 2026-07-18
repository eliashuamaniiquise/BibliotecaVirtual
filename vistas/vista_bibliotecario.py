import os


class VistaBibliotecario:


    def limpiar(self):

        os.system(
            "cls" if os.name == "nt" else "clear"
        )


    def dibujar(self):

        self.limpiar()

        print("┌──────────────────────────────────────────────────────────────────────────────────────────────┐")
        print("│                                                                                              │")
        print("│                         BIENVENIDO BIBLIOTECARIO                                             │")
        print("│                                                                                              │")
        print("├───────────────────────────────────────────────┬──────────────────────────────────────────────┤")
        print("│                                               │                                              │")
        print("│ DATOS DEL BIBLIOTECARIO                       │           MENÚ DE COMANDOS                   │")
        print("│                                               │                                              │")
        print("│ ┌───────────────────────────────────────────┐ │ ┌──────────────────────────────────────────┐ │")
        print("│ │ nombre del bibliotecario(a)               │ │ │ 1. guardar_libro                         │ │")
        print("│ └───────────────────────────────────────────┘ │ │    Permite ingresar libro nuevo          │ │")
        print("│                                               │ └──────────────────────────────────────────┘ │")
        print("│ ┌───────────────────────────────────────────┐ │                                              │")
        print("│ │ contraseña del bibliotecario(a)           │ │ ┌──────────────────────────────────────────┐ │")
        print("│ └───────────────────────────────────────────┘ │ │ 2. eliminar_credenciales                 │ │")
        print("│                                               │ │    Elimina lectores no deseados          │ │")
        print("│ ┌───────────────────────────────────────────┐ │ └──────────────────────────────────────────┘ │")
        print("│ │ año de nacimiento del bibliotecario(a)    │ │                                              │")
        print("│ └───────────────────────────────────────────┘ │                                              │")
        print("│                                               │                                              │")
        print("│                                               │                                              │")
        print("└───────────────────────────────────────────────┴──────────────────────────────────────────────┘")


    def pedirComando(self):

        comando = input(
            "\ncomando> "
        )

        return comando.lower().strip()