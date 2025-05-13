"""
Hacer una función que  tenga dos parámetros;
el primero es una cadena de caracteres que representa el estado de un tablero de ajedrez en un momento dado para un jugador (blanco o negro),
y un carácter que representa el nombre de una pieza del ajedrez ('Q','K','T','A','C','P', reina, rey, torre, alfil, caballo, peón, respectivamente).
Ejemplo: cad = “Q18K45T88”, se interpreta  como que la reina (Q) está en la posición (1,8), el rey (K) está en la posición (4,5) y la torre (T) está en la posición
(8,8). La función deberá retornar el nombre de la pieza con la posición que ocupa en el tablero.
El programa principal deberá leer la cadena, el carácter, usar la función y mostrar el resultado.
"""

# Función que calcula la longitud de una cadena (reemplazo de len)
def mi_len(cadena):
    
    contador = 0
    for _ in cadena:
        contador += 1
    return contador

# Función que busca la primera aparición de un carácter en una cadena (reemplazo de find)
def mi_find(cadena, caracter):
    
    i = 0
    while i < mi_len(cadena):
        if cadena[i] == caracter:
            return i  
        i += 1
    return -1  # Si no se encuentra, devuelve -1

# Función que busca la pieza en la cadena y retorna su posición
def buscar_pieza(cadena, pieza):
    
    idx = mi_find(cadena, pieza)  
    
    if idx == -1:
        return "Pieza no encontrada"  # Si no está, lo indica
    
    fila = cadena[idx+1]            # Toma el carácter siguiente como fila
    
    columna = cadena[idx+2]         # Toma el siguiente como columna
    
    return f"{pieza} en posición ({fila},{columna})"  # Devuelve el resultado formateado

# --- Programa principal ---
cad = input("Ingrese la cadena del tablero: ")  # Solicita la cadena del tablero
car = input("Ingrese la pieza a buscar (Q,K,T,A,C,P): ")  # Solicita la pieza a buscar
resultado = buscar_pieza(cad.upper(), car.upper())  # Llama a la función para buscar la pieza
print(resultado)  # Muestra el resultado

