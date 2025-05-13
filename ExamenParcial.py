'''
1) Escribir una función que tenga como parámetros una cadena de caracteres y dos números enteros,
n1 y n2, y retorne la cadena con los caracteres invertidos entre n1 y n2.
("abcdxyabcd", 5, 6) -> "abcdyxabcd"
("ejercicios", 1, 3) -> "ejercicios"
("abcdxyabcd", 4, 7) -> "abcayxdbcd"
Usar la función anterior para invertir una palabra ingresada por teclado, si la palabra está
totalmente compuesta de caracteres alfabéticos, se deberá invertir completa:
totalmente → etnemlatot
Si la palabra no es totalmente alfabética se deberá mostrar un cartel especificando que no se
pudo aplicar la función.
'''

# Se tomo el inicio desde 0

'''
Salida del programa
("abcdxyabcd", 4, 5) -> "abcdyxabcd"
("ejercicios", 0, 2) -> "ejercicios"
("abcdxyabcd", 3, 6) -> "abcayxdbcd"
'''

#Reemplazo del len

def mi_len(cadena):
    
    contador = 0
    for _ in cadena:
        contador += 1
    return contador

def mi_sorted(secuencia):
    
    #Hace una copia de la secuencia original
    
    copia = [0] * mi_len(secuencia)
    
    for i in range(mi_len(secuencia)):
        copia[i] = secuencia[i]
        
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


def mi_reverse(secuencia):
    
    invertida = ""
    i = mi_len(secuencia) - 1
    
    while i >= 0:
        invertida += secuencia[i]
        i -= 1
    return invertida

def es_alfabetica(cadena):
    
        for c in cadena:
            if not ('a' <= c <= 'z' or 'A' <= c <= 'Z'):
                return False
        return True


#Funcion para dar vuelta la palabra entre 2 numeros

def caracteresInvertidos(caracter, n1, n2):
    
    if n1 < 0 or n2 >= mi_len(caracter) or n1 > n2:
        
        return caracter

    return caracter[:n1] + caracter[n1:n2+1][::-1] + caracter[n2+1:]


def invertir_palabra(palabra_usuario):
    
    if es_alfabetica(palabra_usuario):
        palabra_ordenada = ""
        for letra in mi_sorted(palabra_usuario):
            palabra_ordenada += letra
        if palabra_usuario == palabra_ordenada:
            print(mi_reverse(palabra_usuario))
        else:
            print("La palabra no está en orden alfabético.")
    else:
        print("No se pudo aplicar la función: la palabra contiene caracteres no alfabéticos.")



#Programa para invertir los caracteres en base a num1 y num2

palabra = input("Ingrese caracteres: ")
num1 = int(input('ingrese el 1er numero: '))
num2 = int(input('Ingrese el 2do numero: '))

print(caracteresInvertidos(palabra, num1, num2))

#Programa para invertir la palabra en caso de que sea alafbetica

palabra2 = input('Ingrese una palabra: ')

invertir_palabra(palabra2)
