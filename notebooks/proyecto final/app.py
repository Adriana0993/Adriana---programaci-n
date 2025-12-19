import csv

import pandas as pd
import os

COMPRAS_DATA = []
print("Cargando datos  de compras desde compras.csv...")
from datos import guardar_csv, ingresar_datos, cargar_compras
from analisis import analiza_compras
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    global COMPRAS_DATA
    while True:
        limpiar_pantalla()
        print("1. Ingreasr nueva compra")
        print("2. Análisis de compras")
        print("3. Cargar compras desde archivo")
        print("4. Salir")
        opción = input("Seleccione una opción (1-4): ")
        if opción == "1":
            ingresar_datos(COMPRAS_DATA)
        elif opción == "2":
            analiza_compras(COMPRAS_DATA)
        elif opción == "3":
            VENTAS_DATA = cargar_compras()
        elif opción == "4":
            print(("Salinedo del programa. ¡Hasta luego!"))
            break
        else: 
            print("opción no válida, intente nuevamente")
            input("Presione  enter para continuar")

if __name__ == "__main__":
    print("BIENVENIDO AL SISTEMA DE CONTROL DE COMPRAS")
    COMPRAS_DATA = cargar_compras()
    ingresar_datos(COMPRAS_DATA)
    menu()

    
     
