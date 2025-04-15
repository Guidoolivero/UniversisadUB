"""
Escribir un programa que verifique si un string es una password correcta. Las reglas para
determinar si es correcta son:
Debe tener como mínimo 8 caracteres.
Sólo puede tener letras y dígitos.
Como mínimo debe tener dos dígitos.
"""

def password(word):
    min_caracter = 8
    min_digit = 2
    
    if len(word) < min_caracter:
        print("Error: La contraseña debe tener al menos 8 caracteres.")
        return False

    
    if not word.isalnum():
        print("Error: La contraseña solo puede contener letras y dígitos.")
        return False

    
    digit_count = sum(1 for carac in word if carac.isdigit())
    
    if digit_count < min_digit:
        print("Error: La contraseña debe contener al menos dos dígitos.")
        return False

    print("La contraseña es válida.")
    return True



word = input("Ingrese un password: ")
password(word)







