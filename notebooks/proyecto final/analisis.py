import pandas as pd
def analiza_compras(compras):
    try:
        df = pd.DataFrame(compras)
        if df.empty:
            print("No hay datos de compra.")
            return
        print("\n ANÁLISIS DE COMPRAS ")
        
        total = total_compras(compras)
        print(f"Total de compras: {total:.2f}")


        #producto que más se compró.

        producto_mas_comprado = df.groupby("Producto")["Cantidad"].sum().idmax()
        print(f"El producto que más se compró fue: {producto_mas_comprado}")

        print(df)

        producto_mayor_inversion = df["Subtotal"].max()
        producto_mayor_precio =df.groupby("Producto")["Subtotal"].sum().idmax()

        #Resumen de compras por fecha:
        resumen_por_fecha = df.groupby("Fecha")["Subtotal"]
        print(resumen_por_fecha)
    except Exception as e:
        def total_compras(compras):
            return 0
        
    try:
        df = compras
        df["Subtotal"] = df["Cantidad"] * ["Precio"]
        total = df["Subtotal"].sum()
        return total
    except Exception as e:
        print(f"Error al calcular el total comprado: {e}")
        return 0










