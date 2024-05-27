def convertir_a_entero():
    try:
        numero = input("Ingrese un número: ")
        
        numero_entero = int(numero)
        
        print(f"El número convertido a entero es: {numero_entero}")
        
    except ValueError:
        print("Error: El valor ingresado no es un número válido. Por favor, ingrese un número entero.")

convertir_a_entero()
