class ControladorInicio:

    def __init__(
        self,
        vista_inicio,
        controlador_bibliotecario,
        controlador_lector
    ):

        self.vista_inicio = vista_inicio
        self.controlador_bibliotecario = controlador_bibliotecario
        self.controlador_lector = controlador_lector


    def ejecutar(self):

        while True:

            self.vista_inicio.dibujar()

            comando = self.vista_inicio.pedirComando()


            if comando == "bibliotecario":

                print("Entrando como bibliotecario")

                self.controlador_bibliotecario.ejecutar()


            elif comando == "iniciar_sesion":

                print("Iniciando sesión")


            elif comando == "registrarme":

                print("Registrando usuario")


            elif comando == "salir":

                print("Cerrando sistema")
                break


            else:

                print("Comando no válido")


            input("\nPresiona ENTER para continuar...")