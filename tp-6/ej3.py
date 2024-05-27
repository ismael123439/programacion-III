def leer_linea_tabla():
    try:
        n = int(input("Ingrese un número entero entre 1 y 10 (n): "))
        m = int(input("Ingrese un número entero entre 1 y 10 (m): "))
        
        if n < 1 or n > 10 or m < 1 or m > 10:
            raise ValueError("Ambos números deben estar entre 1 y 10.")
        
        # Nombre del archivo
        nombre_archivo = f"tabla-{n}.txt"
        
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            if m <= len(lineas):
                print(lineas[m-1])
            else:
                print(f"Error: El archivo {nombre_archivo} no tiene una línea {m}.")
    
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no existe.")
    
    except ValueError as e:
        print(f"Error: {e}")

leer_linea_tabla()
