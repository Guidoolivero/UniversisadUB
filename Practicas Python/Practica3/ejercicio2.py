"""
Una palabra es "alfabética" si todas sus letras están ordenadas alfabéticamente. Por
ejemplo, "amor", "chino" e "himno" son palabras "alfabéticas". Diseña un programa que lea
una palabra y nos diga si es alfabética o no.

"""

def esAlfabetica(word):

    
    if list(word) == sorted(word):
        print("Es alfabetica")
        
    else: 
        print("No es alfabetica")
        
    
word = str(input("Ingrese una palabra: "))
        
     
esAlfabetica(word)        
        
        
    
    
    
    