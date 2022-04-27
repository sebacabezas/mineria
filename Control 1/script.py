from msilib.schema import Class
import pandas as pd
import numpy as np
import matplotlib as plt

filename = "data_control_1.csv"
data = pd.read_csv(filename, header = 0)


#print(data.shape)
#print(data.head()) # genera un summary de los datos




#cantidad_2022 = data[data.PERIODO.apply(str).str.contains("2022")].size
#print(f"La cantidad de polizas generadas en el 2021 es de: {cantidad_2021}")
#print(f"La cantidad de polizas generadas en el 2022 es de: {cantidad_2022}")

cantidad_2021_finalizada = data[data.PERIODO.apply(str).str.contains("2021") & data.FECHA_FIN.apply(str).str.contains("2021|2022/01|2022/02|2022/03|2022/04") & data.FECHA_FIN_ORIGINAL.apply(str).str.contains("2021|2022/01|2022/02|2022/03|2022/04")]

print(cantidad_2021_finalizada[cantidad_2021_finalizada.FECHA_FIN.apply(str).str.contains("20223")])

# tipo de variable de cada columna
#print(data.dtypes)

# Columnas
# print(data.columns)

# Buscaremos los valores de la categoria USER_ID
# print(pd.unique(data["User_ID"]))

# Estadisticas de alguna columna
# print(data["Age"].describe())