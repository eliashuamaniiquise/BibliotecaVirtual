class ControladorInicio:

    def __init__(self, vista):
        self.vista = vista


    def ejecutar(self):

        while True:

            self.vista.dibujar()

            comando = self.vista.pedirComando()


            if comando == "bibliotecario":
                print("Entrando como bibliotecario")


            elif comando == "iniciar_sesion":
                print("Iniciando sesión")


            elif comando == "registrarme":
                print("Registrando usuario")


            elif comando == "salir":
                break


            else:
                print("Comando no válido")


            input("\nPresiona ENTER...")