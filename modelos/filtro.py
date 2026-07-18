class Filtro:
    def __init__(self, criterioBusqueda):
        self.criterioBusqueda = criterioBusqueda
    def aplicarFiltro(self, listaLibros):
        librosEncontrados = []
        for libro in listaLibros:
            if self.criterioBusqueda.lower() in libro.categoria.lower():
                librosEncontrados.append(libro)

        return librosEncontrados