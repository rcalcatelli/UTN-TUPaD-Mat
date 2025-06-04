def ingresar_cantidad_integrantes():
    cant = 0
    while cant < 1 :
        cant = int(input("Ingrese la cantidad de integrantes del grupo: "))
        if cant >= 1:
            return cant
        else:
            print("Error: La cantidad debe estar entre 1 y 10. Intente nuevamente.")