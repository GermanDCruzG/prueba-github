#Programa de práctica de Python de Generation
#Creado por Germán D. Cruz G.
#Programa asistente virtual Parte 3: Gestión de información personal
perfil = {
    "nombre": "Germán",
    "edad": 42,
    "color favorito": "azul"
}
opcion = 0

while opcion != 4:
    print("===== GESTIÓN DE PERFIL =====")
    print("1. Ver datos")
    print("2. Agregar o modificar datos")
    print("3. Eliminar datos")
    print("4. Volver al menú principal")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("Tus datos actuales:")
        #Ciclo que recorre los elementos de la secuencia
        #Método del diccionario que genera el par: clave/valor
        for clave, valor in perfil.items():
            #La letra f permite que se muestre el contenido del diccionario perfil
            print(f"{clave}: {valor}")
    elif opcion == 2:
        clave = input("Ingresa el nombre del dato que deseas agregar o modificar: ")
        valor = input("Ingresa el valor: ")
        #Se asigna un valor a una clave en el diccionario perfil
        perfil[clave] = valor
        print("Dato actualizado correctamente.")
    elif opcion == 3:
        clave = input("Ingresa el nombre del dato que deseas eliminar: ")
        #Comprueba si la clave está en el diccionario perfil,
        #se borra la entrada con esa clave de perfil
        if clave in perfil:
            del perfil[clave]
            print("Dato eliminado.")
        else:
            print("Ese dato no existe.")
    elif opcion == 4:
        print("Regresando al menú principal...")
    else:
        print("Opción no válida.")