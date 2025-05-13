"""
Dos palabras son anagramas si tienen las mismas letras pero en otro orden. Por ejemplo,
«torpes» y «postre» son anagramas, mientras que «aparta» y «raptar» no lo son, ya que
«raptar» tiene una r de más y una a de menos.
Escriba la función sonAnagramas(p1, p2) que indique si las palabras p1 y p2 son
anagramas:
sonAnagramas('torpes', 'postre') ---> True
sonAnagramas('aparta', 'raptar') ---> False
"""

def sonAnagramas(p1, p2):
    # Si las longitudes son distintas, no pueden ser anagramas
    if len(p1) != len(p2):
        return False
    # Ordena ambas palabras y compara
    return sorted(p1) == sorted(p2)

# Ejemplos de uso:
print(sonAnagramas('torpes', 'postre'))  # True
print(sonAnagramas('aparta', 'raptar'))  # False