def convertir_a_lista_de_listas(dnis_list):
    dnis_list_normalizados = []
    for dni in dnis_list:
    # Convierte el DNI a string y luego a lista de enteros (manteniendo repeticiones y orden)
        digitos = [int(digito) for digito in str(dni)]
        dnis_list_normalizados.append(digitos)
    return dnis_list_normalizados
## Salida [[3, 5, 4, 5, 9, 8, 3, 1], [3, 5, 2, 2, 1, 4, 9, 0], [1, 2, 3, 4, 6, 5, 4, 7]]
def generar_digitos_unicos(dnis: list):
    dnis_digitos_unicos = []
    for dni in dnis:
        # Convierte el DNI a string, luego a set de enteros para eliminar repeticiones
        digitos_unicos = {int(digito) for digito in str(dni)}
        dnis_digitos_unicos.append(digitos_unicos)
    return dnis_digitos_unicos

#print(generar_digitos_unicos([35459831, 24357864, 11564878]))
## Salida: [{1, 2, 3, 4}, {1, 2, 4, 5, 6}]