"""
Ejercicio 14 (opcional):
Los biólogos usan una secuencia de letras A, C, T, y G para modelar un genoma. Un gen es
un subcadena de un genoma que comienza después de la tripleta ATG y termina con una
tripleta TAG, TAA, ó TGA. La longiutd de una cadena de gen es un múltiplo de 3 y el gen
no contiene a las tripletas ATG, TAG, TAA y TGA. Escribir un programa que permita
ingresar un genoma y muestre todos los genes en el genoma. Si en la cadena no se
encuentran genes, el programa mostrará un mensaje acorde. Ejemplo:
si la cadena es TTATGTTTTAAGGATGGGGCGTTAGTT, el programa mostrará:
TTT

Programación I Prof. Diana Cicinelli
-----------------------------------============================----------------------------------

GGGCGT
Si la cadena es TGTGTGTATAT entonces se deberá mostrar "no se encontraron genes".
"""

def encontrar_genes(genoma):
    genes = []
    i = 0
    while i < len(genoma) - 2:
        if genoma[i:i+3] == "ATG":
            inicio = i + 3
            fin = inicio
            while fin < len(genoma) - 2:
                tripleta = genoma[fin:fin+3]
                if tripleta in ("TAG", "TAA", "TGA"):
                    gen = genoma[inicio:fin]
                    if len(gen) % 3 == 0 and gen:
                        # Verificar que el gen no contiene ninguna de las tripletas prohibidas
                        contiene_prohibidas = False
                        for j in range(0, len(gen), 3):
                            if gen[j:j+3] in ("ATG", "TAG", "TAA", "TGA"):
                                contiene_prohibidas = True
                                break
                        if not contiene_prohibidas:
                            genes.append(gen)
                    break
                fin += 3
            i = fin + 3
        else:
            i += 1
    return genes

genoma = input("Ingrese la secuencia del genoma: ").upper()
genes = encontrar_genes(genoma)
if genes:
    for gen in genes:
        print(gen)
else:
    print("no se encontraron genes")
