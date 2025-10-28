#Programa de práctica de Python de Generation
#Creado por Germán D. Cruz G.
#Programa asistente virtual Parte 2: Menú principal
#Asignación e inicio de variables
#Variable opcion iniciada en cero
opcion = 0
#Lista de datos 
datos = []

#Mensaje de bienvenida
print("Bienvenido.")

#Ciclo principal del menú (mientras no se digite 5 (Salir))
while opcion != 5:
    print("===== MENÚ PRINCIPAL =====")
    print("1. Ver información")
    print("2. Agregar datos")
    print("3. Eliminar datos")
    print("4. Realizar cálculo (suma)")
    print("5. Salir")

    # Solicitar opción al usuario
    opcion = int(input("Por favor, elige una opción (1-5): "))
    #Opción 1: Ver información
    if opcion == 1:
        print("1. Ver información")
        if len(datos) == 0:
            print("No hay datos guardados.")
        else:
            print("Datos actuales:", datos)
    #Opción 2: Agregar datos
    elif opcion == 2:
        print("2. Agregar datos")
        nuevo = input("Escribe un dato para agregar: ")
        #Se envía el dato nuevo a la parte final de la lista datos
        datos.append(nuevo)
        print("Dato agregado correctamente.")
    #Opción 3: Eliminar datos
    #En esta parte del programa fue necesario incluir unas lineas
    #adicionales de código para volver a cambiar las variables de tipo
    #numérico int/float a str para poder ejecutar la orden de eliminar
    #datos contenidos en la lista datos.
    elif opcion == 3:
        print("3. Eliminar datos")
        if len(datos) == 0:
            print("No hay datos para eliminar.")
        else:
            print("Datos actuales: ", datos)
            eliminar = input("Escribe el dato que deseas eliminar: ")
            # Crear una nueva lista con los números convertidos a texto
            datos = [str(elemento) if isinstance(elemento, (int, float)) else elemento for elemento in datos]
            print(datos)
            if eliminar in datos:
                #Comando para eliminar el dato
                datos.remove(eliminar)
                print("Dato eliminado correctamente.")
            else:
                print("Ese dato no existe en la lista.")
    #Opción 4: Realizar cálculo (suma)
    #En esta parte del programa fue necesario digitar unas líneas
    #adicionales para cambiar el tipo de datos de str a int/float para
    #poder realizar los cálculos numéricos de suma de las variables
    #contenidas en la lista datos. 
    elif opcion == 4:
        print("4. Realizar cálculo (suma)")
        if len(datos) == 0:
            print("No se encontraron datos.")
        else:
            print("Datos actuales: ", datos)
            # Variable para acumular la suma
            suma = 0
            numeros = False
            parte = 0
            #Verificar si el elemento es de tipo numérico int o float
            #En Python todas las entradas se asumen como datos de tipo string
            #Es necesario cambiar el tipo de dato

            #Recorrer la lista por posición (índice)
            for i in range(len(datos)):
                #Tomar el valor actual
                elemento = datos[i]
                #Verificar si es un número entero
                if elemento.isdigit():
                    datos[i] = int(elemento)
                #Verificar si es un número decimal preguntando si hay un punto en el dato
                elif "." in elemento:
                    #Se crea una nueva variable llamada parte que es una copia de la variable elemento, 
                    #pero con el primer punto (.) encontrado reemplazado por una cadena vacía (""). 
                    #Es decir, elimina el primer carácter de punto de la cadena elemento sin modificar 
                    #la cadena original.    
                    parte = elemento.replace(".", "", 1)
                    if parte.isdigit():
                        datos[i] = float(elemento)
                #Verificar si es numérico y sumar
                if type(datos[i]) == int or type(datos[i]) == float:
                    suma += datos[i]
                    numeros = True
            if numeros:
                print("La suma de los elementos numéricos es:", suma)
            else:
                print("No se encontraron datos numéricos.")                                     
    #Opción 5: Salir
    elif opcion == 5:
        print("5. Salir")
        print("Gracias por usar el programa. Hasta pronto.")
        break
    else: 
        print("Marcación errada. Intenta de nuevo.")        
                      





