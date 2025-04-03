"Construir un programa que permita multiplicar dos numeros enteros positivos empleando el metodo denomindado miltiplicacion rusa."
"Este metodo permite calcular el producto de N por M de la siguiente forma"





def MultiplicacionRusa():
   
   multiplicando = int(input(print("Inserte el multiplicador: ")))
   multiplicador = int(input(print("Inserte el multiplicando: ")))
   acum = 0 
    
   while multiplicando >= 1:
      if multiplicando % 2 != 0:
         acum = acum + multiplicador
         multiplicando = multiplicando // 2
         multiplicador = multiplicador * 2
         
   print(f"La respuesta es: {acum}")
         

         
          
MultiplicacionRusa()
             
    
    
    
    

