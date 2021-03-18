# Importamos la funcion saludar que esta en subpaquetes
from paquete.hola.saludos import *

saludar() # llamamos el metodo del modulo saludos.py
Saludo() # Llamamos la clase u objeto 

# Importamos la funcion de despedida que esta en subpaquetes
from paquete.adios.despedidas import *
Despedida()


# importar todas las funciones de un script que esta en un paquete
# from paquete.saludos import *
# Saludo()
