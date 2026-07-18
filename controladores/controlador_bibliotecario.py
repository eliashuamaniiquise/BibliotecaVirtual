class ControladorBibliotecario:


    def __init__(self, vista, bibliotecario):

        self.vista = vista
        self.bibliotecario = bibliotecario



    def ejecutar(self):

        while True:

            self.vista.dibujar()

            comando = self.vista.pedirComando()



            if comando == "guardar_libro":

                self.bibliotecario.agregarLibros()



            elif comando == "clasificar_libro":

                self.bibliotecario.clasificarLibro()



            elif comando == "eliminar_libro":

                self.bibliotecario.eliminarLibro()



            elif comando == "salir":

                break


            else:

                print("Comando incorrecto")


            input("\nPresiona ENTER...")