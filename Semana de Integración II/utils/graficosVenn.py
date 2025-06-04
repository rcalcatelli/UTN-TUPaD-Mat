from matplotlib_venn import venn2, venn3
import matplotlib.pyplot as plt

MENSAJE_ERROR = "La función solo soporta 2 conjuntos para mostrar elementos."

# Función para mostrar la diferencia entre dos conjuntos con un diagrama de Venn 

def diferencia_entre_dos(conjuntos, etiquetas=None, titulo='Diferencia entre conjuntos'):
    n = len(conjuntos)
    if n == 2:
        conjunto1, conjunto2 = conjuntos[0], conjuntos[1]
        if etiquetas is None:
            etiquetas = [f'Conjunto {i+1}' for i in range(n)]

        venn = venn2([conjunto1, conjunto2], set_labels=(etiquetas[0], etiquetas[1]))
        plt.title(titulo)

        diferencia_a_b = conjunto1.difference(conjunto2)

        # Mostrar los elementos reales
        if venn.get_label_by_id('10'):
            venn.get_label_by_id('10').set_text('\n'.join(map(str, diferencia_a_b)))
        if venn.get_label_by_id('01'):
            venn.get_label_by_id('01').set_text(None)
        if venn.get_label_by_id('11'):
            venn.get_label_by_id('11').set_text(None)

        # Mostrar A - B como texto debajo del gráfico
        plt.figtext(
            0.5,
            0.01,
            f'{etiquetas[0]} - {etiquetas[1]} = {sorted(diferencia_a_b)}',
            ha='center',
            fontsize=10,
            color='blue'
        )

        plt.show()
    else:
        print(MENSAJE_ERROR)

    
# Función para mostrar la unión de varios conjuntos
# Esta función es para 2 conjuntos, ya que matplotlib_venn no soporta más de 3 conjuntos
# y no se puede mostrar la unión de más de 3 conjuntos en un diagrama de Venn

def union_varios(conjuntos, etiquetas=None, titulo='Unión de conjuntos'):
    n = len(conjuntos)
    if n == 2:
        conjunto1, conjunto2 = conjuntos[0], conjuntos[1]
        if etiquetas is None:
            etiquetas = [f'Conjunto {i+1}' for i in range(n)]
        venn = venn2([conjunto1, conjunto2], set_labels=(etiquetas[0], etiquetas[1]))

        plt.title(titulo)

        # Mostrar union completa
        union = conjunto1 | conjunto2
        if venn.get_label_by_id('10'):
            venn.get_label_by_id('10').set_text(None)
        if venn.get_label_by_id('11'):
            venn.get_label_by_id('11').set_text('\n'.join(map(str, sorted(union))))
        if venn.get_label_by_id('01'):
            venn.get_label_by_id('01').set_text(None)
            
        # Mostrar unión completa abajo
        union = set().union(*conjuntos)
        plt.figtext(
            0.5,
            0.01,
            f'{etiquetas[0]} ∪ {etiquetas[1]} = {sorted(union)}',
            ha='center',
            fontsize=10,
            color='blue'
        )

        plt.show()

    else:
        print(MENSAJE_ERROR)


# Función para mostrar la intersección de varios conjuntos
# Esta función es para 2 o 3 conjuntos, ya que matplotlib_venn no soporta más de 3 conjuntos

def interseccion_varios(conjuntos, etiquetas=None, titulo='Intersección de conjuntos'):
    n = len(conjuntos)
    
    if etiquetas is None:
        etiquetas = [f'Conjunto {i+1}' for i in range(n)]

    inter = set.intersection(*conjuntos)

    if n == 2:
        c1, c2 = conjuntos
        venn = venn2([c1, c2], set_labels=etiquetas)

        plt.title(titulo)

        # Mostrar elementos reales en cada región
        if venn.get_label_by_id('10'):
            venn.get_label_by_id('10').set_text(None)
        if venn.get_label_by_id('01'):
            venn.get_label_by_id('01').set_text(None)
        if venn.get_label_by_id('11'):
            venn.get_label_by_id('11').set_text('\n'.join(map(str, sorted(c1 & c2))))

        # Mostrar intersección final
        plt.figtext(0.5, 0.01, f'{etiquetas[0]} ∩ {etiquetas[1]} = {sorted(inter)}', ha='center', fontsize=10, color='blue')
        plt.show()

    elif n == 3:
        c1, c2, c3 = conjuntos
        venn = venn3([c1, c2, c3], set_labels=etiquetas)

        plt.title(titulo)

        # Etiquetas individuales
        regiones = {
            '100': c1 - c2 - c3,
            '010': c2 - c1 - c3,
            '001': c3 - c1 - c2,
            '110': (c1 & c2) - c3,
            '101': (c1 & c3) - c2,
            '011': (c2 & c3) - c1,
            '111': c1 & c2 & c3,
        }

        for region_id, valores in regiones.items():
            label = venn.get_label_by_id(region_id)
            if label:
                label.set_text('\n'.join(map(str, valores)))

        # Mostrar intersección final
        plt.figtext(0.5, 0.01, f'{etiquetas[0]} ∩ {etiquetas[1]} ∩ {etiquetas[2]} = {sorted(inter)}', ha='center', fontsize=10, color='blue')
        plt.show()

    else:
        print("Sólo se soportan 2 o 3 conjuntos para el diagrama de Venn.")
# Función para mostrar la diferencia simétrica y las diferencias entre dos conjuntos

def diferencia_simetrica_y_diferencias(conjuntos, etiquetas= None, titulo='Diferencia simétrica'):
    n = len(conjuntos)
    if n != 2:
        print(MENSAJE_ERROR)
        return
    if n == 2:
        conjunto1, conjunto2 = conjuntos[0], conjuntos[1]
        if etiquetas is None:
            etiquetas = [f'Conjunto {i+1}' for i in range(n)]
        venn = venn2([conjunto1, conjunto2], set_labels=(etiquetas[0], etiquetas[1]))
        plt.title(titulo)

        # Diferencia A - B
        if venn.get_label_by_id('10'):
            venn.get_label_by_id('10').set_text('\n'.join(map(str, conjunto1.difference(conjunto2))))

        # Diferencia B - A
        if venn.get_label_by_id('01'):
            venn.get_label_by_id('01').set_text('\n'.join(map(str, conjunto2.difference(conjunto1))))

        # Intersección A ∩ B
        if venn.get_label_by_id('11'):
            venn.get_label_by_id('11').set_text(None)

        # Diferencia simétrica A ∆ B
        diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
        plt.figtext(
            0.5,
            0.01,
            f'{etiquetas[0]} ∆ {etiquetas[1]} = {sorted(diferencia_simetrica)}',
            ha='center',
            fontsize=10,
            color='blue'
        )

        plt.show()
    else:
        print(MENSAJE_ERROR)