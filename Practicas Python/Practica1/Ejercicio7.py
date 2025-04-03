mes = int(input("Ingrese el número del mes (1-12): "))
año = int(input("Ingrese el año: "))

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if 1 <= mes <= 12:
    es_bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
    if es_bisiesto and mes == 2:
        dias = 29
    else:
        dias = dias_por_mes[mes - 1]
    print(f"{meses[mes - 1]} {año} tiene {dias} días.")
else:
    print("Mes inválido. Debe estar entre 1 y 12.")