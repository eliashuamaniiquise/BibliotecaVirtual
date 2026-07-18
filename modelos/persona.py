from abc import ABC,abstractmethod
class Persona(ABC):
    def __init__(self,nombre=str,correo=str,password=str):
        self.nombre=nombre
        self.correo=correo
        self.password=password
    @abstractmethod
    def mostrarInformacion(self):
        print(f"nombre de usuario:{self.nombre}")
        print(f"nombre de correo:{self.correo}")
        print(f"contraseña:{self.password}")
    @abstractmethod
    def modificarDatos(self,palabra_clave:str):
        comando="D"
        if palabra_clave==comando:
            self.nombre=input("ingrese nueva nombre: ")
            self.correo=input("ingrese nuevo correo: ")
            self.password=input("ingrese nueva contraseña:")
            print("contraseña modificada")
        else:
            print("comando invalido")
