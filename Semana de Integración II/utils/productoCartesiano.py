from datetime import datetime
# Verificamos si todos los integrantes nacieron después del año 2000
# Usamos la función all() que devuelve True solo si todos cumplen la condición
def producto_cartesiano(list_years):
    years_nacimiento = list_years

    grupo_z(years_nacimiento)
    # Pedimos el año actual para poder calcular las edades
    year_referencia = datetime.now().year

    # Calculamos las edades restando el año de nacimiento al año actual
    edades = [year_referencia - year for year in years_nacimiento]

        # Mostramos las edades calculadas
    print("\nEdades actuales de los integrantes:")
    for i in range(len(edades)):
        if edades[i] < 0:
            print(f"El año del integrante es: {years_nacimiento[i]}, no se puede calcular la edad porque el año de referencia, {year_referencia}, es posterior al año de nacimiento")
        else:
            print(f"Integrante {i+1}: {edades[i]} años")

        # Ahora vamos a calcular el producto cartesiano entre los años y las edades
        # significa que vamos a combinar cada año con cada edad posible 
    producto_cartesiano = []

    # Doble ciclo para combinar cada año con cada edad
    for year in years_nacimiento:
        for edad in edades:
            producto_cartesiano.append((year, edad))  # Agregamos la pareja (año, edad)
        
        # Mostramos el producto cartesiano resultante
    print("\nProducto cartesiano entre años de nacimiento y edades:")
    for par in producto_cartesiano:
        print(par)  # Mostramos cada combinación

def grupo_z(list_year):
    contador = 0
    limite = len(list_year)
    for year in list_year:  
        if year > 2000:
            contador += 1 
    if contador == limite:
        return print("Todos los integrantes pertenecen al Grupo Z")
    else :
        return print("No todos los integrantes pertenecen al Grupo Z")
