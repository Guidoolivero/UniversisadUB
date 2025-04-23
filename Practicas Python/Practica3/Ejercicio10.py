"""
Escribir una programa que permita ingresar un texto y un caracter e imprima la palabra
más larga en la que se encuentra ese carácter.
"""

def palabra_mas_larga_con_caracter():
    

    palabras = texto.split()
    palabra_mas_larga = ""

    for palabra in palabras:
        if caracter in palabra and len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra

    if palabra_mas_larga:
        print("La palabra más larga que contiene el carácter es:", palabra_mas_larga)
    else:
        print("No se encontró ninguna palabra que contenga el carácter.")

texto = input("Ingrese un texto: ")
caracter = input("Ingrese un caracter: ")
palabra_mas_larga_con_caracter()

