import random
bitacora = open("bitacora.txt", "w")
pali = open("palindromo.txt", "w")
pali.write("Palindromo Generado:\n")
limite = 0
while(1):
    print("Bienvenido al generador de Palindromos!\n\n1. Generar palindromo con longitud especifica\n2. Generar palindromo con longitud aleatoria\n3. Salir")
    opcion = int(input("Opcion: "))
    if(opcion==1):
        limite = int(input("Ingrese el limite: "))
    else:
        if(opcion==2):
            limite = random.randint(1,100000)
            print("Generando Palindromo de "+str(limite)+"")
        else:
            if(opcion==3):
                break
            else:
                print("Opcion invalida\n")
    if(limite==0):
        bitacora.write("Regla 1 - Epsilon\tPalindromo actual: E\n")
        pali.write("E")
        bitacora.close()
        pali.close()
        break
    else:
        if(limite==1):
            reglaR = random.randint(2,3)
            if(reglaR==2):
                bitacora.write("Regla 2 - Ingresando 0\tPalindromo actual: 0\n")
                pali.write("0")
                bitacora.close()
                pali.close()
                break
            else:
                bitacora.write("Regla 3 - Ingresando 1\tPalindromo actual: 1\n")
                pali.write("1")
                bitacora.close()
                pali.close()
                break
        else:
            palAux = ""
            reglaR = random.randint(4,5)
            if(reglaR==4):
                palAux = "0P0"
                bitacora.write("Regla 4 - Ingresando 0P0\tPalindromo actual: "+palAux+"\n")
            else:
                palAux = "1P1"
                bitacora.write("Regla 5 - Ingresando 1P1\tPalindromo actual: "+palAux+"\n")
            if(limite % 2 == 0):
                print("\n------Palindromo Par------\n")
                while(1):
                    if(len(palAux)==limite+1):
                        #eliminar P
                        pal = ""
                        for x in palAux:
                                if(x=='P'):
                                    pal = pal + ''    
                                else:
                                    pal = pal + x
                        pali.write(pal)
                        bitacora.write("Regla 1 - Epsilon\tPalindromo actual: "+pal+"\n")
                        bitacora.close()
                        pali.close()
                        break
                    else:
                        reglaR = random.randint(4,5)
                        if(reglaR==4):
                            #0P0
                            pal = ""
                            for x in palAux:
                                if(x=='P'):
                                    pal = pal + '0P0'    
                                else:
                                    pal = pal + x
                            palAux = pal
                            pal = ""
                            bitacora.write("Regla 4 - Ingresando 0P0\tPalindromo actual: "+palAux+"\n")
                        else:
                            #1P1
                            pal = ""
                            for x in palAux:
                                if(x=='P'):
                                    pal = pal + '1P1'    
                                else:
                                    pal = pal + x
                            palAux = pal
                            pal = ""
                            bitacora.write("Regla 5 - Ingresando 1P1\tPalindromo actual: "+palAux+"\n")
            else:
                print("\n------Palindromo Impar-----\n")
                while(1):
                    if(len(palAux)==limite):
                        #Cambiar P
                        pal = ""
                        for x in palAux:
                                if(x=='P'):
                                    reglaR = random.randint(2,3)
                                    if(reglaR==2):
                                        pal = pal + '0' 
                                    else:
                                        pal = pal + '1'
                                else:
                                    pal = pal + x
                        pali.write(pal)
                        bitacora.write("Regla "+str(reglaR)+" - Epsilon\tPalindromo actual: "+pal+"\n")
                        bitacora.close()
                        pali.close()
                        break
                    else:
                        reglaR = random.randint(4,5)
                        if(reglaR==4):
                            #0P0
                            pal = ""
                            for x in palAux:
                                if(x=='P'):
                                    pal = pal + '0P0'    
                                else:
                                    pal = pal + x
                            palAux = pal
                            pal = ""
                            bitacora.write("Regla 4 - Ingresando 0P0\tPalindromo actual: "+palAux+"\n")
                        else:
                            #1P1
                            pal = ""
                            for x in palAux:
                                if(x=='P'):
                                    pal = pal + '1P1'    
                                else:
                                    pal = pal + x
                            palAux = pal
                            pal = ""
                            bitacora.write("Regla 5 - Ingresando 1P1\tPalindromo actual: "+palAux+"\n")    