def contar_frecuencia_dni(numeros):
    """Recibe una lista de números y devuelve un diccionario con la frecuencia de cada número."""
    frecuencia = {}
    for numero in numeros:
        frecuencia[numero] = frecuencia.get(numero, 0) + 1
    return frecuencia

def contar_frecuencia_dni_list(dnis_list:list):
    """Recibe una lista de listas de números y devuelve un diccionario con la frecuencia de cada número."""
    for dnis in dnis_list:
        print(contar_frecuencia_dni(dnis))

def sumar_digitos(numeros):
    """Recibe una lista de números y devuelve la suma de sus dígitos."""
    return sum(numeros)

def sumar_dni_list(dnis_list:list):
    """Recibe una lista de listas de números y devuelve la suma de los dígitos de cada lista."""
    for dnis in dnis_list:
        print(f"La suma de los digitos del DNI {dnis} es: ", sumar_digitos(dnis))

def obtener_digitos_compartidos(conjuntos):
    """Recibe una lista de conjuntos y devuelve el conjunto de dígitos que están en todos ellos."""
    if not conjuntos:
        return set()
    interseccion = conjuntos[0]
    for i, conjunto in enumerate(conjuntos):
        print(f'Conjunto {i +1}: {conjunto}')

    for conjunto in conjuntos[1:]:
        interseccion = interseccion.intersection(conjunto)
    return interseccion
