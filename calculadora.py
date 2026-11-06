# generador_super_calculadora.py

codigo = []

codigo.append("""
import math
import random
import datetime

class SuperCalculadora:

    def __init__(self):
        self.historial = []

    def guardar(self, operacion, resultado):
        self.historial.append((operacion, resultado))

""")

# Crear muchas funciones
for i in range(1, 121):
    codigo.append(f"""
    def operacion_{i}(self, a, b):
        resultado = a + b
        self.guardar("op_{i}", resultado)
        return resultado
""")

# Errores lógicos
for i in range(121, 161):
    codigo.append(f"""
    def operacion_{i}(self, a, b):
        resultado = a - b + b - a
        return resultado
""")

# Errores de variables
for i in range(161, 181):
    codigo.append(f"""
    def operacion_{i}(self, a, b):
        resultado = a + c
        return resultado
""")

# Errores de división
for i in range(181, 201):
    codigo.append(f"""
    def operacion_{i}(self, a, b):
        return a / 0
""")

# Errores de sintaxis generados como texto
codigo.append("""

def error_sintaxis_1(
    print("falta parentesis")

""")

# Muchas funciones matemáticas
for i in range(201, 301):
    codigo.append(f"""
def funcion_{i}(x):
    return math.sqrt(x)
""")

# Errores con listas
for i in range(301, 351):
    codigo.append(f"""
def lista_{i}():
    datos = [1,2,3]
    return datos[10]
""")

# Errores con cadenas
for i in range(351, 401):
    codigo.append(f'''
def texto_{i}():
    numero = 10
    return "Resultado: " + numero
''')

# Bloques repetitivos
for i in range(401, 701):
    codigo.append(f"""
def calcular_{i}(a,b,c):
    total = a+b+c
    return total
""")

# Errores de atributos
for i in range(701, 801):
    codigo.append(f"""
class Clase{i}:
    pass

def prueba_{i}():
    obj = Clase{i}()
    return obj.nombre
""")

# Errores de tipo
for i in range(801, 901):
    codigo.append(f"""
def tipo_{i}():
    return 5 + "10"
""")

# Funciones normales
for i in range(901, 1001):
    codigo.append(f"""
def extra_{i}(x):
    return x * {i}
""")

with open("super_calculadora.py", "w", encoding="utf-8") as f:
    f.write("\\n".join(codigo))

print("Archivo generado correctamente")
