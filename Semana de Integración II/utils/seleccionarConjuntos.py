def seleccionar_conjuntos(dnis, cantidad_conjuntos):
    
    if len(dnis) <= cantidad_conjuntos:
        # Si hay misma cantidad de conjuntos que la cantidad de conjuntos a seleccionar, se devuelven todos
        # Porque la API graficadora los admite
        return dnis
    else :
        # Selección del primer conjunto
        conjuntos = []
        seleccion = -1
        while seleccion < 0 or seleccion > len(dnis) - 1:
            for i, conjunto in enumerate(dnis):
                print(f"{i + 1}. {conjunto}")
            seleccion = int(input("Seleccione el número del primer conjunto (1, 2, ...): ")) - 1
            
            if seleccion < 0 or seleccion > len(dnis) - 1:
                print("Selección inválida. Intente nuevamente.")
            else:
                conjuntos.append(dnis[seleccion])
            
        # Selección del segundo conjunto
        seleccion = -1
        while seleccion < 0 or seleccion > len(dnis) - 1:
            for i, conjunto in enumerate(dnis):
                print(f"{i + 1}. {conjunto}")
            seleccion = int(input("Seleccione el número del segundo conjunto (1, 2, ...): ")) - 1
            if seleccion < 0 or seleccion > len(dnis) - 1:
                print("Selección inválida. Intente nuevamente.")
            else:
                conjuntos.append(dnis[seleccion])
        # Seleccion del tercer conjunto
        seleccion = -1
        if cantidad_conjuntos == 3:
            while seleccion < 0 or seleccion > len(dnis) - 1:
                for i, conjunto in enumerate(dnis):
                    print(f"{i + 1}. {conjunto}")
                seleccion = int(input("Seleccione el número del tercer conjunto (1, 2, ...): ")) - 1
                if seleccion < 0 or seleccion > len(dnis) - 1:
                    print("Selección inválida. Intente nuevamente.")
                else:
                    conjuntos.append(dnis[seleccion])
        return conjuntos