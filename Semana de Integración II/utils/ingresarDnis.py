#y luego le solicite los DNI. 
#en base a ese FOR vas a sacar 2 variables, una que sea de tipo set, y otra que sea de tipo list.
def ingresar_dnis(cant_integrantes):
    dnis_list = []
    for i in range(cant_integrantes):
        dni_input = input(f"Ingrese el DNI del integrante {i + 1}: ")
        while not dni_input.isdigit() or int(dni_input) < 1000000 or int(dni_input) > 99999999:
            print("DNI inválido. Debe tener entre 7 y 8 dígitos y solo contener números.")
            dni_input = input(f"Ingrese el DNI del integrante {i + 1} nuevamente: ")
        dni = int(dni_input)
        dnis_list.append(dni)
    return dnis_list

#salida [35459831, 35221490, 12346547]