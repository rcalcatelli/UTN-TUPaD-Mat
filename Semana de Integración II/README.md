<p align="center">
  <img src="assets/logo-utn.png" alt="Logo UTN" width="100%"/>
</p>
<p align="center">
  <strong>Universidad Tecnológica Nacional</strong>
</p>

# Semana de Integración 2 - Conjuntos Numéricos y Python

## Introducción

Este trabajo práctico se realizó con el fin de incorporar y aplicar conocimientos sobre **conjuntos numéricos** y **programación en Python**. 

Se utilizaron herramientas propias del core de Python como `set`, estructuras lógicas de control (`if`, `else`, `for`, `while`), y se integraron librerías externas como `matplotlib` y `matplotlib-venn` para representar gráficamente las operaciones de conjuntos mediante **diagramas de Venn**.

Se utilizó la librería estándar de Python `datetime` para obtener la fecha y el año actual de manera precisa y dinámica, lo que permitió calcular las edades actuales de los integrantes a partir de sus años de nacimiento. Esto garantiza que el programa siempre utilice la fecha real del sistema al ejecutarse, evitando errores manuales o datos desactualizados.

Además, aplicamos conceptos de **Arquitectura de Sistemas Operativos**, automatizando tareas mediante **scripts bash y PowerShell**, lo que permite una experiencia multiplataforma tanto para usuarios de Linux/macOS como de Windows.

---

## Integrantes (ordenados alfabéticamente)

- **Pablo Basualdo Arcati**
- **Hugo Albertini**
- **Renzo Calcatelli**
- **Elias Carulla**
- **Dante Kaddarian**

---

## Consignas

### A. Operaciones con DNIs

- Ingreso de los DNIs (reales o ficticios).
- Generación automática de los conjuntos de **dígitos únicos**.
- Cálculo y visualización de:
  - Unión
  - Intersección
  - Diferencias
  - Diferencia simétrica
- **Conteo de frecuencia** de cada dígito en cada DNI utilizando estructuras repetitivas.
- **Suma total** de los dígitos de cada DNI.
- Evaluación de condiciones lógicas vinculadas con las expresiones trabajadas.

**Ejemplos de condiciones lógicas implementadas:**

- Si un dígito aparece en todos los conjuntos: `Dígito compartido`.

---

### B. Operaciones con años de nacimiento

- Ingreso de los **años de nacimiento** (si hay repeticiones, usar datos ficticios).
- Contar cuántos nacieron en **años pares** e **impares** (uso de estructuras repetitivas).
- Si **todos nacieron después del 2000**, mostrar: `Grupo Z`.
- Si **alguno nació en un año bisiesto**, mostrar: `Tenemos un año especial`.
- Implementar una **función para determinar si un año es bisiesto**.
- Calcular el **producto cartesiano** entre el conjunto de años y el conjunto de edades actuales.

---

### Estructura del proyecto
<pre>
📦 Semana de integracion 2
├── main.py                      # Script principal que ejecuta el programa
├── requirements.txt             # Lista de dependencias a instalar con pip
├── README.md                    # Instrucciones y documentación del proyecto
├── setup.sh                     # Script para automatizar instalación en Linux/macOS
├── setup.ps1                    # Script para automatizar instalación en Windows PowerShell
└── utils/                       # Módulo con funciones auxiliares
    ├── __init__.py              # Inicializa el paquete utils
    ├── graficosVenn.py          # Funciones para generar diagramas de Venn básicos
    ├── graficoVennDiferencia.py # Funciones para graficar diferencias entre conjuntos
    ├── normalizador.py          # Funciones para sanitizar y limpiar entradas del usuario
    ├── menu.py                  # Funciones de menu y submenu
    ├── mainMenu.py              # Función principal de menu para ejecutar al inicio del programa en loop
    └── operaciones.py           # Funciones de operaciones con conjuntos (unión, intersección, etc.)
</pre>

---

### Herramientas externas - Documentación
`matplotlib` y `matplotlib-venn`: https://pypi.org/project/matplotlib-venn/ | https://github.com/konstantint/matplotlib-venn

---

## Setup del entorno y dependencias

### 1. Crear y activar entorno virtual

Desde la raíz del proyecto, abrir una terminal y ejecutar:

#### En Windows (PowerShell):

python -m venv .venv

O ejectuar script: setup.ps1


#### En Linux / macOS:

python3 -m venv .venv

O ejecutar bash: bash setup.sh

---

#### Check:

Comprobar si las dependencias de requirements.txt se encuentran instaladas, caso contrario python install para cada una de las siguientes librerias: matplotlib, matplotlib-venn

---

### Video explicativo

Se ha realizado un video donde se explican los objetivos del proyecto, la estructura del código y
los resultados obtenidos.

**Enlace al video:** https://youtu.be/QuteWDIjAOI
