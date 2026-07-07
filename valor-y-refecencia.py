"""
Valor y referencia
"""

# Tipos de dato por valor

num_a = 10
num_b = 20
print(num_a)
print(num_b)

# Tipos de dato por referencia

lista_a = [10, 20]
lista_b = lista_a
lista_b.append(30)
print(lista_a)
print(lista_b)

# Funciones con datos por valor


def num_func(num: int):
    num = 20
    print(num)


num_c = 10
num_func(num_c)
print(num_c)

# Funciones con datos por referencia


def lista_func(lista: list):
    lista.append(30)

    lista_d = lista
    lista_d.append(40)

    print(lista)
    print(lista_d)


lista_c = [10, 20]
lista_func(lista_c)
print(lista_c)
