"Dibujar un triangulo rectangulo de altura h = 5"


def triangulo_rectangulo():
    
    altura = 5
    
    for i in range(altura):
        asterisco = "*" * (i + 1)
        print(asterisco)
        
triangulo_rectangulo()       



def sumas():
    
    a = int(input("Asigne un valor: "))
    b = int(input("Asigne otro valor: " ))
    
    x = a + b
    
    print("La suma de los numeros es: ", x)


sumas()



def calculadora(a, b):
    x = a + b
    y = a - b
    z = a * b
    
    return x,y,z


a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

suma, resta, por = calculadora(a, b)

print(suma, resta, por)