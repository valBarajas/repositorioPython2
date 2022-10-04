"""
Date:        10/04/2022
Authors:     vale barajas
File:        2022-4.py
Brief:       Description file
Version:     0.1
Changes By:  none
Fixes:       nonea
"""
miLista1=[]
i=1
for i in range(1,6, 1):
    print(f"ingrese alumno {i}->")
    miLista1.insert(i,input())
print(miLista1)

miLista2=[]

for i in range(0,5, 1):
    print(f"ingrese calificacion del alumno {miLista1[i]}->")
    miLista2.insert(i,input())
print(miLista2)
dictionary={}
for i in range(0,5,1):
   dictionary[miLista1[i]] = miLista2[i]
p=0
for values in dictionary.values():
    print(values)
    p=int(values)+p

p=p/5


print(f"el promedio es {values}")


