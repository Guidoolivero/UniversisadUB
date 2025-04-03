
numero = int(input("Ingrese un número entero: "))


mitad = numero / 2
es_doble_de_impar = mitad.is_integer() and (mitad % 2 != 0)

if es_doble_de_impar:
    print(f"{numero} es el doble de {int(mitad)}, que es impar.")
else:
    print(f"{numero} no es el doble de un número impar.")