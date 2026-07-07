tupla =("lunes","martes","miercoles","jueves","viernes","sabado","domingo")
tupla[3] #aceso
print(type(tupla))

lista = []
lista = [dia for dia in tupla[0:5]]
print(lista)
lista.append(tupla[5]) # insercion
lista.append(tupla[6])
print(lista)
lista.remove("sabado") # Eliminacion
print(lista)
lista.pop() # Eliminacion ultimo
print(lista)
lista[0] = "LUNES" # Actualizacion
print(lista)
print(type(lista))

mi_set = {1,2,3,4,5,6,7}
print(mi_set)
mi_set.add(8) # Insercion
mi_set.add(8) # No puede repetir valores
print(mi_set)
mi_set.remove(5) # Eliminacion
print(mi_set)
print(type(mi_set))

diccionario = {
    "nombre": "Pepe",
    "apellido": "Garcia",
    "apodo": "Pepito",
    "edad": "36"
}
diccionario["email"] = "pepe@email.com"  # Inserción
print(diccionario)
del diccionario["apodo"]  # Eliminación
print(diccionario)
print(diccionario["nombre"])  # Acceso
diccionario["edad"] = "37"  # Actualización
print(diccionario)
print(type(diccionario))


