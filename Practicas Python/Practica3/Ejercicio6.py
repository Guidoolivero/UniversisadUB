""""
Escribir un programa que retorne el número que le corresponde a una letra en mayúscula
de acuerdo al teclado telefónico
"""


def teclado_telefonico (letra):
    
    numeros = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }
    
    for numero, letras in numeros.items():
        if letra.lower() in letras:
            print(numero) 
    return "Letra no válida"

letra = input("Ingrese una letra: ")

teclado_telefonico(letra)










