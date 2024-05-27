def leer_tabla():
    try:

        n = int(input("Ingrese un número entero entre 1 y 10: "))
        
        if n < 1 or n > 10:
            raise ValueError("El número debe estar entre 1 y 10.")
    
        nombre_archivo = f"tabla-{n}.txt"
        
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no existe.")
    
    except ValueError as e:
        print(f"Error: {e}")

leer_tabla()
