num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))


if num1 <= num2:
    print(f"En orden creciente: {num1}, {num2}")
else:
    print(f"En orden creciente: {num2}, {num1}")