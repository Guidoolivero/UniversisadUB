

x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))


distancia = (x**2 + y**2)**0.5  # Teorema de Pitágoras


radio = 10


if distancia < radio:
    print(f"El punto ({x}, {y}) está dentro del círculo.")
elif distancia == radio:
    print(f"El punto ({x}, {y}) está en la circunferencia.")
else:
    print(f"El punto ({x}, {y}) está fuera del círculo.")