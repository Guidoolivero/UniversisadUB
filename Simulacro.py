"""
Se pide hacer una función que tome como parámetros una palabra y un número n, la función deberá retornar la palabra cortada a n caracteres y retornará la palabra adicionada con el carácter @ si fue cortada.
Ejemplo: mañana, n = 5, la función retorna mañan@. Hacer un programa que lea varias palabras, finalizar el ingreso de datos con una cadena vacía ('\n'),
El programa deberá mostrar las palabras ingresadas, acortadas si corresponde, y el total de palabras que fueron modificadas.
"""

n = 5
cont = 0 

def acortar(palabra, n):
    """
    Si la palabra es más larga que n, la corta y agrega '@'.
    Si no, la retorna igual.
    """
    if len(palabra) > n:
        
        return palabra[:n] + '@'
    
    return palabra


### Programa principal
palabras_modificadas = []  # Lista para almacenar palabras que fueron modificadas
pal = input("Ingrese una palabra: ")

while pal:
    
    palabra_modificada = acortar(pal, n)  # Procesa la palabra
    
    if palabra_modificada != pal:
        cont += 1  # Incrementa el contador si la palabra fue modificada
        palabras_modificadas.append(palabra_modificada)  # Guarda la palabra modificada
        
    print(palabra_modificada)  # Muestra la palabra (modificada o no)
    
    pal = input("Ingrese una palabra: ")  # Solicita la siguiente palabra

print("Cantidad de palabras modificadas:", cont)  # Muestra el total de palabras modificadas
print("Palabras modificadas:")

for palabra in palabras_modificadas:
    print(palabra)  # Muestra cada palabra modificada

'''
def tipo_correo(correo):
    # Divido el correo en dos partes usando el '@'
    partes = correo.split('@')
    if len(partes) != 2:
        print("Correo inválido")
        return None

    nombre_apellido = partes[0]
    dominio = partes[1]

    # Separo nombre y apellido
    if '.' in nombre_apellido:
        nombre, apellido = nombre_apellido.split('.')
    else:
        print("Correo inválido")
        return None

    # Verifico si es alumno o profesor
    if dominio == "alum.ub.edu.ar":
        print(f"{nombre.capitalize()} {apellido.capitalize()} es Alumno")
        return "alumno"
    elif dominio == "prof.ub.edu.ar":
        print(f"{nombre.capitalize()} {apellido.capitalize()} es Profesor")
        return "profesor"
    else:
        print("Dominio desconocido")
        return None

# Programa principal
profesores = 0

while True:
    correo = input("Ingrese un correo (o '@' para terminar): ")
    if correo == "@":
        break
    tipo = tipo_correo(correo)
    if tipo == "profesor":
        profesores += 1

print(f"Cantidad de correos de profesores: {profesores}")

'''