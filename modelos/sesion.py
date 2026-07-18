class Sesion:
    def __init__(self, usuarioActivo, fechaInicio):
        self.usuarioActivo = usuarioActivo
        self.fechaInicio = fechaInicio
        
    def cerrarSesion(self):
        print(
            f"Cerrando sesión de: {self.usuarioActivo.nombre}"
        )
        self.usuarioActivo = None
        print("Sesión cerrada correctamente")