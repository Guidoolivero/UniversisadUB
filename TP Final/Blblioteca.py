"""
Se desea hacer un sistema que administre los libros de una biblioteca pequeña. Se deberá diseñar
una base de datos, basada en un lista simplemente encadenada de libros, que permita altas, bajas,
consultas y modificaciones.
La estructura básica para un libro deberá contener la siguiente información: titulo, autor (hasta tres
autores), cantidad de páginas, número ISBN, año de edición, editorial, género al que pertenece
(ficción, política, biografía, historia, aventura, etc), pueden agregarle otros datos que crean
convenientes.
Funcionalidad:
Se deberá permitir realizar las siguientes operaciones:
• Dar de alta un libro (se deberá verificar que el libro no exista).
• Dar de baja un libro (se deberá verificar que el libro exista).
• Consultar por un libro de un determinado título.
• Modificar los datos de un libro.
• Listados:
1. Listar todos los autores existentes.
2. Listar todos los libros existentes.
3. Listar todos los libros de un género determinado.
4. Listar todos los libros que posee un autor determinado.
5. Listar todos los libros de una editorial determinada.
6. Listar todos los libros de una editorial determinada en un rango de años de edición.
7. Listar todos los autores de una determinada editorial.
8. Listar todos los libros que fueron editados en un determinado año.
9. Listar todos los libros de los autores cuyos apellidos comienzan con una letra
determinada.
10. Listar todos los libros cuyos títulos contengan una palabra determinada.
Nota: si lo concideran necesario, pueden usar estructuras de datos auxiliares para desarrollar las
operaciones indicadas.


"""

libros = []


def agregar_libro(titulo, autor, cantPag, isbn, edicion, editorial, genero):
    
    libro = {
         
         "Titulo": titulo,
         "Autor": autor,
         "CantPags": cantPag,
         "ISBN": isbn,
         "Edicion": edicion,
         "Editorial": editorial,
         "Genero": genero
         
    }
    
    libros.append(libro)
    
    print("Libro agregado")
    


def eliminar_libro(titulo, isbn):
    
    return

def buscar_libro(titulo, isbn):
    
    for libro in libros:
        if libro["Titulo"] == titulo or libro["ISBN"] == isbn:
            print(libro)
            print("Libro encontrado")
            
            return libro
        else: 
            print("Libro no encontrado")
    return None

def modificar_libro(titulo, isbn):
    
    return


def listar_libors():

    return

# ...existing code...

def menu():
    
    opcion = ""
    
    while opcion != "x":
        print("\n--- Menú Biblioteca ---")
        print("1. Agregar libro")
        print("2. Modificar libro")
        print("3. Eliminar libro")
        print("4. Listar libros")
        print("X. Salir")
        
        opcion = input("Seleccione una opción: ").strip().lower()
        
        if opcion == "1":
            titulo = input("Ingrese el título: ")
            isbn = input("Ingrese el ISBN: ")
            
            if buscar_libro(titulo, isbn) is None:
                
                autor = input("Ingrese el/los autor/es (separados por coma): ")
                cantPag = input("Ingrese la cantidad de páginas: ")
                edicion = input("Ingrese el año de edición: ")
                editorial = input("Ingrese la editorial: ")
                genero = input("Ingrese el género: ")
                agregar_libro(titulo, autor, cantPag, isbn, edicion, editorial, genero)
                
            else:
                print("El libro ya existe.")
                
        elif opcion == "2":
            
            titulo = input("Ingrese el título: ")
            isbn = input("Ingrese el ISBN: ")
            
            buscar_libro(titulo, isbn)
            
        elif opcion == "3":
            
            pass
        elif opcion == "4":
           
            pass
        elif opcion == "x":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")



if __name__ == "__main__":
    menu()


