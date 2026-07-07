def imprimir_hola():
    print("hola")

imprimir_hola()

def retornar_hola():
    return "hola"

print(retornar_hola())

def con_argumento(nombre):
    return f'tu nombre es "{nombre}"'

print(con_argumento("Pepe"))

def varios_argumentos(nombre, anios):
    return f'tu nombre es "{nombre}" y tienes {anios} años'

print(varios_argumentos("pepe",25))

def argumento_predefinido(nombre="Pepe"):
    return f"hola {nombre}"

print(argumento_predefinido())
print(argumento_predefinido("Juan"))

def varios_valores_return():
    return "hola","mundo"

pal1, pal2 = varios_valores_return()
print(pal1," ",pal2)

def argumentos_variables(*nombres):
    for n in nombres:
        print(f"hola {n}")

argumentos_variables()

def argumentos_variables_kv(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

argumentos_variables_kv()

def funcion_superior():
    def funcion_inferior():
        print("funcion inferior")
    funcion_inferior()

funcion_superior()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))
