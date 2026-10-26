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