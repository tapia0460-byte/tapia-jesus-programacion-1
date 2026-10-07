# Ejercicio datos personales
nombre = "Tapia"
edad = 18
ciudad = "Guadalajara"

print (nombre, edad, ciudad)

# Ejercicio contador
contador = 0

contador = contador + 1 
print (contador)

contador = contador + 1
print (contador)

contador = contador + 1
print (contador)

# Ejercicio constante de conversion
PULGADAS_A_CENTIMETROS = 2.54
pulgadas = 10
centimetros = pulgadas * PULGADAS_A_CENTIMETROS

print (centimetros)

# Ejercicio area de un rectangulo
base = 10
altura = 9

area = (base * altura) / 2

print("el area es:", area)

# Ejercicio total con IVA
IVA = 0.16

precio = 100
total = precio + precio * IVA

print("El total a pagar es:", total)


IVA = 0.16

precio = 250
total = precio + precio * IVA

print("El total a pagar es:", total)

# Ejercicio intercambio de valores
a = 10
b = 20

print("Antes:")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp

print("Despues:")
print("a =", a)
print("b =", b)

# Ejercicio Identificar tipos con type()
entero = 10
decimal = 5.5
texto = "Hola"
booleano = True

print(type(entero))
print(type(decimal))
print(type(texto))
print(type(booleano))

# Ejercicio convertir tipos
texto = "25"
numero = int(texto)

print(numero, type(numero))

entero = 50
texto_nuevo = str(entero)

print(texto_nuevo, type(texto_nuevo))

# Ejercicio booleanos y comparaciones
a = 10
b = 5

mayor = a > b

print(mayor)
print(type(mayor))