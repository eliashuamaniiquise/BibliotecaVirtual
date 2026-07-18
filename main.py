# ======================================
# IMPORTACIONES
# ======================================

from modelos.biblioteca import Biblioteca
from modelos.bibliotecario import Bibliotecario
from modelos.lector import Lector

from vistas.vista_inicio import VistaInicio
from vistas.vista_bibliotecario import VistaBibliotecario
from vistas.vista_lector import VistaLector

from controladores.controlador_inicio import ControladorInicio
from controladores.controlador_bibliotecario import ControladorBibliotecario
from controladores.controlador_lector import ControladorLector



# ======================================
# CREAR SISTEMA
# ======================================

biblioteca = Biblioteca()



# ======================================
# CREAR USUARIOS
# ======================================

bibliotecario = Bibliotecario(
    biblioteca
)

lector = Lector(
    "Elias",
    "elias@gmail.com",
    "1234",
    biblioteca
)

# ======================================
# CREAR VISTAS
# ======================================

vista_inicio = VistaInicio()

vista_bibliotecario = VistaBibliotecario()

vista_lector = VistaLector()



# ======================================
# CREAR CONTROLADORES
# ======================================

controlador_bibliotecario = ControladorBibliotecario(
    vista_bibliotecario,
    bibliotecario
)


controlador_lector = ControladorLector(
    vista_lector,
    lector
)

controlador_inicio = ControladorInicio(
    vista_inicio,
    controlador_bibliotecario,
    controlador_lector
)


if __name__ == "__main__":

    controlador_inicio.ejecutar()