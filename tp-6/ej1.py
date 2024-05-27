def guardar_tabla_multiplicar():
    try:
        n = int(input("Ingrese un número entero entre 1 y 10: "))
        
        if n < 1 or n > 10:
            raise ValueError("El número debe estar entre 1 y 10.")

        with open(f"tabla-{n}.txt", "w") as file:
            for i in range(1, 11):
                file.write(f"{n} x {i} = {n * i}\n")
                
        print(f"La tabla de multiplicar del {n} ha sido guardada en el archivo tabla-{n}.txt.")
    
    except ValueError as ve:
        print(f"Error: {ve}")

guardar_tabla_multiplicar()
