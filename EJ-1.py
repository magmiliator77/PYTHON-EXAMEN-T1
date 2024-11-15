# Tipo de cambio
tipo_cambio = 0.95  # 1 dólar = 0.95 euros

# Solicitar datos al usuario
producto = input("Producto comprado: ")
precio = float(input("Precio del producto: "))
moneda = input("Moneda de pago (dolares/euros): ").strip().lower()

# Conversión de moneda y resultado

#CASO DE EUROS
if moneda == "dolares":
    print(f"{producto}: {precio} dolares → {float(precio * tipo_cambio)} euros")
    
#CASO DE LA DOLARES
elif moneda == "euros":
    print(f"{producto}: {precio} euros → {float(precio / tipo_cambio)} dolares")
    
else:
    print("Moneda no válida. Usa 'dolares' o 'euros'.")
