from data_stark import lista_personajes

def menu_principal()-> str:

    print(f"{'Menu de Opciones':^50s}")
    print("1- Desafio Stark")
    print("2- Desafio Star 01")
    return input("Ingrese una opcion: ")

"""
A. Analizar detenidamente el set de datos
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
la altura del mismo
D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
F. Recorrer la lista y determinar la altura promedio de los superhéroes
(PROMEDIO)
G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (MÁXIMO, MÍNIMO)
H. Calcular e informar cual es el superhéroe más y menos pesado.
I. Ordenar el código implementando una función para cada uno de los valores
informados.
J. Construir un menú que permita elegir qué dato obtener
"""
def menu_1()-> str:

    print(f"{'Menu de Opciones':^50s}")
    print("1- Nombre de los heroes")
    print("2- Nombre y altura de los heroes")
    print("3- Superheroe mas alto")
    print("4- Superheroe mas bajo")
    print("5- Altura promedio de los heroes")
    print("6- Superheroe mas pesado y menos pesado")
    print("7- Salir")

    return input("Ingrese una opcion: ")

#A
def normalizar_datos(lista:list)-> None:
    for heroe in lista:
        heroe["altura"] = float(heroe["altura"])
        heroe["peso"] = float(heroe["peso"])
        heroe["fuerza"] = int(heroe["fuerza"])

normalizar_datos(lista_personajes)

#B.
def mostrar_dato(lista:list, dato:str)-> None:
    print(f"     {dato.capitalize()}")
    print("------------------")
    for heroe in lista:
        print(heroe[dato])

#C
def mostrar_nombres_datos(lista:list, dato:list)-> None:
    print(f"      Nombre              {dato.capitalize()}")
    print("---------------------------------")
    for heroe in lista:
        print(f"{heroe['nombre']:<20}      {heroe[dato]}")

#D y E
def heroe_maximo_minimo(lista:list, dato:str, maximo:bool = True)-> dict:
    flag = True
    maximo_minimo = 0
    heroe_maximo_minimo = None
    for i in lista:
        if flag or maximo_minimo < i[dato] if maximo else flag or maximo_minimo > i[dato]:
            flag = False
            maximo_minimo = i[dato]
            heroe_maximo_minimo = i
    return heroe_maximo_minimo

#F
def dato_promedio(lista:list, dato:str)-> float:
    tam = len(lista)
    acumulador = 0
    for heroe in lista:
        acumulador += heroe[dato]
    return acumulador / tam

#G
def mostrar_maximo_minimo(heroe, dato)-> None:
    print(f"{heroe['nombre']}  |  {heroe[dato]}")

def mostrar_promedio_dato(dato:str, value:float)-> None:
    print(f"{dato:.2f} promedio de los heroes: {value}")

##########################################################################
"""
Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos,
utilizando un menú que permita acceder a cada uno de los puntos por separado.
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género M
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
G. Recorrer la lista y determinar la altura promedio de los superhéroes de
género M
H. Recorrer la lista y determinar la altura promedio de los superhéroes de
género F
I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (ítems C a F)
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
no tener, Inicializarlo con ‘No Tiene’).
M. Listar todos los superhéroes agrupados por color de ojos.
N. Listar todos los superhéroes agrupados por color de pelo.
O. Listar todos los superhéroes agrupados por tipo de inteligencia
"""

def menu_2()-> str:

    print(f"{'Menu de Opciones':^50s}")
    print("1- Mostrar Heroes genero masculino")
    print("2- Mostrar heroes genero femenino")
    print("3- Superheroe mas alto genero masculino")
    print("4- Superheroe mas bajo genero femenino")
    print("5- Altura promedio de los heroes masculinos")
    print("6- Altura promedio de los heroes femeninos")
    print("7- Heroes por color de ojos")
    print("8- Heroes por color de pelo")
    print("9- Heroes por tipo de inteligencia")
    print("10- Salir")

    return input("Ingrese una opcion: ")

#A
def filter_heroe(filtradora, lista: list)-> list:
    lista_filtrada = []
    for el in lista:
        if filtradora(el):
            lista_filtrada.append(el)
    return lista_filtrada

#j
def agrupar_dato(lista:list, dato:str)-> list:
    lista_datos = []
    for i in lista:
        lista_datos.append(i[dato])
    lista_datos = set(lista_datos)  

    lista_agrupada = []
    for i in lista_datos:
        lista_agrupada.append(filter_heroe(lambda heroe: heroe[dato] == i, lista_personajes))
    return lista_agrupada

def mostrar_datos_agrupados(lista:list, dato:str)->None:
    for i in lista:
        mostrar_nombres_datos(i, dato)
        print()