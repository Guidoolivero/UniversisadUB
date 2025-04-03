"Escribir un programa que muestre, de a 10 numeros por linea y separados por un blanco, todos los numeros entre 100 y 1000 que sean divisibles por 5 y 6"



def programa():

    count = 0

    for num in range(100, 1001):

        if num % 5 == 0 and num % 6 == 0:
            print(num, end=" ")

            count += 1

            if count % 10 == 0:
                print()
        

programa()









