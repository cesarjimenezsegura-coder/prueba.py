import os
import sqlite3
import pickle

# Vulnerabilidad: Secreto hardcodeado
API_KEY = "sk-live-secret-1234567890abcdef"

def buscar_usuario(username):
    conexion = sqlite3.connect('mi_base.db')
    cursor = conexion.cursor()
    
    # Vulnerabilidad: Inyección SQL (concatenación directa)
    query = "SELECT * FROM usuarios WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

def ejecutar_tarea(parametro):
    # Vulnerabilidad: Inyección de comandos (Command Injection)
    os.system("ping -c 1 " + parametro)

def deserializar_inseguro(datos_bytes):
    # Vulnerabilidad: Uso inseguro de pickle
    return pickle.loads(datos_bytes)

def evaluar_expresion(expr):
    # Vulnerabilidad: Uso peligroso de eval()
    return eval(expr)
