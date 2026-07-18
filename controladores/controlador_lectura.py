class ControladorLectura:


    def __init__(self, vista, lector):

        self.vista = vista
        self.lector = lector



    def ejecutar(self, libro):


        while True:

            self.vista.dibujar(libro.titulo)


            comando = self.vista.pedirComando()



            if comando == "me_gusta_libro":

                self.lector.agregarFavoritos(libro)



            elif comando == "devolver_libro":

                break



            else:

                print("Comando incorrecto")


            input("\nPresiona ENTER...")