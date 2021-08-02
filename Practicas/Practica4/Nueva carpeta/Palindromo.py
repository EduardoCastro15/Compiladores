import random

def r1(palindromo, archivo):
    archivo.write("Se aplico regla 1 a \"" + palindromo + "\".\n")
    if(len(palindromo) == 1):
        return palindromo.replace("P", "e")
    else:
        return palindromo.replace("P", "")

def r2(palindromo, archivo):
    archivo.write("Se aplico regla 2 a \"" + palindromo + "\".\n")
    return palindromo.replace("P", "0")

def r3(palindromo, archivo):
    archivo.write("Se aplico regla 3 a \"" + palindromo + "\".\n")
    return palindromo.replace("P", "1")

def r4(palindromo, archivo):
    archivo.write("Se aplico regla 4 a \"" + palindromo + "\".\n")
    return palindromo.replace("P", "0P0")

def r5(palindromo, archivo):
    archivo.write("Se aplico regla 5 a \"" + palindromo + "\".\n")
    return palindromo.replace("P", "1P1")

def aplicar23(palindromo, archivo):
    regla = random.randint(2,3)
    if(regla == 2):
        palindromo = r2(palindromo, archivo)
    else:
        palindromo = r3(palindromo, archivo)
    
    return palindromo

def aplicar45(palindromo, archivo):
    regla = random.randint(4, 5)
    if(regla == 4):
        palindromo = r4(palindromo, archivo)
    else:
        palindromo = r5(palindromo, archivo)
    
    return palindromo

def inicio():
    while(True):
        opcion = menu()
        if(opcion == 1):
            longitud = pedirLongitud()
            procesar(longitud)
        elif(opcion == 2):
            longitud = generarLongitud()
            procesar(longitud)
        elif(opcion == 3):
            break
        else:
            print(" Ingrese una opcion valida.")

def menu():
    while(True):
        print("\n Palindromo con GLC")
        print(" (1) Ingresar una longitud")
        print(" (2) Generar una longitud")
        print(" (3) Salir")
        try:
            opcion = int(input(" Ingresa una opcion: "))
            break
        except:
            print(" Ingresa una opcion valida.")

    return opcion

def generarLongitud():
    return random.randint(0,10000)

def pedirLongitud():
    while(True):
        try:
            longitud = int(input(" Ingresa la longitud: "))
            if(longitud >= 0 and longitud <= 100000):
                break
            else:
                print(" La longitud debe ser entre 0 y 100000")
        except:
            print(" Ingresa una longitud valida.")

    return longitud

def procesar(longitud):
    procedimiento = open("procedimiento.txt", "w")
    salida = open("salida.txt", "w")
    palindromo = "P"

    if(longitud == 0):
        palindromo = r1(palindromo, procedimiento)
    elif(longitud == 1):
        palindromo = aplicar23(palindromo, procedimiento)
    else:
        palindromo = aplicar45(palindromo, procedimiento)
        if(esPar(longitud)):
            while(True):
                if(longitud+1 == len(palindromo)):
                    palindromo = r1(palindromo, procedimiento)
                    break
                else:
                    palindromo = aplicar45(palindromo, procedimiento)
        else:
            while(True):
                if(longitud == len(palindromo)):
                    palindromo = aplicar23(palindromo, procedimiento)
                    break
                else:
                    palindromo = aplicar45(palindromo, procedimiento)

    salida.write("El resultado es: " + palindromo)

    salida.close()
    procedimiento.close()

def esPar(longitud):
    return longitud % 2 == 0

inicio()
