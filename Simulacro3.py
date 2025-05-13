'''
Trabajo práctico #6
Un grupo de investigadores se encuentra trabajando en un centro de observación espacial,
donde toman fotografías digitales mediante un nuevo telescopio a una zona aún no
explorada del espacio, con el objetivo de determinar la presencia de nuevos planetas
girando alrededor de las estrellas que allí se encuentran.
Estas fotografías tienen la particularidad de contener muy pocos colores, por lo aque cada
pixel puede ser representado mediante alguna de las siguientes letras que indica su color:
'B', 'N', 'R', 'V', 'A'. De esta forma una imagen es directamente una secuencia de letras.
Además de contener una poca cantidad de colores, también tienen la particularidad de ser
demasiado grandes con la intención de obtener la mejor resolución posible. Por este
motivo los investigadores necesitan de un método para comprimir estas imágenes y luego
poder ser almacenadas.
Mediante un estudio determinaron que un método muy simple para comprimir estas
imágenes es buscar secuencias donde una letra este repetida de forma consecutiva, para
después almacenarse sólo una única letra junto al número de veces que se repite. Para
diferenciar las partes de la imagen que han sido comprimidas, y luego poder recuperar la
imagen original sin ningún problema, se encierran entre paréntesis tanto la letra como el
valor que indica la cantidad de repeticiones. Para lograr una verdadera compresión, se
debe reemplazar una repetición de letras siempre que esta sea mayor que 4, ya que en caso
contrario no se obtiene compresión alguna.
Se pide escribir dos funciones, la primera recibiendo como entrada una cadena de
caracteres conteniendo una imagen sin comprimir y que genere y retorne otra cadena con
la compresión de la imagen y la segunda función que reciba una cadena conteniendo la
imagen comprimida, genere y retorne otra cadena con la imagen descomprimida.
Ejemplo:
primera función
imagen: NNNNNNNNBRAVBRRRRRAAAAAAAVVVVV
imagen comprimida: (N8)BRAVB(R5)(A7)(V5)
'''



def mi_len(cadena):
    contador = 0
    for _ in cadena:
        contador += 1
    return contador



def comprimir_imagen(imagen):
    comprimida = ''
    i = 0
    while i < mi_len(imagen):
        actual = imagen[i]
        contador = 1
        j = i + 1
        while j < mi_len(imagen) and imagen[j] == actual:
            contador += 1
            j += 1
        if contador > 4:
            comprimida += '(' + actual + str(contador) + ')'
        else:
            k = 0
            while k < contador:
                comprimida += actual
                k += 1
        i += contador
    return comprimida

def descomprimir_imagen(imagen):
    descomprimida = ''
    i = 0
    while i < mi_len(imagen):
        if imagen[i] == '(':
            letra = imagen[i+1]
            j = i+2
            numero = ''
            while imagen[j] != ')':
                numero += imagen[j]
                j += 1
            cantidad = 0
            k = 0
            while k < len(numero):
                cantidad = cantidad * 10 + (ord(numero[k]) - ord('0'))
                k += 1
            l = 0
            while l < cantidad:
                descomprimida += letra
                l += 1
            i = j + 1
        else:
            descomprimida += imagen[i]
            i += 1
    return descomprimida


imagen = input('Ingrese una imagen: ')
comprimida = comprimir_imagen(imagen)

print('Imagen comprimida: ', comprimida)
print('Imagen desconprimida: ', descomprimir_imagen(imagen))


# Ejemplo de uso:
# imagen = 'NNNNNNNNBRAVBRRRRRAAAAAAAVVVVV'
# comprimida = comprimir_imagen(imagen)
# print(comprimida)  # (N8)BRAVB(R5)(A7)(V5)
# print(descomprimir_imagen(comprimida))  # NNNNNNNNBRAVBRRRRRAAAAAAAVVVVV



