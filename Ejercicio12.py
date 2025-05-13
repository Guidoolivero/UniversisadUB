"""
Escribe un programa que lea dos cadenas y devuelva el prefijo común más largo de
ambas. Ejemplo: las cadenas "politécnico" y "polinización" tienen como prefijo común más
largo a la cadena "poli".
"""

# Leer las dos cadenas
cadena1 = input("Introduce la primera cadena: ")
cadena2 = input("Introduce la segunda cadena: ")

# Encontrar el prefijo común más largo
prefijo = ""
i = 0

while i < len(cadena1) and i < len(cadena2):
    if cadena1[i] == cadena2[i]:
        prefijo = prefijo + cadena1[i]
        i = i + 1
    else:
        break

print("El prefijo común más largo es:", prefijo)