#Práctica de código Python de Generation
#Programa de consulta de Pokemon
#Creado por Germán D. Cruz G.
print("Hola, bienvenido a esta consulta de Pokemon.")
inicio = input("Para ver la lista de Pokemon, por favor digita 1.")
import requests
import json
if inicio == "1":
    print("Cargando información...")
    print("Por favor espera.")
    #URL base de la API
    #Definición de URL y solicitud a la API
    #URL base para listar 100 Pokémon (se puede ampliar a más de 1000)
    url = "https://pokeapi.co/api/v2/pokemon?limit=100" 
    respuesta = requests.get(url)
    #Se convierte la respuesta de la api en un objeto json
    if respuesta.status_code == 200:
        datos = respuesta.json()
        #La API retorna un listado de nombres de Pokemon en la clave "results"
        resultados = datos["results"]
        print("Lista de Pokemon disponibles: ")
        for pokemon in resultados:
            print("-", pokemon["name"])          
    else:
        print("El servidor no respondió", respuesta.status_code) 

    #Entrada del nombre del primer Pokemon con modificación a letra minúscula
    nombre_pokemon = input("Por favor digita el nombre de un Pokemon: ").lower()    # #url = f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}'
    url_1 = f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}'
    respuesta_1 = requests.get(url_1)
    #Se convierte la respuesta de la api en un objeto json
    if respuesta_1.status_code == 200:
        datos_1 = respuesta_1.json()
        #La API retorna un listado de datos del Pokemon escogido en "results"
        #resultados_1 = datos_1["results"]
        print("Lista de características del Pokemon: ")
        print(f"Nombre: {datos_1['name']}")
        print(f"ID: {datos_1['id']}")
        print(f"Altura: {datos_1['height'] / 10} m")
        print(f"Peso: {datos_1['weight'] / 10} kg")

        #Mostrar tipos del Pokémon
        print("Tipos: ")
        tipos = datos_1["types"]
        for tipo in tipos:
            nombre_tipo = tipo["type"]["name"]
            print("-", nombre_tipo)

        #Mostrar habilidades
        print("Habilidades: ")
        habilidades = datos_1["abilities"]
        for habilidad in habilidades:
            nombre_habilidad = habilidad["ability"]["name"]
            print("-", nombre_habilidad)

        #Mostrar estadísticas principales
        print("Estadísticas principales: ")
        stats = datos_1["stats"]
        for stat in stats:
            nombre_stat = stat["stat"]["name"]
            valor_stat = stat["base_stat"]
            if nombre_stat in ["speed", "defense", "attack"]:
                print(f"{nombre_stat}: {valor_stat}")   

    #Entrada del nombre del segundo pokemon con modificación a letra minúscula
    nombre_pokemon_1 = input("Ahora, por favor digita el nombre de otro Pokemon: ").lower()    # #url = f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}'
    url_2 = f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon_1}'
    respuesta_2 = requests.get(url_2)
    #Se convierte la respuesta de la api en un objeto json
    if respuesta_2.status_code == 200:
        datos_2 = respuesta_2.json()
        #La API retorna un listado de datos del Pokemon escogido en "results"
        #resultados_1 = datos_1["results"]
        print("Lista de características del Pokemon: ")
        print(f"Nombre: {datos_2['name']}")
        print(f"ID: {datos_2['id']}")
        print(f"Altura: {datos_2['height'] / 10} m")
        print(f"Peso: {datos_2['weight'] / 10} kg")

        #Mostrar tipos del Pokémon
        print("Tipos: ")
        tipos = datos_2["types"]
        for tipo in tipos:
            nombre_tipo = tipo["type"]["name"]
            print("-", nombre_tipo)

        #Mostrar habilidades
        print("Habilidades: ")
        habilidades = datos_2["abilities"]
        for habilidad in habilidades:
            nombre_habilidad = habilidad["ability"]["name"]
            print("-", nombre_habilidad)

        #Mostrar estadísticas principales
        print("Estadísticas principales: ")
        stats = datos_2["stats"]
        for stat in stats:
            nombre_stat = stat["stat"]["name"]
            valor_stat = stat["base_stat"]
            if nombre_stat in ["speed", "defense", "attack"]:
                print(f"{nombre_stat}: {valor_stat}") 

        #Simulador de batalla
        #Se obtiene el segundo atributo (attack) de cada Pokemon
        atributo1 = datos_1["stats"][1]["base_stat"]
        atributo2 = datos_2["stats"][1]["base_stat"]

        #Se muestran los valores
        print(f"Ataque de {nombre_pokemon}: {atributo1}")
        print(f"Ataque de {nombre_pokemon_1}: {atributo2}")

        #Se comparan los valores
        print("Resultado de la batalla Pokemon.")
        if atributo1 > atributo2:
            print(f"{nombre_pokemon} gana, tiene mejor ataque.")
        elif atributo2 > atributo1:
            print(f"{nombre_pokemon_1} gana, tiene mejor ataque.")
        else:
            print("Ambos tienen el mismo ataque.")

    else:
       print("El servidor no respondió", respuesta.status_code) 
else: 
    print("Intenta de nuevo. Gracias")

            
