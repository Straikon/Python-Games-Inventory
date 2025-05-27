#Ejercicio 2 Listas en Python

#Creacion de la lista
frutas = ["Mango","Sandia","Manzana","Fresa","Durazno"]

#Visualizacion de la lista
print("Lista de frutas")
i = 1;
for fruta in frutas:
    print(f"{i}.- {fruta}")
    i=i+1
    
#Agregar fruta a la lista
nueva_fruta = input("\nIngresa una nueva fruta a la lista: ")
frutas.append(nueva_fruta)

#lista actualizada
print("\nLista de frutas actializadas")
i = 1
for fruta in frutas:
    print(f"{i}.- {fruta}")
    i=i+1

#Eliminar fruta de la lista    
eliminar_fruta = input("\nIngresa la fruta a eliminar de la lista anterior: ")
encontrado = False  # ← bandera para saber si encontramos algo
for fruta in frutas:
    if eliminar_fruta.lower() == fruta.lower():
        frutas.remove(fruta)
        print(f"{eliminar_fruta} eliminada de la lista")
        encontrado = True  # ← si encuentra, cambiamos la bandera
        break
if not encontrado:
        print(f"No se encontro'{eliminar_fruta}'.")

#Lista despues de eliminar
print("\nLista de frutas actializadas")
i = 1
for fruta in frutas:
    print(f"{i}.- {fruta}")
    i=i+1