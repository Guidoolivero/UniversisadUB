"Diseña un programa que solicite la lectura de un numero entre 0 y 10 (ambos inclusive)."
"Si el usuario teclea un numero fuera de rango vlido, el programa solicitara nuevamente la introduccion del valor cuantas veces sea necesario"


num1 = 0
num2 = 10
num3= int(input("Ingrese un numero entre 0 y 10: "))

while num3 >= num1 and num3 <= num2:
    print(num3)
    num3= int(input("Ingrese un numero entre 0 y 10: "))

print("Usted ha terminado el programa al ingresar un numero mayor a 10")