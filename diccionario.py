dictionary = {
              "fulanito":87,
              "ximena":98,
              "cesar":80,
              "rodrigo":100
              }
#for key in sorted(dictionary.keys()):
for key in sorted(dictionary.keys()):
    print(key, "your kkdkdkd is", dictionary[key])
#
list = dictionary.items()
print(list)

#investigar de tuplas y arreglos, key
for tupleOne, tupleTwo in dictionary.items():
    print("the key is= ",tupleOne, "the vaule is ", tupleTwo)

for values in dictionary.values():
    print(values)

#agregar valor en timepo de ejeucion
# modificar, add, delate
dictionary["fulanito"] = 60
dictionary["oscar"] = 80

dictionary.update({"ramirez":90 })
print(dictionary)

# crear un script en python un programa para calcular promedios
# pedira el nombre seguido de su calificacion
# crear dos listas donde se pongan nombre y en otra calificaciones
# se vacia a una diccionario y se ordena alfabeticamente
# mostrar promedio del grupo 