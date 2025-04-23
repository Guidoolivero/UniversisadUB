"""
ISBN-13 es un nuevo estandar para identificar libros. Usa 13 dígitos:
d1d2d3d4d5d6d7d8d9d10d11d12d13 .
El último dígito, es el dígito verificador y se calcula con la siguiente fórmula:

Si el dígito verificador es 10 se reemplaza por 0. El programa deberá permitir ingresar un
número como un string y mostrar el ISBN-13, ejemplo:
978013213080 ---> 9780132130806


978013213079 ---> 9780132130790
"""

def calcular_isbn13(isbn12):
    """Calcula el ISBN-13 completo a partir de los primeros 12 dígitos."""

    # Validación básica de la entrada
    if len(isbn12) != 12 or not isbn12.isdigit():
        return "Entrada inválida. Se requieren 12 dígitos numéricos."

    suma = 0
    for i in range(12): # Iterar sobre los 12 dígitos
        digito = int(isbn12[i])
        # Aplicar peso 1 a posiciones impares (índice 0, 2, ...)
        # y peso 3 a posiciones pares (índice 1, 3, ...)
        if (i + 1) % 2 == 0:
            suma += digito * 3
        else:
            suma += digito * 1

    # Calcular el dígito verificador
    residuo = suma % 10
    digito_verificador = 10 - residuo

    # Si el resultado es 10, el dígito verificador es 0
    if digito_verificador == 10:
        digito_verificador = 0

    # Concatenar el dígito verificador al número original
    isbn13_completo = isbn12 + str(digito_verificador)

    return isbn13_completo

# --- Programa principal ---
isbn_parcial = input("Ingrese los primeros 12 dígitos del ISBN: ")

isbn_completo = calcular_isbn13(isbn_parcial)

print("ISBN-13 completo:", isbn_completo)





