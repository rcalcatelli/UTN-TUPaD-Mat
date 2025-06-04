from utils.menu import menu, sub_menu_conjuntos, sub_menu_producto_cartesiano
from utils.graficosVenn import diferencia_entre_dos as graficar_diferencia, union_varios as graficar_union, interseccion_varios as graficar_interseccion, diferencia_simetrica_y_diferencias as graficar_diferencias_simetrica
from utils.operaciones import obtener_digitos_compartidos, contar_frecuencia_dni_list, sumar_dni_list
from utils.normalizador import convertir_a_lista_de_listas, generar_digitos_unicos
from utils.productoCartesiano import producto_cartesiano
from utils.anioBisiesto import anio_bisiesto
from utils.operacionesConAnios import pedir_anios, contar_pares_impares
from utils.ingresarCantIntegrantes import ingresar_cantidad_integrantes
from utils.ingresarDnis import ingresar_dnis
from utils.seleccionarConjuntos import seleccionar_conjuntos

OPCION_NO_VALIDA = "Opción no válida. Intente nuevamente."

def main_loop():
    main_menu = True
    while main_menu:
        opcion = menu()
        
        if opcion == "1":
            print("\n")
            cantidad_integrantes = ingresar_cantidad_integrantes()
            dnis_list = ingresar_dnis(cantidad_integrantes) 
            dnis_list_of_lists = convertir_a_lista_de_listas(dnis_list)
            dnis_list_of_sets = generar_digitos_unicos(dnis_list)
            print("\n")
            print(f"Conjunto de digitos unicos de DNI (set): {dnis_list_of_sets}")
            print("\n")
            print(f"Lista de DNI (list): {dnis_list_of_lists}")
            print("\n")
            ejecutar_submenu_conjuntos(dnis_list_of_sets, dnis_list_of_lists)
        
        elif opcion == "2":
            print("\n")
            ejecutar_submenu_producto_cartesiano()
        
        elif opcion == "3":
            print("\n")
            print("Saliendo del programa...")
            main_menu = False
        
        else:
            print(OPCION_NO_VALIDA)


def ejecutar_submenu_conjuntos(dnis, dnis_list): #dnis: array de sets de digitos unicos
    print(f"Conjuntos de dígitos únicos generados: {dnis}")
    print("\n")
    while True:
        sub_option = sub_menu_conjuntos()
        if sub_option == "1":
            print("\n")
            dos_conjuntos_seleccionados = seleccionar_conjuntos(dnis,2)
            print(f"Conjuntos seleccionados: {dos_conjuntos_seleccionados}")
            diferencia_entre_dos = set.difference(*dos_conjuntos_seleccionados)
            print(f'Diferencia entre los conjuntos seleccionados: {diferencia_entre_dos}')
            graficar_diferencia(dos_conjuntos_seleccionados)
            print("\n")
        elif sub_option == "2":
            print("\n")
            tres_conjuntos_seleccionados = seleccionar_conjuntos(dnis,3)
            union_total = set.union(*tres_conjuntos_seleccionados)
            print(f'Union total de digitos unicos: {union_total}')
            graficar_union(tres_conjuntos_seleccionados)
            print("\n")
        elif sub_option == "3":
            print("\n")
            tres_conjuntos_seleccionados = seleccionar_conjuntos(dnis,3)
            interseccion_total = set.intersection(*tres_conjuntos_seleccionados)
            print(f'Intersección total de dígitos únicos: {interseccion_total}')
            graficar_interseccion(tres_conjuntos_seleccionados)
            print("\n")
        elif sub_option == "4":
            print("\n")
            dos_conjuntos_seleccionados = seleccionar_conjuntos(dnis,2)
            diferencia_simetrica_entre_dos = set.symmetric_difference(*dos_conjuntos_seleccionados)
            print(f'Diferencia simétrica entre los conjuntos seleccionados: {diferencia_simetrica_entre_dos}')
            graficar_diferencias_simetrica(dos_conjuntos_seleccionados)
            print("\n")
        elif sub_option == "5":
            print("\n")
            contar_frecuencia_dni_list(dnis_list)
            print("\n")
        elif sub_option == "6":
            print("\n")
            sumar_dni_list(dnis_list)
            print("\n")
        elif sub_option == "7":
            print("\n")
            digitos_compartidos = obtener_digitos_compartidos(dnis)
            print(f"Dígitos compartidos entre todos los conjuntos: {digitos_compartidos}")
            print("\n")
        elif sub_option == "8":
            break
        else:
            print(OPCION_NO_VALIDA)


def ejecutar_submenu_producto_cartesiano():
    while True:
        sub_option = sub_menu_producto_cartesiano()
        if sub_option == "1":
            integrantes  = int(input("Ingrese la cantidad de integrantes: "))
            anios = pedir_anios(integrantes)
            pares, impares = contar_pares_impares(anios)
            print(f"Números pares: {pares}, Números impares: {impares}")
            anio_bisiesto(anios)
            producto_cartesiano(anios)
            break
        else:
            print(OPCION_NO_VALIDA)
