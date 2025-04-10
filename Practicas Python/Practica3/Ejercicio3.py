"""
Hay un tipo de pasatiempos que propone descifrar un texto del que se han suprimido
las vocales. Por ejemplo, el texto ".n .j.mpl. d. p.s.t..mp.s", se descifra sustituyendo cada
punto con una vocal del texto. La solución es "un ejemplo de pasatiempos". Diseña un
programa que ayude al creador de pasatiempos. El programa recibirá una cadena y
mostrará otra en la que cada vocal ha sido reemplazada por un punto.
"""

def pasatiempos(palabra):
    
    vocales = ("aeiou")
    resultado = ""
    
    for caracter in palabra:
        if caracter in vocales:
            resultado += "."
         
        else:
            resultado += caracter    
            
    print(resultado) 
    
palabra = str(input("Ingrese una palabra: "))

pasatiempos(palabra)