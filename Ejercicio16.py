"""
Las palabras panvocálicas son las que tienen las cinco vocales. Por ejemplo: centrifugado,
bisabuelo, hipotenusa. Escriba la función esPanvocalica(palabra) que indique si una
palabra es panvocálica o no:
esPanvocalica('educativo') ---> True
esPanvocalica('pedagogico') ---> False

"""

def esPanvocalica(palabra):
    vocales = "aeiou"
    for v in vocales:
        if v not in palabra.lower():
            return False
    return True

# Ejemplos de uso:
print(esPanvocalica('educativo'))    # True
print(esPanvocalica('pedagogico'))  # False