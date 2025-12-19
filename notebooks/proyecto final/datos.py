import csv
import pandas as pd

def guardar_csv(compras, archivo= 'compra.csv'):
    if not compras: 
        print('no hay datos para guardar')
        return
    try:
        with open(archivo, mode="w", newline= '', encoding= 'utf-8') as base:
            columnas = ["Producto" , "Cantidad" , "Precio" , "Fecha"]
            writer = csv.dictwriter(base, fielname= columnas)
            writer.writerheader()
            writer.writerrows(compras)
            print(f'Datos guardados correctamente en {archivo}.')
    except Exception as e:
         print(f'Error al guardar los datos en {archivo}: {e}')

def ingresar_datos(compras):
    while True:
        try:
            producto = input("Ingrese el nombre del producto").upper()
            cantidad = int(input("Ingrese la cantidad comprada: "))
            precio = int(input("Ingrese el precio del prodcuto: "))
            fecha = input("ingrese la fecha de la venta (YYY_MM_DD): ")
            if cantidad <= 0:
                print("La cantidad debe ser mayor a cero")

            if precio <= 0:
                print(" el precio debe ser mayor a cero")

        except ValueError:
            print("Error Cantidad y precio deben ser valores numéricos. Por favor intente de nuevo")
        except Exception as e:
            print(f"Error al ingresar los datos: {e}")
            continue
            
            compra = {
                "Prodcuto": producto,
                "Cantidad" : cantidad,
                "Precio": precio,
                "Fecha": fecha

            }

        compras.append(compras)
        print("Compra ingresada con éxito")
            
        continuar = input("¿Deaea ingresar otra compra? (s/n): ").lower()
        if continuar != "s":
         guardar_csv(compras)

def cargar_compras(archivo_csv='compras.csv'):
    try:
        pass
        df = pd.read_csv(archivo_csv)
        compras_cargadas = df.to.dict(orient="records")
        print(f"Datos cargados correctamente desde {archivo_csv}.")
        return compras_cargadas
    except FileNotFoundError:
        print(f"El archivo {archivo_csv} no existe. Se devolverá una lista vacía")



if __name__ == '__main__':
    compra_inicial = [
        {"Prodcuto": "Almohada Ortopédica", "Cantidad": 25, "Precio": 1400, "Fecha": "2025-10-22"}, 
        {"Producto": "Edredón Amici 6 pz", "Cantidad": 5 , "Precio": 10500, "Fecha": "2025-10-22" },
        {"Producto": "Cobija matrimonial mexicana" , "Cantidad": 3, "Precio": 10555, "Fecha": "2025-10-22"},
        {"Producto": "Edredón Amici 6 pz", "Cantidad": 5, "Precio": 10500, "Fecha": "2025-10-24"}, 
        {"Producto": "Almohada Ortopédica","Cantidad": 25, "Precio": 1400, "Fecha": "2025-10-24"},
        {"Producto": "Edredón matri bordado Miel Home", "Cantidad": 1, "Precio": 8000, "Fecha": "2025-10-24"},
        {"Prodcuto": "Cobija matrimonial 3b", "Cantidad": 4, "Precio": 4000, "Fecha": "2025-10-24"},
        {"Producto": "Mantel navideño", "Cantidad": 2, "Precio": 4000, "Fecha": "2025-10-24"},
        {"Producto": "Sábana matriminial Amici", "Cantidad": 2, "Precio": 5500, "Fecha": "2025-10-24"},
        {"Producto": "Escurridor de platos", "Cantidad": 1, "Precio": 10500, "Fecha": "2025-10-24"},
        {"Producto": "Almohada Ortopédica", "Cantidad": 20, "Precio": 1400, "Fecha": "2025-10-23"},
        {"Producto": "Edredón Amici 6 pz", "Cantidad": 2, "Precio": 10500, "Fecha": "2025-10-23"},
        {"Producto": "Edredón matri bordado Miel Home", "Cantidad": 2, "Precio": 8000, "Fecha": "2025-10-23"},
        {"Producto": "Cobija borrego", "Cantidad": 2, "Precio": 7600, "Fecha": "2025-10-23" },
        {"Producto": "Cobija matrimonial 3b", "Cantidad": 2, "Precio": 4000, "Fecha": "2025-10-23"},
        {"Producto": "Escurridor de platos", "Cantidad": 1, "Precio": 10500, "Fecha": "2025-10-25"},
        {"Producto": "Edredón Amici 6 pz", "Cantidad": 5, "Precio": 10500, "Fecha": "2025-10-25"},
        {"Producto": "Cobija matrimonial 3b", "Cantidad": 4, "Precio": 4000, "Fecha": "2025-10-25"},
        {"Producto": "Sabana matrimonial variada", "Cantidad": 2, "Precio": 5500, "Fecha": "2025-10-25"},
        {"Producto": "Mantel navideño", "Cantidad": 1, "Precio": 4000, "Fecha": "2025-10-25"},
        {"Producto": "Almohada Ortopédica", "Cantidad": 35, "Precio": 1400, "Fecha": "2025-10-25"},
        {"Producto": "Cortina tegal Lemond", "Cantidad": 2, "Precio": 6500, "Fecha": "2025-10-25"},
        {"Producto": "Cortina argollas 2 pz", "Cantidad": 2, "Precio": 7000, "Fecha": "2025-10-25"},
        {"Producto": "Edredón Amici 6 pz", "Cantidad": 4, "Precio": 10500, "Fecha": "2025-11-04"},
        {"Producto": "Cortina navideña doble", "Cantidad": 1, "Precio": 7500, "Fecha": "2025-11-04"},
        {"Producto": "Edredón full Adriana", "Cantidad": 4, "Precio": 11000, "Fecha": "2025-11-04"},
        {"Producto": "Cobija matrimonial Samuka", "Cantidada": 3, "Precio": 6500, "Fecha": "2025-11-04"},
        {"Producto": "Almohada Ortopédica", "Cantidad": 20, "Precio": 1400, "Fecha": "2025-11-04"},
        {"Producto": "Almohada Ortopédica", "Cantidad": 55, "Precio": 1400, "Fecha": "2025-11-13"},
        {"Producto": "Edredón matri bordado Miel Home", "Cantidad": 16, "Precio": 10500, "Fecha": "2025-11-13"},
        {"Producto": "Almohada Ortopédica", "Cantidad": 20, "Precio": 1400, "Fecha": "2025-11-11"},
        {"Producto": "Cobija matrimonial 3b", "Cantidad": 2, "Precio": 4000, "Fecha": "2025-11-11"},
        {"Producto": "Edredón Lemond 9 pz", "Cantidad": 7, "Precio": 10540, "Fecha": "2025-11-11"},
        {"Producto": "Almohada Ortopédica", "Cantidad": 20, "Precio": 1400, "Fecha": "2025-11-12"},
        {"Producto": "Edredón matri bordado Miel Home", "Cantidad": 8, "Precio": 10450, "Fecha": "2025-11-12"},
        {"Producto": "Cobija matrtimonial 3b", "Cantidad": 3, "Precio": 4000, "Fecha": "2025-11-12"},
        {"Producto": "Cobija matrimonial 3b", "Cantidad": 1, "Precio": 4000, "Fecha": "2025-11-13"},
        {"Producto": "Edredón matri bordado Miel Home", "Cantidad": 8, "Precio": 10450, "Fecha": "2025-11-13"},
        {"Producto": "Almohada Ortopédica", "Cantidad": 20, "Precio": 1400, "Fecha": "2025-11-14"},
        {"Producto": "Edredón matri bordado Miel Home", "Cantidad": 6, "Precio": 10450, "Fecha": "2025-11-14"},
        {"Producto": "Cobija matrimonial 3b", "Cantidad": 4, "Precio": 4000, "Fecha": "2025-11-14"},
        {"Producto": "Cobija borrego king", "Cantidad": 4, "Precio": 8500, "Fecha": "2025-11-14"},
        {"Producto": "Forro sillón navideño", "Cantidad": 2, "Precio": 11000, "Fecha": "2025-11-14"},
        {"Producto": "Alfombra lisa", "Cantidad": 1, "Precio": 7500, "Fecha": "2025-11-14"},
        {"Producto": "Alfombra navideña", "Cantidad": 2, "Precio": 7000, "Fecha": "2025-11-14"},
        {"Producto": " Set navideño", "Cantidad": 2, "Precio": 3000, "Fecha": "2025-11-14"},
        {"Producto": "Cobija full con fundas", "Cantidad": 2, "Precio": 8000, "Fecha": "2025-11-14"}
    ]

    guardar_csv(compra_inicial)



 