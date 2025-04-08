"""
Necesitamos buscar en diversas secuencias de ARN las posibles apariciones del codón
iniciador 'AUG', que marca el inicio de un gen. Como en una secuencia de ARN puede
haber más de un gen, deseamos conocer todas las posiciones en las que aparece dicho
codón. Para ello elaboraremos un programa que ingresará una cadena de caracteres que
representa una secuencia de ARN y comprobará que la secuencia de ARN contiene
únicamente los caracteres 'A','U', 'G' ó 'C'. En caso contrario, la secuencia es inválida y se
deberá imprimir un mensaje adecuado.
"""