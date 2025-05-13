'''
2) Escribir una función que tenga como parámetro el correo de una persona. El correo puede ser de
dos tipos:
a) nombre.apellido@alum.ub.edu.ar
b) nombre.appellido@prof.ub.edu.ar
Diseñar una función para mostrar un cartel que indique si el correo es de un profesor o de un
alumno y completar el mensaje con el nombre y apellido de la persona.
Hacer un programa que permita ingresar correos, finalizar el ingreso con ‘@’ y mostrar para cada
correo el nombre y apellido de cada uno, indicando si es profesor o alumno (usar la función
diseñada para tal fin), además, calcular y mostrar la cantidad de correos de profesores.
'''

#Funciones de reemplazo

def mi_len(cadena):
    contador = 0
    for _ in cadena:
        contador += 1
    return contador


#Funcion principal

def tipo_correo(correo):
    
    #Divido el correo en dos partes usando el '@'
    
    partes = correo.split('@')
    
    if mi_len(partes) != 2:
        print("Correo inválido")
        return None

    nombre_apellido = partes[0]
    dominio = partes[1]

    #Separo nombre y apellido
    
    if '.' in nombre_apellido:
        nombre, apellido = nombre_apellido.split('.')
        
    else:
        print("Correo inválido")
        return None

    #Verifico si es alumno o profesor
    
    if dominio == "alum.ub.edu.ar":
        print(f"{nombre} {apellido} es Alumno")
        return "Alumno"
    
    elif dominio == "prof.ub.edu.ar":
        print(f"{nombre} {apellido} es Profesor")
        return "Profesor"
    
    else:
        print("Dominio desconocido")
        return None

#Programa principal

profesores = 0

while True:
    
    correo = input("Ingrese un correo (o '@' para terminar): ")
    
    if correo == "@":
        break
    
    tipo = tipo_correo(correo)
    
    if tipo == "Profesor":
        profesores += 1

print(f"Cantidad de correos de profesores: {profesores}")
