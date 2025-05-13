'''
Necesitamos buscar en diversas secuencias de ARN las posibles apariciones del codón
iniciador 'AUG', que marca el inicio de un gen. Como en una secuencia de ARN puede
haber más de un gen, deseamos conocer todas las posiciones en las que aparece dicho
codón. Para ello elaboraremos un programa que ingresará una cadena de caracteres que
representa una secuencia de ARN y comprobará que la secuencia de ARN contiene
únicamente los caracteres 'A','U', 'G' ó 'C'. En caso contrario, la secuencia es inválida y se
deberá imprimir un mensaje adecuado.
'''

def buscar_codon_inicio(secuencia):
    # Validar que la secuencia solo contenga A, U, G, C
    if not all(base in 'AUGC' for base in secuencia):
        print("Secuencia inválida: solo se permiten los caracteres 'A', 'U', 'G' y 'C'.")
        return

    posiciones = []
    for i in range(len(secuencia) - 2):
        if secuencia[i:i+3] == 'AUG':
            posiciones.append(i)

    if posiciones:
        print("El codón 'AUG' aparece en las posiciones:", posiciones)
    else:
        print("El codón 'AUG' no aparece en la secuencia.")

# Ejemplo de uso:
secuencia = input("Ingrese la secuencia de ARN: ").upper()
buscar_codon_inicio(secuencia)



