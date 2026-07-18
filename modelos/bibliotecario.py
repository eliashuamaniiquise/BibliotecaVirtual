class Biblotecario():
    def agregarLibros(self,palabra_clave):
        comando="agregar libros"
        if palabra_clave==comando:
            self.titulo=input("titulo")
            self.autor=input("autor")
            self.categoria=input("categoria")
            self.year=input("year")
            self.estado=input("estado")
            self.contenido=input("contenido")
        else:
            print("comando invalido")
import types
import sys

# ==========================================
# 0. DEFINICIÓN DE CLASES Y ENTORNO INICIAL
# ==========================================

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Herramienta:
    def usar(self):
        return "🛠️ Herramienta original en acción"

def funcion_antigua():
    return "❌ Este es el comportamiento viejo"

print("--- 🚀 INICIO DEL SCRIPT UNIFICADO ---\n")

# ==========================================
# 1. MONKEY PATCHING (Reemplazar en caliente)
# ==========================================
print("[Paso 1] Aplicando Monkey Patching...")

# Definimos la nueva lógica que reemplazará a la antigua
def nueva_logica():
    return "✅ ¡Este es el NUEVO comportamiento en caliente!"

# Sobrescribimos la función directamente en memoria
funcion_antigua = nueva_logica

# Al llamarla, ya ejecuta el código nuevo
print(f"Resultado: {funcion_antigua()}\n")


# ==========================================
# 2. USO DE EXEC() CON INYECCIÓN DE OBJETOS
# ==========================================
print("[Paso 2] Ejecutando código dinámico e inyectando objetos...")

# Creamos un objeto de la clase Usuario
mi_usuario = Usuario("Carlos")

# Este string simula el contenido de un script externo que recibes en tiempo de ejecución
script_externo_string = """
# Este código dinámico puede leer y modificar el objeto inyectado
print(f"  -> [Dentro de exec] Leyendo objeto: {user.nombre}")
user.nombre = "Carlos Modificado por Exec"
"""

# Ejecutamos el string pasando el objeto 'mi_usuario' bajo el nombre de variable 'user'
contexto = {"user": mi_usuario}
exec(script_externo_string, contexto)

# Comprobamos que el objeto original fue modificado por el script dinámico
print(f"Resultado: Nombre del usuario actual: {mi_usuario.nombre}\n")


# ==========================================
# 3. CREACIÓN / RECARGA DE UN MÓDULO VIRTUAL
# ==========================================
print("[Paso 3] Creando e inyectando objetos en un módulo en tiempo de ejecución...")

# Creamos un módulo vacío directamente en la memoria del sistema (sin escribir en disco)
mi_modulo_dinamico = types.ModuleType("mi_modulo_dinamico")
sys.modules["mi_modulo_dinamico"] = mi_modulo_dinamico

# Creamos una instancia del objeto Herramienta
objeto_herramienta = Herramienta()

# Metemos el objeto dentro de nuestro nuevo módulo dinámico
mi_modulo_dinamico.herramienta_activa = objeto_herramienta

# Simulamos que otra parte de tu app importa este módulo y usa el objeto metido en caliente
import mi_modulo_dinamico
print(f"Resultado: {mi_modulo_dinamico.herramienta_activa.usar()}\n")

print("--- 🏁 FIN DEL SCRIPT ---")
