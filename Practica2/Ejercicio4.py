"Construir un programa que permita multiplicar dos numeros enteros positivos empleando el metodo denomindado miltiplicacion rusa."
"Este metodo permite calcular el producto de N por M de la siguiente forma"


a = int(input(print("Inserte el multiplicador: ")))
b = int(input(print("Inserte el multiplicando: ")))



def MultiplicacionRusa(a, b):
    
    resultado = a * b
    return resultado

print(f"{a} * {b} = {MultiplicacionRusa(a,b)}")
             
    
    
    
    

