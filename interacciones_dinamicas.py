#Programa de práctica de Python de Generation
#Creado por Germán D. Cruz G.
#Programa asistente virtual Parte 4: Interacciones dinámicas

import random
perfil = {
    "nombre": "Germán",
    "edad": 42,
    "color favorito": "azul"
}
#Lista de posibles saludos
saludos = ["¡Hola!", "¡Qué gusto verte!", "¡Buen día! ¿Cómo estás?", "¡Hola de nuevo!"]
#Mensaje de bienvenida
print("Bienvenido a tu asistente virtual. Escribe 'salir' para terminar.")
while True:
    #Las entradas se cambian a letra minúscula para evitar errores
    mensaje = input("Tú: ").lower()
    #El programa se detiene si se digita "salir"
    if mensaje == "salir":
        print("Hasta pronto.")
        break
    #Lista de palabras que el asistente detecta como saludo
    #Se recorre cada palabra de la lista y se comprueba si su contenido
    #está presente en la variable mensaje
    #Se retorna True si al menos una de las opciones es verdadera
    #Lista de palabras a detectar en el mensaje
    palabras_clave = ["hola", "buenas", "saludos"]
    #Variable de control
    encontrado = False  
    for palabra in palabras_clave:
        if palabra in mensaje:
            encontrado = True
            #Si ya se encontró una de las palabras, se deja de buscar      
            break
    if encontrado:
        print("Asistente:", random.choice(saludos))
    
    #Buscar información en el perfil
    elif "color" in mensaje and "favorito" in mensaje:
        print("Asistente: Tu color favorito es", perfil.get("color favorito", "desconocido"))
    elif "edad" in mensaje:
        print("Asistente: Tu edad es", perfil.get("edad", "desconocida"))
    elif "nombre" in mensaje:
        print("Asistente: Tu nombre es", perfil.get("nombre", "desconocido"))

    #Respuesta genérica
    else:
        print("Asistente: No entendí tu saludo o tu solicitud.")
        

     


        
        
