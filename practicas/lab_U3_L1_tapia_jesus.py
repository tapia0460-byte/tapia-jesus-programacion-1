# Clasificacion por edad
edad = int(input("Ingrese su edad: "))

if edad < 13:
    print("Usted es un niño.")
elif edad < 18:
    print("Usted es un adolescente.")
else: 
    print("Usted es un adulto.")

# Validar acceso (usuario y contraseña)
usuario_correcto = "Akemi"
contrasena_correcta = "1225"

usuario = input("Ingrese su usuario: ")
contrasena = input("Ingrese su contraseña: ")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Acceso concedido.")
elif usuario != usuario_correcto:
    print("Usuario no encontrado")
else:
    print("Contraseña incorrecta")

# Calculadora de envio
peso = float(input("Ingrese el peso del paquete (kg): "))
if peso < 1:
    print("50 pesos de envio")
elif peso < 5:
    print("100 pesos de envio")
else:
    print("150 pesos de envio")

# Clasificar la temperatura
temperatura = float(input("Ingresa la temperatura en grados: "))

if temperatura < 10:
    print("La temperatura es fría")
elif temperatura >= 10 and temperatura <= 24:
    print("La temperatura es templada")
else:
    print("La temperatura es calor")

# Clasificacion con letras
calificacion = float(input("Ingresa tu calificación (0 a 100): "))

if calificacion >= 90:
    print("Tu calificación es A")
elif calificacion >= 80:
    print("Tu calificación es B")
elif calificacion >= 70:
    print("Tu calificación es C")
elif calificacion >= 60:
    print("Tu calificación es D")
else:
    print("Tu calificación es F")

# Descuento por monto de compra
compra = float(input("Ingresa el monto de tu compra: $"))

if compra > 500:
    descuento = 0.20
elif compra > 200:
    descuento = 0.10
else:
    descuento = 0

monto_descuento = compra * descuento
total = compra - monto_descuento

print("Porcentaje de descuento:", descuento * 100, "%")
print("Monto final a pagar: $", total)

# Validar un rango con comparación encadenada
numero = float(input("Ingresa un número: "))

if 1 <= numero <= 100:
    print("El número está dentro del rango.")
else:
    print("El número no está dentro del rango.")

# Clasificar el IMC
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))

imc = peso / estatura ** 2

print("Tu IMC es:", round(imc, 2))

if imc < 18.5:
    print("Clasificación: Bajo peso")
elif imc < 25:
    print("Clasificación: Normal")
elif imc < 30:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")

# Tarifas de electricidad
consumo = float(input("Ingresa el consumo mensual en kWh: "))

if consumo <= 150:
    costo = consumo * 1.20
elif consumo <= 300:
    costo = (150 * 1.20) + ((consumo - 150) * 1.80)
else:
    costo = (150 * 1.20) + (150 * 1.80) + ((consumo - 300) * 2.50)

print("Consumo mensual:", consumo, "kWh")
print("Costo total: $", costo)