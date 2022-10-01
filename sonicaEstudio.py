"""
#el programa intentara bisualisar de una forma facio los datos

"""
import numpy as np
import pandas as pd


######################################

# importar dataset para iniciar el análisis
Qenergia = pd.read_csv("sonicacompleto.csv")

# visualisamos los primeros 5 datos del dataset
print(Qenergia.head())

# eliminamos la primera columna id
#iris=iris.drop('Id',axis=1)
#print(iris.head())

# imprimimos la información del data set como largo y ancho
print('informcion del dataset:')
print(Qenergia.info())

print('descripcion del data set')
print(Qenergia.describe())
a=Qenergia.describe()

print('distribusion de las espesies de Iris:')
print(Qenergia.groupby('Vrms ph-n L2N Min').size())
