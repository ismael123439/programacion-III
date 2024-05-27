# Ejercicio 1: División por Cero

def dividir_numeros():
    try:
        numerador = float(input("Ingrese el numerador: "))
        denominador = float(input("Ingrese el denominador: "))
        
        # Realizar la división
        resultado = numerador / denominador

        print(f"El resultado de la división es: {resultado}")
        
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero. Por favor, ingrese un denominador distinto de cero.")

dividir_numeros()
