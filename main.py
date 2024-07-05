import os
import globales
import ventas
import random

def menu_general():

    while True:
        os.system("cls")
        print("===========================")
        print("1. Asignar montos aleatorios.")
        print("2. Ver estadísticas.")
        print("3. Salir del programa")
        print("===========================")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            print("== Asignar montos aleatorios ==")
            ventas.generar_ventas()
            input()
        elif opcion == 2:
            print("== 2. Ver estadísticas ==")
            globales.leer_archivo_json
            input()
        else:
            print("== 3. SALIR DEL PROGRAMA ==")
            return
        
menu_general()