"""
este es el primer ehercicio con regrecion lineal y se usa una
libreria de unas plantas iris paar tener una prediccio
"""
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

######################################

#importar dataset para iniciar al analisis
iris=pd.read_csv("Iris.csv")

# visualisamos los primeros 5 datos del dataset
print(iris.head())

# eliminamos la primera columna id
iris=iris.drop('Id',axis=1)
print(iris.head())

#imprimimos la informacion del dta set como largo y ancho
print('informcion del dataset:')
print(iris.info())

print('descripcion del data set')
print(iris.describe())

print('distribusion de las espesies de Iris:')
print(iris.groupby('Species').size())

########## visualizar datos #######
import matplotlib.pyplot as plt

#Grafico Sepal - Longitud vs Ancho
fig = iris[iris.Species == 'Iris-setosa'].plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', color='blue', label='Setosa')
iris[iris.Species == 'Iris-versicolor'].plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', color='green', label='Versicolor', ax=fig)
iris[iris.Species == 'Iris-virginica'].plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', color='red', label='Virginica', ax=fig)

fig.set_xlabel('Sépalo - Longitud')
fig.set_ylabel('Sépalo - Ancho')
fig.set_title('Sépalo - Longitud vs Ancho')
plt.show()

#Grafico Pétalo - Longitud vs Ancho
fig = iris[iris.Species == 'Iris-setosa'].plot(kind='scatter', x='PetalLengthCm', y='PetalWidthCm', color='blue', label='Setosa')
iris[iris.Species == 'Iris-versicolor'].plot(kind='scatter', x='PetalLengthCm', y='PetalWidthCm', color='green', label='Versicolor', ax=fig)
iris[iris.Species == 'Iris-virginica'].plot(kind='scatter', x='PetalLengthCm', y='PetalWidthCm', color='red', label='Virginica', ax=fig)

fig.set_xlabel('Pétalo - Longitud')
fig.set_ylabel('Pétalo - Ancho')
fig.set_title('Pétalo Longitud vs Ancho')
plt.show()

############### aolicacion de modelos de machin learning#######

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

###### Modelo con todos los datos
# separo todos los dtos con las caracteristicas y mas equiquetas o resultados
X= np.array(iris.drop(['Species'],1))
y=np.array(iris['Species'])

#separo los datos de train en etrenamiento y prueba para probar los algoridmos
X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.2)

print('son {} datos para entrenamiento y {} datos para prueba'.format(X_train.shape[0],X_test.shape[0]))

#Modelo de Regresión Logística
algoritmo = LogisticRegression()
algoritmo.fit(X_train, y_train)
Y_pred = algoritmo.predict(X_test)
print('Precisión Regresión Logística: {}'.format(algoritmo.score(X_train, y_train)))

#Modelo de Máquinas de Vectores de Soporte
algoritmo = SVC()
algoritmo.fit(X_train, y_train)
Y_pred = algoritmo.predict(X_test)
print('Precisión Máquinas de Vectores de Soporte: {}'.format(algoritmo.score(X_train, y_train)))

#Modelo de Vecinos más Cercanos
algoritmo = KNeighborsClassifier(n_neighbors=5)
algoritmo.fit(X_train, y_train)
Y_pred = algoritmo.predict(X_test)
print('Precisión Vecinos más Cercanos: {}'.format(algoritmo.score(X_train, y_train)))

#Modelo de Árboles de Decisión Clasificación
algoritmo = DecisionTreeClassifier()
algoritmo.fit(X_train, y_train)
Y_pred = algoritmo.predict(X_test)
print('Precisión Árboles de Decisión Clasificación: {}'.format(algoritmo.score(X_train, y_train)))



