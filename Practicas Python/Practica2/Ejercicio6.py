"Diseñar un programa que genere una lista de números usando el siguiente proceso:"
"comenzar con un entero n que deberá ingresar el usuario. Si n es par, dividirlo por 2. Si n"
"es impar, multiplicarlo por 3 y sumarle 1. Repetir este proceso hasta que el nuevo valor obtenido para n sea 1."
"Ejemplo, para n = 22, la secuencia que se obtiene es:"
"22 11 33 17 52 26 13 40 20 10 5 16 8 4 2 1"

num1 = int(input("Ingrese un numero: "))
lista_numeros = [num1]

while num1 != 1:
    if num1 % 2 == 0:
        num1 = num1 // 2
        lista_numeros.append(num1)
        print(lista_numeros)
    else:
        num1 = (num1 * 3) + 1
        lista_numeros.append(num1)
        print(lista_numeros)
    
   