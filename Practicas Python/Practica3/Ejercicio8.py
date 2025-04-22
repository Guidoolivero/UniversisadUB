""""
Un ISBN-10 (International Standard Book Number) consiste de 10 dígitos:
d1d2d3d4d5d6d7d8d9d10.
El último dígito, d10, es el dígito verificador que se calcula como sigue:

Si el dígito verificador es 10, el último dígito es x, de acuerdo a las normas ISBN. Escribir
un programa que permita ingresar los primeros 9 dígitos como una cadena y muestre el
número ISBN.
Ejemplo: 013601267 ---> 0136012671
013031997 ---> 013601267X

"""

""""
Un ISBN-10 (International Standard Book Number) consiste de 10 dígitos:
d1d2d3d4d5d6d7d8d9d10.
El último dígito, d10, es el dígito verificador que se calcula como sigue:

Si el dígito verificador es 10, el último dígito es x, de acuerdo a las normas ISBN. Escribir
un programa que permita ingresar los primeros 9 dígitos como una cadena y muestre el
número ISBN.
Ejemplo: 013601267 ---> 0136012671
013031997 ---> 013601267X


Validación de números ISBN 10
Mira este ejemplo:

Número ISBN-10:0553418025

(10 * 0) + (9 * 5) + (8 * 5) + (7 * 3) + (6 * 4) + (5 * 1) + (4 * 8) + (3 * 0) + (2 * 2) + (1 * 5) = 176


"""

def isbn_10(numero):
    
    verificador = 0
   
    for i in range(1, 10):
       verificador = verificador + int(numero[i-1]) * i
   
    if (verificador % 11 == 10):
        numero = numero + "x"
    
    else:
        numero = numero + str(verificador % 11)
        
    return numero 

    


isbn = input("Ingrese los numero: ")

print(isbn_10(isbn))
