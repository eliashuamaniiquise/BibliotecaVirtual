class ControladorLector:


    def __init__(self, vista, lector):

        self.vista = vista
        self.lector = lector



    def ejecutar(self):

        while True:

            self.vista.dibujar()

            comando = self.vista.pedirComando()



            if comando == "buscar_libro":

                self.lector.buscarLibros()



            elif comando == "filtrar":

                self.lector.filtrarLibros()



            elif comando == "leer_libro":

                self.lector.leerLibro()



            elif comando == "favoritos":

                self.lector.mostrarFavoritos()



            elif comando == "cerrar_sesion":

                break


            else:

                print("Comando incorrecto")


            input("\nPresiona ENTER...")