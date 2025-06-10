'''
Náufragos es un juego basado en el juego Galaxis que consiste en rescatar personas perdidas en el espacio.
En nuestro caso, el rescate se produce en el mar, y el objetivo es rescatar la máxima cantidad de personas, con la menor cantidad de sondas detectoras.
Una sonda detectora es un artefacto que se utiliza para detectar personas. Cuando una sonda es activada en una posición dada, ésta envía una señal en dirección de cada uno de los cuatro puntos cardinales.
La señal se propaga hasta perderse salvo que choque con el dispositivo reflector de alguno de los náufragos.
En ese caso, la señal retorna a la sonda lo que produce que se encienda una luz intermitente sobre la cubierta de la sonda.
Note que cada sonda tiene una única luz, por lo cual cuando la luz comienza a parpadear, no hay forma de saber si esto ocurre por que retornaron varias señales o sólo una,
tampoco hay cómo saber desde que dirección retornó la señal, y menos aún, a qué distancia de la sonda se encontraba el dispositivo reflector que hizo retornar la señal.
Sin embargo la sonda detectora sí es capaz de determinar si ella es activada en la posición en que se encuentra un náufrago, en cuyo caso la luz se enciende y no parpadea.
Cuando esto sucede, el náufrago puede ser rescatado desde la posición en que se ha activado la sonda.
En el siguiente ejemplo se muestra las posiciones de 4 náufragos, representados por la letra N.
Así, si la sonda detectora es activada en la posición [3,3] la señal se pierde, en tanto que si es activada en la posición [6,2] se detecta un náufrago, y en la posición [6,5] se rescata un náufrago.
Estrategia de solución Para implementar este juego se utiliza una lista bidimensional que representar´a el tablero correspondiente al espacio del naufragio.
El tamaño del tablero será configurable, y en él se dispondrán los náufragos en posiciones aleatorias.
La cantidad de náufragos, así como la cantidad de sondas disponibles también será configurable.
En cada paso, debe pedirse al jugador la posición en la cual desea activar una sonda detectora.
El algoritmo deberá determinar si en esa posición existe un náufrago, si en alguna de las cuatro direcciones existe un náufrago, o si la señal se pierde.
En cualquier situación debe notificar el resultado al jugador.
Esta rutina se repite hasta que se hayan rescatado todos los náufragos, o se acaben las sondas detectoras.
'''

import random

# Crea el tablero y coloca los náufragos en posiciones aleatorias
def crear_tablero(filas, columnas, cantidad_naufragos):
    
    tablero = []
    
    for i in range(filas):
        
        fila = []
        
        for j in range(columnas):
            
            fila.append('.')
            
        tablero.append(fila)
        
    naufragos_colocados = 0
    
    while naufragos_colocados < cantidad_naufragos:
        
        
        f = random.randint(0, filas-1)
        c = random.randint(0, columnas-1)
        
        if tablero[f][c] == '.':
            tablero[f][c] = 'N'
            naufragos_colocados += 1
            
    return tablero

# Muestra el tablero en pantalla
def mostrar_tablero(tablero, mostrar_naufragos=False):
    
    for fila in tablero:
        linea = ""
        
        for celda in fila:
            
            if celda == 'N' and not mostrar_naufragos:
                linea += ". "
            else:
                linea += celda + " "
                
        print(linea.strip())
        
    print()

# Activa la sonda en la posición elegida
def activar_sonda(tablero, fila, columna):
    
    if tablero[fila][columna] == 'N':
        tablero[fila][columna] = 'R'
        return "¡Naufrago rescatado!"
    
    filas = len(tablero)
    columnas = len(tablero[0])
    
    # Revisar en las 4 direcciones
    direcciones = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for df, dc in direcciones:
        
        f = fila + df
        c = columna + dc
        
        while 0 <= f < filas and 0 <= c < columnas:
            
            if tablero[f][c] == 'N':
                return "¡Señal detectada! (luz parpadea)"
            
            f += df
            c += dc
            
    return "La señal se pierde (no hay naufragos en linea recta)"

# Pide un número entero al usuario y verifica que este en el rango correcto
def pedir_numero(mensaje, minimo, maximo):
    
    correcto = False
    
    while not correcto:
        entrada = input(mensaje)
        
        if entrada.isdigit():
            valor = int(entrada)
            
            if minimo <= valor <= maximo:
                correcto = True
                return valor
            
            else:
                print(f"Por favor, ingrese un numero entre {minimo} y {maximo}.")
                
        else:
            print("Por favor, ingrese un numero valido.")

# Función principal del juego
def juego():
    
    print("Bienvenido al juego Naufrago")
    filas = pedir_numero("¿Cuantas filas tiene el tablero? ", 1, 20)
    columnas = pedir_numero("¿Cuantas columnas tiene el tablero? ", 1, 20)
    
    max_naufragos = filas * columnas
    
    cantidad_naufragos = pedir_numero("¿Cuantos naufragos hay? ", 1, max_naufragos)
    sondas = pedir_numero("¿Cuantas sondas tenes? ", 1, 100)
    
    tablero = crear_tablero(filas, columnas, cantidad_naufragos)
    
    rescatados = 0

    while sondas > 0 and rescatados < cantidad_naufragos:
        
        mostrar_tablero(tablero)
        print(f"Sondas restantes: {sondas}")
        
        fila = pedir_numero(f"Elige la FILA para la sonda (1 a {filas}): ", 1, filas) - 1
        columna = pedir_numero(f"Elige la COLUMNA para la sonda (1 a {columnas}): ", 1, columnas) - 1
        resultado = activar_sonda(tablero, fila, columna)
        
        print(resultado)
        
        if resultado == "¡Naufrago rescatado!":
            rescatados += 1
            
        sondas -= 1

    print("\nJuego terminado.")
    mostrar_tablero(tablero, mostrar_naufragos=True)
    print(f"Naufragos rescatados: {rescatados} de {cantidad_naufragos}")
    
    if (rescatados == 0):
        print("Se murieron todos los marineros")

if __name__ == "__main__":
    juego()