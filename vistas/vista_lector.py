import os


class VistaLector:


    def limpiar(self):

        os.system(
            "cls" if os.name == "nt" else "clear"
        )


    def dibujar(self):

        self.limpiar()

        print("┌──────────────────────────────────────────────────────────────────────────────────────────────┐")
        print("│                                                                                              │")
        print("│                              BIENVENIDO LECTOR                                               │")
        print("│                                                                                              │")
        print("├───────────────────────────────────────────────┬──────────────────────────────────────────────┤")
        print("│                                               │                                              │")
        print("│ DATOS DEL LECTOR                              │            MENÚ DE COMANDOS                  │")
        print("│                                               │                                              │")
        print("│ ┌───────────────────────────────────────────┐ │ ┌──────────────────────────────────────────┐ │")
        print("│ │ nombre del lector(a)                      │ │ │ 1. ingresa_nombre_libro                  │ │")
        print("│ └───────────────────────────────────────────┘ │ │    Permite pedir libro específico         │ │")
        print("│                                               │ └──────────────────────────────────────────┘ │")
        print("│ ┌───────────────────────────────────────────┐ │                                              │")
        print("│ │ contraseña del lector(a)                  │ │ ┌──────────────────────────────────────────┐ │")
        print("│ └───────────────────────────────────────────┘ │ │ 2. cambiar_nombre (cn)                   │ │")
        print("│                                               │ │    Ingresa tu nuevo nombre                │ │")
        print("│ ┌───────────────────────────────────────────┐ │ └──────────────────────────────────────────┘ │")
        print("│ │ año de nacimiento del lector(a)           │ │                                              │")
        print("│ └───────────────────────────────────────────┘ │ ┌──────────────────────────────────────────┐ │")
        print("│                                               │ │ 3. cambiar_año_nacimiento (ca)            │ │")
        print("│                                               │ │    Ingresa tu fecha de nacimiento         │ │")
        print("│                                               │ └──────────────────────────────────────────┘ │")
        print("│                                               │                                              │")
        print("│                                               │ ┌──────────────────────────────────────────┐ │")
        print("│                                               │ │ 4. cambiar_contraseña (cc)               │ │")
        print("│                                               │ │    Ingresa nueva contraseña               │ │")
        print("│                                               │ └──────────────────────────────────────────┘ │")
        print("│                                               │                                              │")
        print("├───────────────────────────────────────────────┴──────────────────────────────────────────────┤")
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