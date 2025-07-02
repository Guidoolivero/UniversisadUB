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
        "Autor": [a.strip() for a in autor.split(",")][:3],  # hasta 3 autores
        "CantPags": cantPag,
        "ISBN": isbn,
        "Edicion": edicion,
        "Editorial": editorial,
        "Genero": genero
    }
    libros.append(libro)
    print("Libro agregado")

def eliminar_libro(titulo, isbn):
    for i, libro in enumerate(libros):
        if libro["Titulo"] == titulo or libro["ISBN"] == isbn:
            del libros[i]
            print("Libro eliminado")
            return
    print("Libro no encontrado")

def buscar_libro(titulo, isbn):
    for libro in libros:
        if libro["Titulo"] == titulo or libro["ISBN"] == isbn:
            return libro
    
    return None

def modificar_libro(titulo, isbn):
    libro = buscar_libro(titulo, isbn)
    
    if libro:
        print("Ingrese los nuevos datos (deje vacío para no modificar):")
        
        nuevo_titulo = input(f"Título [{libro['Titulo']}]: ") or libro["Titulo"]
        nuevo_autor = input(f"Autor(es) [{', '.join(libro['Autor'])}]: ") or ", ".join(libro["Autor"])
        nuevo_cantPag = input(f"Cantidad de páginas [{libro['CantPags']}]: ") or libro["CantPags"]
        nuevo_edicion = input(f"Año de edición [{libro['Edicion']}]: ") or libro["Edicion"]
        nuevo_editorial = input(f"Editorial [{libro['Editorial']}]: ") or libro["Editorial"]
        nuevo_genero = input(f"Género [{libro['Genero']}]: ") or libro["Genero"]
        
        libro["Titulo"] = nuevo_titulo
        libro["Autor"] = [a.strip() for a in nuevo_autor.split(",")][:3]
        libro["CantPags"] = nuevo_cantPag
        libro["Edicion"] = nuevo_edicion
        libro["Editorial"] = nuevo_editorial
        libro["Genero"] = nuevo_genero
        
        print("Libro modificado")
        
    else:
        print("No se pudo modificar el libro.")



def listar_libros(filtro=None, valor=None, valor2=None):
    
    encontrados = []
    
    for libro in libros:
        
        if filtro is None:
            encontrados.append(libro)
            
        elif filtro == "genero" and libro["Genero"].lower() == valor.lower():
            encontrados.append(libro)
            
        elif filtro == "autor" and valor in libro["Autor"]:
            encontrados.append(libro)
            
        elif filtro == "editorial" and libro["Editorial"].lower() == valor.lower():
            encontrados.append(libro)
            
        elif filtro == "editorial_rango":
            
            if (libro["Editorial"].lower() == valor.lower() and
                valor2[0] <= libro["Edicion"] <= valor2[1]):
                encontrados.append(libro)
                
        elif filtro == "año" and libro["Edicion"] == valor:
            encontrados.append(libro)
            
        elif filtro == "apellido_letra":
            for autor in libro["Autor"]:
                if autor.strip().split()[-1][0].lower() == valor.lower():
                    encontrados.append(libro)
                    break
                
        elif filtro == "palabra_titulo" and valor.lower() in libro["Titulo"].lower():
            encontrados.append(libro)
            
    if encontrados:
        
        for libro in encontrados:
            mostrar_libro(libro)
            
    else:
        print("No se encontraron libros con ese criterio.")
        
def mostrar_libro(libro):
    print(f"Título: {libro['Titulo']}")
    print(f"Autor(es): {', '.join(libro['Autor'])}")
    print(f"Páginas: {libro['CantPags']}")
    print(f"ISBN: {libro['ISBN']}")
    print(f"Año de edición: {libro['Edicion']}")
    print(f"Editorial: {libro['Editorial']}")
    print(f"Género: {libro['Genero']}")
    print("-" * 40)


def menu():
    
    while True:
        
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
            
            modificar_libro(titulo, isbn)
            
        elif opcion == "3":
            
            titulo = input("Ingrese el título: ")
            isbn = input("Ingrese el ISBN: ")
            
            eliminar_libro(titulo, isbn)
            
        elif opcion == "4":
            
            print("1. Todos")
            print("2. Por género")
            print("3. Por autor")
            print("4. Por editorial")
            print("5. Por editorial y rango de años")
            print("6. Por año de edición")
            print("7. Por letra de apellido de autor")
            print("8. Por palabra en título")
            
            otraOpcion = input("Seleccione tipo de listado: ")
            
            if otraOpcion == "1":
                listar_libros()
                
            elif otraOpcion == "2":
                
                genero = input("Género: ")
                
                listar_libros("genero", genero)
                
            elif otraOpcion == "3":
                
                autor = input("Autor: ")
                
                listar_libros("autor", autor)
                
            elif otraOpcion == "4":
                
                editorial = input("Editorial: ")
                
                listar_libros("editorial", editorial)
                
            elif otraOpcion == "5":
                
                editorial = input("Editorial: ")
                desde = input("Desde año: ")
                hasta = input("Hasta año: ")
                
                listar_libros("editorial_rango", editorial, (desde, hasta))
                
            elif otraOpcion == "6":
                
                año = input("Año de edición: ")
                
                listar_libros("año", año)
                
            elif otraOpcion == "7":
                
                letra = input("Letra del apellido: ")
                
                listar_libros("apellido_letra", letra)
                
            elif otraOpcion == "8":
                
                palabra = input("Palabra en título: ")
                
                listar_libros("palabra_titulo", palabra)
        
        elif opcion == "x":
            
            print("Saliendo del programa...")
            return
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()


