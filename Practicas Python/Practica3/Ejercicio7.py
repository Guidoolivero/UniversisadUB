"""

Escribir un programa que ingrese un número telefónico como un string y convierta los
caracteres a el dígito correspondiente, ejemplo:
1-800-FLOWERS ---> 1-800-3569377
"""
"""

Escribir un programa que ingrese un número telefónico como un string y convierta los
caracteres a el dígito correspondiente, ejemplo:
1-800-FLOWERS ---> 1-800-3569377

"""


def numero_telefonico(letra):
    
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
            return str(numero)
             
    return letra
    
    
def convertir_numero_telefonico(texto):
        resultado = ""
        
        for caracter in texto: 
            resultado += numero_telefonico(caracter)
        
        return resultado

telefono = input("Ingrese el numero: ")
print("Numeros convertidos: ", convertir_numero_telefonico(telefono))

