def acceder_indice():
    lista = []
    
    try:
        indice = int(input("Ingrese el índice al que desea acceder: "))
        elemento = lista[indice]
        
        print(f"El elemento en el índice {indice} es: {elemento}")
        
    except IndexError:
        print("Error: El índice ingresado está fuera del rango de la lista.")
    
    except ValueError:
        print("Error: El índice debe ser un número entero.")

acceder_indice()
