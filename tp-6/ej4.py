def crear_listin():
    try:
        with open("listin.txt", 'a') as archivo:
            pass
        print("Archivo listin.txt creado o ya existe.")
    
    except Exception as e:
        print(f"Error: {e}")

def consultar_telefono():
    try:
        nombre = input("Ingrese el nombre del cliente: ")
        
        with open("listin.txt", 'r') as archivo:
            for linea in archivo:
                cliente, telefono = linea.strip().split(',')
                if cliente == nombre:
                    print(f"El teléfono de {nombre} es {telefono}.")
                    return
            print(f"Cliente {nombre} no encontrado.")
    
    except FileNotFoundError:
        print("Error: El archivo listin.txt no existe.")
    
    except Exception as e:
        print(f"Error: {e}")

def anadir_cliente():
    try:
        nombre = input("Ingrese el nombre del nuevo cliente: ")
        telefono = input("Ingrese el teléfono del nuevo cliente: ")
        
        with open("listin.txt", 'a') as archivo:
            archivo.write(f"{nombre},{telefono}\n")
        
        print(f"Cliente {nombre} añadido con éxito.")
    
    except Exception as e:
        print(f"Error: {e}")

def eliminar_cliente():
    try:
        nombre = input("Ingrese el nombre del cliente a eliminar: ")
        
        with open("listin.txt", 'r') as archivo:
            lineas = archivo.readlines()
        
        with open("listin.txt", 'w') as archivo:
            encontrado = False
            for linea in lineas:
                if linea.strip().split(',')[0] != nombre:
                    archivo.write(linea)
                else:
                    encontrado = True
            
        if encontrado:
            print(f"Cliente {nombre} eliminado con éxito.")
        else:
            print(f"Cliente {nombre} no encontrado.")
    
    except FileNotFoundError:
        print("Error: El archivo listin.txt no existe.")
    
    except Exception as e:
        print(f"Error: {e}")

crear_listin()