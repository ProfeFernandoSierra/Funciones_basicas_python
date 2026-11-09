#Este archivo contiene logica principal, mas llamados a mis funciones
import os
os.system("cls")
from functions import *

#variables o flujo de mi proyecto
anio_actual = 2026
nombre = "Fernando"


#Llamado a mis funciones, segun las necesidades del proyecto
print("**********")
saludar()
print("**********")
obtener_nombre(nombre)
print("**********")
retorno_anio = obtener_anio(anio_actual)
print(f"el año actual es: {retorno_anio}")
print("**********")