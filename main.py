import os # Importo la biblioteca os con la que puedo interactuar con la terminal
import requests # con esta biblioteca puedo hacer peticiones a la API

import requests # con esta biblioteca puedo hacer peticiones a la API

def buscar_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}" # .lower() por si acaso se ponen mayusculas
    respuesta = requests.get(url)  # hace la peticion con la ruta que le he puesto
    
    if respuesta.status_code == 200: # verifica el paquete de red porque 200 es ok
        datos = respuesta.json()

        stats = {stat["stat"]["name"]: stat["base_stat"] for stat in datos["stats"]} #Con esto extraigo y creo un diccionario de todas las estadisticas del pokemon 
                                                                                    #y luego las voy extrallendo de una en una en la seccion de abajo
        return {                         # El dicionario
            "nombre": datos["name"],
            "altura": datos["height"],
            "peso": datos["weight"],
            "tipos": [tipo["type"]["name"] for tipo in datos["types"]],
            "habilidad": [habilidad["ability"]["name"] for habilidad in datos["abilities"]],
            "movimientos": [movimiento["move"]["name"] for movimiento in datos["moves"]],
            # ---------------------------------------------------------------------------------------------------------------------
            "vida": stats.get("hp"),
            "ataque": stats.get("attack"),
            "defensa": stats.get("defense"),
            "ataque especial": stats.get("special-attack"),
            "defensa especial": stats.get("special-defense"),
            "velocidad": stats.get("speed")

        }
    else:
        return None

def ejecutar_busqueda():
    nombre_pokemon = input("Introduce el nombre o numero del Pokemon: ")
    resultado = buscar_pokemon(nombre_pokemon) # llamo a la función de arriba con el nombre del pokemon para que contacte con la api , si hay devuelve un diccionario del pokemon
    
    if resultado:

        while True:

            os.system("cls" if os.name == "nt" else "clear") # con esto limpio la reter en varios sistemas 

            # Menu--------------------------------------------------------------------
            print(f"\nMenu de informacion del pokemon {resultado['nombre'].capitalize()}: \n") # .capitalize es para mostrar la primera palabra en mayuscula y las demas en minusculas
            print("1-Altura y peso")
            print("2-tipos")
            print("3-habilidad/es")
            print("4-estadisticas")
            print("5-movimientos")
            print("0-salir")
            opcion = int(input("\nIntroduce una opción: "))
            #--------------------------------------------------------------------------

            match opcion:   # Como el swtch en otros lenguajes
                case 1:
                    print(f"\n        Altura: {resultado['altura']/10} metros")
                    print(f"        Peso: {resultado['peso']/10} kilogramos")
                case 2:
                    print(f"\n        Tipos: {', '.join(resultado['tipos'])}") # ', '.join es la separación que se le pondra a los tipos
                case 3:
                    print(f"\n        Habilidad/es: {', '.join(resultado['habilidad'])}") 
                case 4:
                    print(f"\n        Vida: {resultado['vida']}")
                    print(f"        Ataque: {resultado['ataque']}")
                    print(f"        Defensa: {resultado['defensa']}")
                    print(f"        Ataque-especial: {resultado['ataque especial']}")
                    print(f"        Defenda-especial: {resultado['defensa especial']}")
                    print(f"        Velocidad: {resultado['velocidad']}")

                    estadisticas_totales = (resultado['vida']+resultado['ataque']+resultado['defensa']+resultado['ataque especial']+resultado['defensa especial']+resultado['velocidad']) 
                    #Como no se pueden sumar las listas tengo que hacerlo separado primero sumando loas valores númericos y luego meterlos en la lista de abajo

                    print(f"        Estadisticas totales: {estadisticas_totales}")

                case 5:
                    print("\nMovimientos:")
                    for movimientos in resultado['movimientos']:
                        print(f"{movimientos}")
                case 0:
                    print("\nAdios")
                    break
                case _: # por si la opcion del menu no vale
                    print("\nOpción no válida")
            input("\nPresiona Enter para continuar")

    else:
        print("No se encontró ningún Pokemon con ese nombre o numero.")


ejecutar_busqueda()
