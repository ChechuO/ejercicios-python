
num1 = 8
num2 = 2

print("Operadores aritmeticos\n")

print(f"Suma: {num1} + {num2} = {num1 + num2}")
print(f"Resta: {num1} - {num2} = {num1 - num2}")
print(f"Multiplicación: {num1} * {num2} = {num1 * num2}")
print(f"División: {num1} / {num2} = {num1 / num2}")
print(f"Módulo: {num1} % {num2} = {num1 % num2}")
print(f"Exponente: {num1} ** {num2} = {num1 ** num2}")
print(f"División entera: {num1} // {num2} = {num1 // num2}")
print("\n")


print("Operadores de comparación\n")

print(f"Igualdad: {num1} == {num2} es {num1 == num2}")
print(f"Desigualdad: {num1} != {num2} es {num1 != num2}")
print(f"Mayor que: {num1} > {num2} es {num1 > num2}")
print(f"Menor que: {num1} < {num2} es {num1 < num2}")
print(f"Mayor o igual que: {num1} >= {num1} es {num1 >= num1}")
print(f"Menor o igual que: {num1} <= {num2} es {num1 <= num2}")
print("\n")


print("Operadores lógicos\n")

print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")
print("\n")


print("Operadores de asignación\n")

numero = 11
print(f"asignación '=' {numero}")
numero += 1 
print(f"suma y asignación '+=' {numero}")
numero -= 1
print(f"resta y asignación '-=' {numero}")
numero *= 2 
print(f"multiplicación y asignación '*=' {numero}")
numero /= 2 
print(f"división y asignación '/=' {numero}")
numero %= 2 
print(f"módulo y asignación '%=' {numero}")
numero **= 1 
print(f"exponente y asignación '**=' {numero}")
numero //= 1
print(f"división entera y asignación '//=' {numero}")
print("\n")


print("Operadores de identidad\n")
nuevo_numero = numero
print(f"numero 'is' nuevo_numero es {numero is nuevo_numero}")
print(f"numero 'is not' nuevo_numero es {numero is not nuevo_numero}")
print("\n")


print("Operadores de pertenencia\n")

print(f"'de' in 'texto de ejemplo' = {'de' in 'texto de ejemplo'}")
print(f"'de' not in 'texto de ejemplo' = {'de' in 'texto de ejemplo'}")
print("\n")


print("Operadores de bit\n")

a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000
print("\n\n")



print("Estructuras de control\n")

print("Condicionales\n")
print("if-else\n")
texto = "Hola"

if texto == "Hola":
    print("texto es 'Hola'")
elif texto == "Mundo":
    print("texto es 'Mundo'")
else:
    print("texto no es 'Hola' ni 'Mundo'")

print("\nmatch\n")

dia = "martes"
match dia:
    case  "lunes"|"martes"|"miercoles"|"jueves"|"viernes":
        print("Entre semana")
    case "sabado"|"domingo":
        print("Fin de semana")

print("\n")


print("Iterativas\n")

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1
print("\n")


print("Excepciones\n")
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")