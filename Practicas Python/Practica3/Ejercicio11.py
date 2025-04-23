"""
La ley de Chargaff dice que en el ADN de un organismo la cantidad de Adenina es la
misma que la de Tiamina, y la de Citosina es la misma que la de Guanina. Dada una
secuencia de nucleótidos del estilo de ATTACCAGTACA... podemos comprobar si cumple
dicha ley de la siguiente forma:
Contamos la cantidad de A, T, C y G presentes en la cadena y calculamos los coeficientes

donde NX indica la cantidad de nucleótidos del tipo X presentes en la secuencia.
Partiremos de una cadena que contiene una cantidad indeterminada de caracteres, que
solo pueden ser A, T, G ó C. Calcula a partir de dicha cadena los coeficientes a y c.
"""

def chargaff():

    NA = 0
    NT = 0
    NC = 0
    NG = 0

    for letra in cadena:
        if letra == "A":
            NA += 1
        elif letra == "T":
            NT += 1
        elif letra == "C":
            NC += 1
        elif letra == "G":
            NG += 1

    if NT != 0:
        coef_a = NA / NT
    else:
        coef_a = "No se puede calcular (NT=0)"

    if NG != 0:
        coef_c = NC / NG
    else:
        coef_c = "No se puede calcular (NG=0)"

    print("Cantidad de A:", NA)
    print("Cantidad de T:", NT)
    print("Cantidad de C:", NC)
    print("Cantidad de G:", NG)
    print("Coeficiente a (A/T):", coef_a)
    print("Coeficiente c (C/G):", coef_c)

cadena = input("Ingrese la secuencia de ADN (solo A, T, C, G): ").upper()

chargaff()







