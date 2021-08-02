from ClaseAutomata import *

#Función que extrae la información del AF del archivo
def LeerAF(PosLinea):
    NombreArchivo = input("Ingresa el nombre del archivo a LeerAF: "); #Recibimos el nombre del archivo
    AF = open(NombreArchivo, "r") #Abrimos el archivo
    TamArchivo = len(open(NombreArchivo).readlines()) #Calculamos el numero de lineas del archivo
    ItemF = [] #Lista para los items del AF
    Trans = [] #Lista para las transiciones de estado

    for i in range(4): #Recorremos los Inicials 4 renglones del archivo
        AF.seek(PosLinea) #Definimos la posición del renglon en el archivo
        Renglon = AF.readline() #Leemos el renglón
        Item = Renglon.split(",") #Distribuimos cada estado en un item de la lista
        Aux = Item.pop() #Sacamos de la lista al Final item
        Aux = Aux.rstrip('\n') #Quitamos el salto de linea al final de la cadena
        Item.append(Aux) #Agregamos un nuevo item al final de la lista
        PosLinea = AF.tell() #Extraemos la linea en donde nos quedamos
        ItemF.append(Item) #Agregamos el item al final de la lista
    
    for i in range(TamArchivo-4): #Recorremos el resto de los renglones del archivo
        AF.seek(PosLinea) #Definimos la posición del renglon en el archivo
        Renglon = AF.readline() #Leemos el renglón
        Item = Renglon.split(",") #Distribuimos cada estado en un item de la lista
        Aux = Item.pop() #Sacamos de la lista al Final item
        Aux = Aux.rstrip('\n') #Quitamos el salto de linea al final de la cadena
        Item.append(Aux) #Agregamos un nuevo item al final de la lista
        PosLinea = AF.tell() #Extraemos la linea en donde nos quedamos
        Trans.append(Item) #Agregamos el item al final de la lista
    ItemF.append(Trans) #Agregamos la ultima transición del AF al final de la lista
    return (ItemF) #Devolvemos la lista con los items finales de cada renglón del archivo

#Función para validar si nuestro AF es correcto
def Validacion(Nodos, Letras, Posicion, Cadena, Total, Validados):
	if Nodos[Posicion].Num != -1: #Condición que nos va a avisar cuando llegemos al final de la lista de estados
		if len(Cadena) == 0: #Si nuestra cadena a validar es 0
			if Nodos[Posicion].Final == True: #Si después de recorrer la cadena estamos en el estado final
				Validados.append(1) #Agregamos un 1 al final de la lista Validados
				print("La Cadena es valida...") #Imprmimos mensaje de correcta validación
		else: #En caso contrario
			if (Cadena[0] in Letras) == False: #Si la posición 1 de la cadena no coincide con la letra del alfabeto
				return
				#Validacion(Nodos, Letras, Posicion, Cadena[1:], Total, Validados) #Aplicamos recursividad avanzando una posición en la cadena
			else: #Si la posición 1 de la cadena coincide con la letra del alfabeto
				Aux2 = Cadena #Copiamos la cadena en una variable auxiliar
				for i in range(len(Nodos[Posicion].Trans)): #Recorremos uno a uno la Lista de Estados
					if Nodos[Posicion].Trans[i][0] == Cadena[0]: #Si la transición origen en el Estado[Posicion] es igual a la posición 1 de la cadena
						Validacion(Nodos, Letras, Nodos[Posicion].Trans[i][1], Aux2[1:], Total, Validados) #Aplicamos recursividad cambiando la
																											#posición de la lista de Estados y avanzando
																											#una posición en la cadena

#Función para agregar las Transiciones extra faltantes
def TransExtra(Letras, Actual):
	Aux = [] #Lista auxiliar
	for i in range(len(Letras)): #Ciclo del tamaño del alfabeto
		if (Letras[i] in Actual) == False:
			Aux.append(Letras[i]) #Agrega la letra del alfabeto al final de la lista auxiliar
	return Aux #Retorna la lista auxiliar

#Función para agregar las letras de c/u de las Transiciones
def LetrasTrans(Nodos, Letras):
	Aux = [] #Lista auxiliar
	for i in range(len(Letras)): #El ciclo es del tamaño de la lista del Alfabeto
		for j in range(len(Nodos.Trans)): #El ciclo es del tamaño de las transciones
			if Letras[i] in Nodos.Trans[j]: #Si la letra del alfabeto es igual alguna de las transiciones de los estados
				Aux.append(Letras[i]) #Va a agregar la letra del alfabeto al final de la lista
	return Aux #Retorna la lista auxiliar

#Función que regresa la posicion de un item de la lista de Nodos
def Pos(Nodos,elemento):
	Aux = -1 #Variable auxiliar
	for i in range(len(Nodos)): #Reocorremos uno a uno la lista de EstadosAF
		if Nodos[i].Num == int(elemento): #Si el estado es igual al estado (origen, letra, destino)
			Aux = i #Guardamos esa posición
	return Aux #Devolvemos la posición

#Función main
if __name__ == "__main__":
	AF = LeerAF(0) #Enviamos la posición 0 del archivo para extraer sus datos en una lista
	Q = AF[0] #Extraemos los estados de la primera posición de la lista
	Q.append(-1) #Marcamos el fin de los estados con -1
	Q = tuple(map(int,Q)) #Convertimos cada item a entero y creamos una tupla inmodificable (Estados)
	Alfabeto = tuple(AF[1]) #Extraemos el alfabeto de la segunda Pos de la lista (Alfabeto)
	q0 = tuple(map(int,AF[2])) #Convertimos cada item a entero y creamos una tupla inmodificable (Estado inicial)
	F = tuple(map(int,AF[3])) #Convertimos cada item a entero y creamos una tupla inmodificable (Estado final)
	Trans = tuple(AF[4]) #Extraemos el total de transiciones de la quinta Pos de la lista (Transiciones)
	EstadosAF = [] #Lista para cada Estado
	Validados = [] #Lista para los estados validados correctamente
	
	if len(q0) > 1: #Validamos que solo exista un estado inicial
		print("Error: No puede haber mas de un estado inicial") #Mensaje de error
		exit() #Salimos

	for i in range(len(Q)): #Recorremos uno a uno los estados para saber cual es el estado inicial y cual el final
		Inicial = False #Declaramos Inicial como falso
		Final = False #Declaramos Final como falso
		if Q[i] in q0: #Verificamos si el Estado i se trata del Estado Inicial
			Inicial = True #Lo marcamos como True para saber que si es
		if Q[i] in F: #Verificamos si el Estado i se trata del Estado Final
			Final = True #Lo marcamos como True para saber que si es
		EstadosAF.append(Estado(Q[i], Inicial, Final)) #Creamos el objeto llamando a la clase Estado y almacenandolo en una lista

	for i in range(len(Trans)): #Recorremos uno a uno las transiciones del AF
		Aux = Pos(EstadosAF, Trans[i][0]) # La funcion nos devuelve la posición del Estado Origen de la Transición i
		if Aux != -1: #En caso de que se encuentre la posición del Estado Origen de la Transición i
			Aux2 = Pos(EstadosAF, Trans[i][2]) # La funcion nos devuelve la posición del Estado Destino de la Transición i
			if Aux2 != -1: #En caso de que se encuentre la posición del Estado Origen de la Transición i
				EstadosAF[Aux].AgregarTrans(Trans[i][1], Aux2) #Agregamos la transición al objeto mediante el método

	for i in range(len(EstadosAF)): #Recorremos uno a uno los Estados Objetos
		Aux = TransExtra(Alfabeto, LetrasTrans(EstadosAF[i], Alfabeto)) #Agregamos las transiciones extra al estado de error
		for j in range(len(Aux)): #Recorremos uno a uno las transiciones extra agregadas
			EstadosAF[i].AgregarTrans(Aux[j], Q.index(-1)) #Agregamos las transicones extra faltantes
	
	Cadena = input("Ingrese la cadena que desea validar: ") #Pedimos la cadena a validar con el AF
	Validacion(EstadosAF, Alfabeto, Pos(EstadosAF, q0[0]), Cadena, Cadena, Validados)
	if len(Validados) == 0: #Si la lista de Validados está vacía
		print("Error: La cadena no es valida...") #Enviamos mensaje de error
		exit()

	