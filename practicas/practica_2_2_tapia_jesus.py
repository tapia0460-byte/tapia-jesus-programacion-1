# Ejercicio ¿Es par o impar?
numero = 10

es_par = numero % 2 == 0

print("¿Es par?", es_par)

numero = 7

es_par = numero % 2 == 0

print("¿Es par?", es_par)

# Ejercicio concatenar o sumar
a = "5"
b = "3"

print(a + b)

# Al sumar textos, se concatenan; al convertirlos a números, se realiza una suma matemática.

a = int(a)
b = int(b)

print(a + b)

# Ejercicio mini reporte de un perfil
nombre = "Tapia"
edad = 18
estatura = 1.67
es_estudiante = True

print("Nombre:", nombre, type(nombre))
print("Edad:", edad, type(edad))
print("Estatura:", estatura, type(estatura))
print("Es estudiante:", es_estudiante, type(es_estudiante))

# Ejercicio operadores aritmeticos basicos
a = 10
b = 5

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)

# Ejercicio division entera y modulo
a = 10
b = 3

# / realiza una división normal y // realiza una división entera.
print("División normal:", a / b)
print("División entera:", a // b)
print("Residuo:", a % b)

# Ejercicio operadores relacionales
a = 10
b = 10

mayor = a > b
menor = a < b
igual = a == b
diferente = a != b

print("¿a es mayor que b?", mayor)
print("¿a es menor que b?", menor)
print("¿a es igual a b?", igual)
print("¿a es diferente de b?", diferente)


a = 10
b = 5

mayor = a > b
menor = a < b
igual = a == b
diferente = a != b

print("¿a es mayor que b?", mayor)
print("¿a es menor que b?", menor)
print("¿a es igual a b?", igual)
print("¿a es diferente de b?", diferente)

# Ejercicio operadores logicos
a = 10
b = 5

comparacion1 = a > b
comparacion2 = a == b

resultado_and = comparacion1 and comparacion2
resultado_or = comparacion1 or comparacion2
resultado_not = not comparacion1

print("AND:", resultado_and)
print("OR:", resultado_or)
print("NOT:", resultado_not)

# Ejercicio promedio y aprobacion
calificacion1 = 8
calificacion2 = 7
calificacion3 = 9

promedio = (calificacion1 + calificacion2 + calificacion3) / 3

aprobado = promedio >= 6

print("Promedio:", promedio)
print("¿Aprobado?", aprobado)


calificacion1 = 4
calificacion2 = 5
calificacion3 = 3

promedio = (calificacion1 + calificacion2 + calificacion3) / 3

aprobado = promedio >= 6

print("Promedio:", promedio)
print("¿Aprobado?", aprobado)

# Validacion de elegibilidad
edad = 20
nacionalidad = "mexicana"

es_elegible = edad > 17 and nacionalidad == "mexicana"

print("¿Es elegible?", es_elegible)


edad = 16
nacionalidad = "mexicana"

es_elegible = edad > 17 and nacionalidad == "mexicana"

print("¿Es elegible?", es_elegible)