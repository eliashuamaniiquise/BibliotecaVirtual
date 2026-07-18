
class Libro:
    def __init__(self,titulo:str,autor:int,categoria=str,year=int,estado=str,contenido=str):
        self.titulo=titulo
        self.autor=autor
        self.categoria=categoria
        self.year=year
        self.estado=estado
        self.contenido=contenido
    def monstrarinformacion(self):
        print(f"titulo:{self.titulo}")
        print(f"autor:{self.autor}")
        print(f"categoria:{self.categoria}")
        print(f"estado:{self.estado}")
        print(f"año:{self.year}")
    #mejoras para estar100%    
    #Lo único que aún te falta es pulir algunos detalles de diseño y 
    # pequeños errores (por ejemplo, algunos tipos de datos, nombres de 
    # métodos y cómo organizar ciertas responsabilidades), 
    # pero esos son ajustes normales mientras desarrollas el proyecto.
libro1=Libro(
    "tres certido",
    "pepe",
    "cuento",
    2020,
    "bueno",
    """
    narra la historia de tres hermanos que construyen casas de paja,
    madera y ladrillo para protegerse de un lobo. 
    El lobo destruye las casas más débiles, pero la de ladrillo resiste y los salva a todos
    """)
libro2=Libro(
    
)