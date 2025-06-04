def pedir_anios(integrantes):
    cantidad_integrantes = int(integrantes)
    lista_anios=[]
    while cantidad_integrantes>0:
        
        anio=int(input("Ingrese el año de nacimiento: "))
        if anio > 2025:
            print("El año no es valido")
        else:
            lista_anios.append(anio)
            cantidad_integrantes -= 1

    return lista_anios

def contar_pares_impares(lista_anios):
    #cuenta cuantos numeros pares hay en una lista
    pares=0
    impares = 0
    for i in lista_anios:
        if i%2==0:
            pares+=1
        else:
            impares+=1
    return pares, impares