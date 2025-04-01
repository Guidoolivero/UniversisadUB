
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))


if num1 <= num2 and num2 <= num3:
    print(f"En orden creciente: {num1}, {num2}, {num3}")
elif num1 <= num3 and num3 <= num2:
    print(f"En orden creciente: {num1}, {num3}, {num2}")
elif num2 <= num1 and num1 <= num3:
    print(f"En orden creciente: {num2}, {num1}, {num3}")
elif num2 <= num3 and num3 <= num1:
    print(f"En orden creciente: {num2}, {num3}, {num1}")
elif num3 <= num1 and num1 <= num2:
    print(f"En orden creciente: {num3}, {num1}, {num2}")
else:
    print(f"En orden creciente: {num3}, {num2}, {num1}")