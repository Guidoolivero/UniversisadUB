# Reemplazo de len
def mi_len(cadena):
    contador = 0
    for _ in cadena:
        contador += 1
    return contador

# Reemplazo de append para listas
def mi_append(lista, elemento):
    nueva_lista = [0] * (mi_len(lista) + 1)
    for i in range(mi_len(lista)):
        nueva_lista[i] = lista[i]
    nueva_lista[mi_len(lista)] = elemento
    return nueva_lista

# Reemplazo de find (devuelve el índice de la primera aparición o -1 si no está)
def mi_find(cadena, caracter):
    i = 0
    while i < mi_len(cadena):
        if cadena[i] == caracter:
            return i
        i += 1
    return -1

# Reemplazo de count (cuenta cuántas veces aparece un carácter)
def mi_count(cadena, caracter):
    contador = 0
    for c in cadena:
        if c == caracter:
            contador += 1
    return contador

# Reemplazo de upper (convierte una cadena a mayúsculas, solo para letras ASCII)
def mi_upper(cadena):
    resultado = ""
    for c in cadena:
        if 'a' <= c <= 'z':
            resultado += chr(ord(c) - 32)
        else:
            resultado += c
    return resultado

# Reemplazo de lower (convierte una cadena a minúsculas, solo para letras ASCII)
def mi_lower(cadena):
    resultado = ""
    for c in cadena:
        if 'A' <= c <= 'Z':
            resultado += chr(ord(c) + 32)
        else:
            resultado += c
    return resultado

# Reemplazo de split (divide una cadena por espacios)
def mi_split(cadena):
    lista = []
    palabra = ""
    for c in cadena:
        if c != " ":
            palabra += c
        else:
            if palabra != "":
                lista = mi_append(lista, palabra)
                palabra = ""
    if palabra != "":
        lista = mi_append(lista, palabra)
    return lista

# Reemplazo de join (une una lista de cadenas con un separador)
def mi_join(separador, lista):
    resultado = ""
    for i in range(mi_len(lista)):
        resultado += lista[i]
        if i < mi_len(lista) - 1:
            resultado += separador
    return resultado

# Reemplazo de replace (reemplaza todas las apariciones de un carácter por otro)
def mi_replace(cadena, viejo, nuevo):
    resultado = ""
    for c in cadena:
        if c == viejo:
            resultado += nuevo
        else:
            resultado += c
    return resultado

# Reemplazo de strip (elimina espacios al principio y al final)
def mi_strip(cadena):
    inicio = 0
    fin = mi_len(cadena) - 1
    while inicio < mi_len(cadena) and cadena[inicio] == " ":
        inicio += 1
    while fin >= 0 and cadena[fin] == " ":
        fin -= 1
    resultado = ""
    i = inicio
    while i <= fin:
        resultado += cadena[i]
        i += 1
    return resultado

# Reemplazo de startswith (verifica si la cadena comienza con un prefijo)
def mi_startswith(cadena, prefijo):
    if mi_len(prefijo) > mi_len(cadena):
        return False
    for i in range(mi_len(prefijo)):
        if cadena[i] != prefijo[i]:
            return False
    return True

# Reemplazo de endswith (verifica si la cadena termina con un sufijo)
def mi_endswith(cadena, sufijo):
    lc = mi_len(cadena)
    ls = mi_len(sufijo)
    if ls > lc:
        return False
    for i in range(1, ls+1):
        if cadena[-i] != sufijo[-i]:
            return False
    return True

# Reemplazo de isdigit (verifica si todos los caracteres son dígitos)
def mi_isdigit(cadena):
    for c in cadena:
        if not ('0' <= c <= '9'):
            return False
    return mi_len(cadena) > 0

# Reemplazo de isalpha (verifica si todos los caracteres son letras)
def mi_isalpha(cadena):
    for c in cadena:
        if not (('a' <= c <= 'z') or ('A' <= c <= 'Z')):
            return False
    return mi_len(cadena) > 0

# Reemplazo de isalnum (verifica si todos los caracteres son letras o dígitos)
def mi_isalnum(cadena):
    for c in cadena:
        if not (('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')):
            return False
    return mi_len(cadena) > 0

# Reemplazo lógico de la función ord (solo para caracteres ASCII)
def mi_ord(caracter):
    # Devuelve el valor numérico del carácter (solo para un solo carácter)
    # Para letras y dígitos ASCII
    ascii = 0
    for c in range(256):  # Solo para los primeros 256 caracteres
        if chr(c) == caracter:
            ascii = c
            break
    return ascii

# Reemplazo de comparación de igualdad entre dos palabras (sin usar ==)
def mi_igual(palabra1, palabra2):
    if mi_len(palabra1) != mi_len(palabra2):
        return False
    i = 0
    while i < mi_len(palabra1):
        if palabra1[i] != palabra2[i]:
            return False
        i += 1
    return True

def mi_reverse(secuencia):
    invertida = ""
    i = mi_len(secuencia) - 1
    while i >= 0:
        invertida += secuencia[i]
        i -= 1
    return invertida

# Reemplazo de sorted (devuelve una nueva lista con los elementos ordenados, sin usar sorted)
def mi_sorted(secuencia):
    # Hace una copia de la secuencia original
    copia = [0] * mi_len(secuencia)
    for i in range(mi_len(secuencia)):
        copia[i] = secuencia[i]
    # Algoritmo de ordenamiento simple (burbuja)
    n = mi_len(copia)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if copia[j] > copia[j + 1]:
                temp = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = temp
            j += 1
        i += 1
    return copia