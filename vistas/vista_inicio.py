import os


class VistaInicio:


    def limpiar(self):

        os.system(
            "cls" if os.name == "nt" else "clear"
        )


    def dibujar(self):

        self.limpiar()

        print("┌──────────────────────────────────────────────────────────────────────────────────────────────┐")
        print("│                                                                                              │")
        print("│                         BIBLIOTECA VIRTUAL                                                   │")
        print("│                                                                                              │")
        print("├──────────────────────────────────────────────────────────────────────────────────────────────┤")
        print("│                                                                                              │")
        print("│                              MENÚ DE COMANDOS                                                │")
        print("│                                                                                              │")
        print("│   ┌──────────────────────────────────────────────────────────────┐                           │")
        print("│   │ 1. BIBLIOTECARIO                                             │                           │")
        print("│   │    Acceso para administración de la biblioteca               │                           │")
        print("│   └──────────────────────────────────────────────────────────────┘                           │")
        print("│                                                                                              │")
        print("│   ┌──────────────────────────────────────────────────────────────┐                           │")
        print("│   │ 2. INICIAR SESIÓN                                            │                           │")
        print("│   │    Ingresar credenciales del usuario                         │                           │")
        print("│   └──────────────────────────────────────────────────────────────┘                           │")
        print("│                                                                                              │")
        print("│   ┌──────────────────────────────────────────────────────────────┐                           │")
        print("│   │ 3. REGISTRARME                                               │                           │")
        print("│   │    Crear una nueva cuenta                                    │                           │")
        print("│   └──────────────────────────────────────────────────────────────┘                           │")
        print("│                                                                                              │")
        print("│                                                                                              │")
        print("│                                                                                              │")
        print("│                                                                                              │")
        print("└──────────────────────────────────────────────────────────────────────────────────────────────┘")
    def pedirComando(self):

        comando = input(
            "\ncomando> "
        )

        return comando.lower().strip()