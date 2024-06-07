import os
from funciones_stark import *

while True:
    normalizar_datos(lista_personajes)
    match menu_principal():
        case "1":
            while True:
                match menu_1():
                    case "1":
                        os.system("cls")
                        mostrar_dato(lista_personajes, "nombre")

                    case "2":
                        os.system("cls")
                        mostrar_nombres_datos(lista_personajes, "altura")

                    case "3":
                        os.system("cls")
                        heroe_max_altura = heroe_maximo_minimo(lista_personajes, "altura")
                        mostrar_maximo_minimo(heroe_max_altura, "altura")

                    case "4":
                        os.system("cls")
                        heroe_min_altura = heroe_maximo_minimo(lista_personajes, "altura", False)
                        mostrar_maximo_minimo(heroe_min_altura, "altura")

                    case "5":
                        os.system("cls")
                        altura_promedio_heroe =  dato_promedio(lista_personajes, "altura")
                        mostrar_promedio_dato(altura_promedio_heroe, "altura")
                        
                    case "6":
                        os.system("cls")
                        heroe_max_peso = heroe_maximo_minimo(lista_personajes, "peso")
                        mostrar_maximo_minimo(heroe_max_altura, "peso") 
                        print("----------------------")
                        heroe_max_ = heroe_maximo_minimo(lista_personajes, "peso", False)
                        mostrar_maximo_minimo(heroe_max_altura, "peso")

                    case "7":
                        os.system("cls")
                        print("Fin del programa")
                        break

                os.system("pause")

        case "2":
            while True:
                match menu_2():
                    case "1":
                        os.system("cls")
                        lista_filtrada = filter_heroe(lambda heroe: heroe["genero"] == "M", lista_personajes)
                        mostrar_dato(lista_filtrada, "nombre")    

                    case "2":
                        os.system("cls")
                        lista_filtrada = filter_heroe(lambda heroe: heroe["genero"] == "F", lista_personajes)
                        mostrar_dato(lista_filtrada, "nombre")
                    
                    case "3":
                        os.system("cls")
                        lista_filtrada = filter_heroe(lambda heroe: heroe["genero"] == "M", lista_personajes)
                        heroe_masculino_max_altura = heroe_maximo_minimo(lista_filtrada, "altura")
                        mostrar_maximo_minimo(heroe_masculino_max_altura, "altura")

                    case "4":
                        os.system("cls")
                        lista_filtrada = filter_heroe(lambda heroe: heroe["genero"] == "F", lista_personajes)
                        heroe_fenenino_max_altura = heroe_maximo_minimo(lista_filtrada, "altura")
                        mostrar_maximo_minimo(heroe_fenenino_max_altura, "altura")
                    
                    case "5":
                        os.system("cls")
                        lista_filtrada = filter_heroe(lambda heroe: heroe["genero"] == "M", lista_personajes)
                        altura_promedio_heroes_masculino =  dato_promedio(lista_filtrada, "altura")
                        mostrar_promedio_dato(altura_promedio_heroes_masculino, "altura")

                    case "6":
                        os.system("cls")
                        lista_filtrada = filter_heroe(lambda heroe: heroe["genero"] == "F", lista_personajes)
                        altura_promedio_heroes_femenino =  dato_promedio(lista_filtrada, "altura")
                        mostrar_promedio_dato(altura_promedio_heroes_femenino, "altura")

                    case "7":
                        os.system("cls")
                        lista_agrupada = agrupar_dato(lista_personajes, "color_ojos")
                        mostrar_datos_agrupados(lista_agrupada, "color_ojos")

                    case "8":
                        os.system("cls")
                        lista_agrupada = agrupar_dato(lista_personajes, "color_pelo")
                        mostrar_datos_agrupados(lista_agrupada, "color_pelo")

                    case "9":
                        os.system("cls")
                        lista_agrupada = agrupar_dato(lista_personajes, "inteligencia")
                        mostrar_datos_agrupados(lista_agrupada, "inteligencia")

                    case "10":
                        os.system("pause")
                        print("Fin del programa")
                        break

                os.system("pause")
                
        case "3":
            os.system("cls")
            print("Fin del programa")
            break

    os.system("pause")