from msilib.schema import Class
import pandas as pd
import numpy as np
import matplotlib as plt

filename = "data_control_1.csv"
data = pd.read_csv(filename, header = 0)



##################### A) ###############################
cantidad_2021 = data[data.PERIODO.apply(str).str.contains("2021")].size
cantidad_2022 = data[data.PERIODO.apply(str).str.contains("2022")].size
print(f"La cantidad de polizas generadas en el 2021 es de: {cantidad_2021}")
print(f"La cantidad de polizas generadas en el 2022 es de: {cantidad_2022}")
###########################################################################


###################### B) ################################################
vigente_2021 = data[data.PERIODO.apply(str).str.contains("2021") & 
    data.FECHA_FIN.apply(str).str.contains("2022/05|2022/06|2022/07|2022/08|2022/09|2022/10|2022/11|2022/012|2023")].size
print(f"La cantidad de polizas vigentes del 2021 son {vigente_2021}")

inicio_2021 = data[data.PERIODO.apply(str).str.contains("2021")]

cantidad_fuga_2021 = 0
for i,j in zip(inicio_2021["FECHA_FIN_ORIGINAL"],inicio_2021["FECHA_FIN"]):
    if i!=j:
        cantidad_fuga_2021 += 1

print(f"La cantidad de fugados que iniciaron contrato el 2021 es de {cantidad_fuga_2021}")
##############################################################################################


##################### C) ####################################################################
cantidad_2021_finalizada = data[data.PERIODO.apply(str).str.contains("2021") & 
    data.FECHA_FIN.apply(str).str.contains("2021|2022/01|2022/02|2022/03|2022/04") & 
    data.FECHA_FIN_ORIGINAL.apply(str).str.contains("2021|2022/01|2022/02|2022/03|2022/04")].size

print(f"la tasa de fuga de los contratos que iniciaron el 2021 es de {cantidad_fuga_2021/cantidad_2021_finalizada}")
##################################################################################################


##################### D) #######################################################################
inicio_2022 = data[data.PERIODO.apply(str).str.contains("2022")]

cantidad_fuga_2022 = 0
for i,j in zip(inicio_2022["FECHA_FIN_ORIGINAL"],inicio_2022["FECHA_FIN"]):
    if i!=j:
        cantidad_fuga_2022 += 1

print(f"La cantidad de fugados que iniciaron contrato el 2022 es de {cantidad_fuga_2022}")

cantidad_2022_finalizada = data[data.PERIODO.apply(str).str.contains("2022") & 
    data.FECHA_FIN.apply(str).str.contains("2022/01|2022/02|2022/03|2022/04") & 
    data.FECHA_FIN_ORIGINAL.apply(str).str.contains("2022/01|2022/02|2022/03|2022/04")].size

print(f"la tasa de fuga de los contratos que iniciaron el 2022 es de {cantidad_fuga_2022/cantidad_2022_finalizada}")
##########################################################################################################################################################


############################################ 2 ####################################################################################################################################
inicio_2021 = data[data.PERIODO.apply(str).str.contains("2021")]
inicio_2022 = data[data.PERIODO.apply(str).str.contains("2022")]

# A)
P2_a = pd.merge(inicio_2021, inicio_2022, left_on = "RUT", right_on = "RUT")["RUT"].size
print(f"La cantidad de personas que contrataron el seguro el 2021 y el 2022 son: {P2_a}")


#B)
P2_b = pd.merge(inicio_2022, inicio_2021, on = "RUT")["RUT"].size
print(f"La cantidad de personas que contrataron el seguro el 2022 y el 2021 son: {P2_b}")


# C)

interseccion = pd.merge(inicio_2021,inicio_2022, how = "outer", on = "RUT", indicator = True)

Solo2022 = interseccion.loc[interseccion["_merge"]== "right_only"]

P2_C = Solo2022["RUT"].size

print(f"{P2_C} generaron una poliza en 2022 sin generar una poliza en 2021")

# D)

Solo2021 = interseccion.loc[interseccion["_merge"]== "left_only"]

P2_D = Solo2021["RUT"].size

print(f"{P2_D} generaron una poliza en 2021 sin generar una poliza en 2022")



















