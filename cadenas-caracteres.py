
s1 = "Hola"
s2 = "Python"

# Concatenación
print(s1 + ", " + s2 + "!")

# Repetición
print(s1 * 3)

# Indexación
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# Slicing 
print(s2[2:5])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Busqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("o", "a"))

# División
print(s2.split("t"))

# Mayúsculas, minúsculas y letras en mayúsculas
print(s1.upper())
print(s1.lower())
print("pepe perez".title())
print("pepe perez".capitalize())

# Eliminación de espacios al principio y al final
print(" pepe perez ".strip())

# Búsqueda al principio y al final
print(s1.startswith("Ho"))
print(s2.startswith("Py"))
print(s1.endswith("la"))
print(s2.endswith("on"))

s3 = "Esto es un texto de ejemplo"

# Búsqueda de posición
print(s3.find("texto"))
print(s3.find("ejemplo"))
print(s3.find("m"))
print(s3.lower().find("E"))

# Búsqueda de ocurrencias
print(s3.lower().count("e"))

# Formateo
print("Saludo: {}, lenguje: {}!".format(s1, s2))

# Interpolación
print(f"Saludo: {s1}, lenguje: {s2}!")

# Tranformación en lista de caracteres
print(list(s3))

# Transformación de lista en cadena
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

# Transformaciones numéricas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Comprobaciones varias
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())