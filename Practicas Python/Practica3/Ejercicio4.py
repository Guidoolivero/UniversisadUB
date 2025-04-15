""""
Haz un programa que lea dos cadenas que representen sendos números binarios. A
continuación, el programa mostrará el número binario que resulta de sumar ambos (y que
será otra cadena). Si, por ejemplo, el usuario introduce las cadenas ’100’ y ’111’, el
programa mostrará como resultado la cadena ’1011’.
Nota: El procedimiento de suma con acarreo que implementes deberá trabajar
directamente con la representación binaria leída.

"""

def suma_binaria(a, b):
    # Asegurar que ambas cadenas tengan la misma longitud rellenando con ceros a la izquierda
    max_longitud = max(len(a), len(b))
    a = a.zfill(max_longitud)
    b = b.zfill(max_longitud)

    resultado = ""
    acarreo = 0

    # Recorrer las cadenas de derecha a izquierda
    for i in range(max_longitud - 1, - 1, - 1):
        suma = int(a[i]) + int(b[i]) + acarreo
        resultado = str(suma % 2) + resultado  # Agregar el bit resultante al inicio
        acarreo = suma // 2  # Calcular el acarreo

    # Si queda un acarreo al final, agregarlo al resultado
    if acarreo:
        resultado = "1" + resultado

    return resultado


# Solicitar los números binarios al usuario
a = input("Ingrese un número binario: ")
b = input("Ingrese otro número binario: ")

# Mostrar el resultado de la suma
resultado = suma_binaria(a, b)
print(f"La suma de {a} y {b} es: {resultado}")










