
# Tapia Hernandez Jesus Adrian
# Programa que registra productos de una compra,
# valida los datos, calcula el IVA del 16% y muestra un recibo.

# ==========================================
# 1. Captura de numeros
# ==========================================

while True:
    numero_productos = input("¿Cuántos productos va a registrar? ")

    # Validar que la entrada contenga solo dígitos
    if numero_productos.isdigit() and int(numero_productos) > 0:
        numero_productos = int(numero_productos)
        break
    else:
        print("Error: ingrese un número entero positivo.")

# Lista para guardar los productos nombrados  
productos = []

# ==========================================
# 2. Validacion de datos
# ==========================================

for i in range(numero_productos):
    print(f"\n--- Producto {i + 1} ---")

    # Capturar y validar el nombre del producto
    while True:
        nombre_producto = input("Nombre del producto: ").strip()

        if nombre_producto:
            break
        else:
            print("Error: el nombre no puede estar vacío.")

    # Capturar y validar el precio
    while True:
        precio_ingresado = input("Precio del producto: ")

        try:
            precio_producto = float(precio_ingresado)

            if precio_producto >= 0:
                break
            else:
                print("Error: el precio no puede ser negativo.")

        except ValueError:
            print("Error: ingrese un precio numérico válido.")

    # Capturar y validar la cantidad
    while True:
        cantidad_ingresada = input("Cantidad de unidades: ")

        try:
            cantidad_producto = int(cantidad_ingresada)

            if cantidad_producto > 0:
                break
            else:
                print("Error: la cantidad debe ser mayor que cero.")

        except ValueError:
            print("Error: ingrese una cantidad entera válida.")

    # ==========================================
    # 3. Cálculo del subtotal del producto
    # ==========================================

    subtotal_producto = precio_producto * cantidad_producto

    # Guardar datos del producto en la lista
    productos.append({
        "nombre": nombre_producto,
        "precio": precio_producto,
        "cantidad": cantidad_producto,
        "subtotal": subtotal_producto
    })

# ==========================================
# 4. Cálculo de toda la compra
# ==========================================

subtotal_general = sum(
    producto["subtotal"] for producto in productos
)

iva = subtotal_general * 0.16
total_pagar = subtotal_general + iva

# ==========================================
# 5. Recibo de compra
# ==========================================

print("\n" + "=" * 50)
print("             RECIBO DE COMPRA")
print("=" * 50)

print(f"{'Producto':<18}{'Precio':>10}{'Cant.':>7}{'Subtotal':>15}")
print("-" * 50)

for producto in productos:
    print(
        f"{producto['nombre']:<18}"
        f"${producto['precio']:>9.2f}"
        f"{producto['cantidad']:>7}"
        f"${producto['subtotal']:>14.2f}"
    )

print("-" * 50)
print(f"{'Subtotal general:':<30}${subtotal_general:>10.2f}")
print(f"{'IVA (16%):':<30}${iva:>10.2f}")
print("=" * 50)
print(f"{'TOTAL A PAGAR:':<30}${total_pagar:>10.2f}")
print("=" * 50)
print("       ¡Gracias por su compra!")
