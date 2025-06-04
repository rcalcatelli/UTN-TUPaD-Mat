
SELECCIONE_OPCION_PROMPT = "Seleccione una opción: "

def menu ():
    print("1. Trabajar con conjuntos")
    print("2. Trabajar con producto cartesiano")
    print("3. Salir")
    opcion = input(SELECCIONE_OPCION_PROMPT)
    return opcion

def sub_menu_conjuntos():
    print("1. Diferencia entre dos conjuntos")
    print("2. Unión de dos conjuntos")
    print("3. Intersección de dos conjuntos")
    print("4. Diferencia simétrica de dos conjuntos")
    print("5. Conteo de Frecuencia de dígitos")
    print("6. Suma total de digitos de cada DNI")
    print("7. Evaluacion de expresion logica de digito compartido")
    print("8. Volver")
    opcion = input(SELECCIONE_OPCION_PROMPT)
    return opcion


def sub_menu_producto_cartesiano():
    print("1.Trabajar con años de nacimiento")
    opcion = input(SELECCIONE_OPCION_PROMPT)
    return opcion

