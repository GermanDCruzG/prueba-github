#Programa de práctica de Python de Generation
#Creado por Germán D. Cruz G.
#Programa asistente virtual Parte 1: Inicio de sesión
#Información previamente almacenada
user = ("germandcruzg") 
password = ("12345678")
#Intentos posibles para acceso
intentos = 3
while intentos > 0:
    user1 = input("Por favor, escribe tu usuario: ")
    password1 = input("Por favor, escribe tu contraseña: ")
    if user == user1 and password == password1:
        print("Bienvenido " + user + ". Podemos continuar.")
        break
    else:
        intentos -= 1 
        print("Usuario o contraseña incorrectos.")
        print("Te quedan", intentos, "intentos.")
if intentos == 0:
    print("Acceso bloqueado. Demasiados intentos fallidos.")