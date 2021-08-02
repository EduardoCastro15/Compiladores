from Automata import *
import Thompson

#función para crea tuplas que guardan las transiciones del archivo
def tres(transiciones):
	Aux = [] #Lista auxiliar
	anterior = 0 #Badera auxiliar
	for i in range(0,int(len(transiciones)/3)): #Ciclo del numero de transacciones entre 3
		siguiente = (i+1)*3 #Calculamos el valor del siguiente
		Aux.append(transiciones[anterior:siguiente]) #Agregamos al final de la lista los items dentro del rango anterior y siguiente de las transacciones
		anterior = siguiente #Igualamos ambas variables auxiliares
	return Aux #Retornamos la lista auxiliar

#Función que convierte todas las cadenas de una lista en enteros
def convertir(cadena):
	Aux = [] #Lista auxiliar
	for i in range(0,len(cadena)): #Ciclo del numero de la cadena
		Aux.append(int(cadena[i])) #Agregamos al final de la lista la cadena convertida a entero
	return Aux #Retronamos la lista auxiliar

#Función que crea una lista separando una cadena
def get_elementos(cadena):
	i = 0 #Reinicio del contador
	j = 0 #Reinicio del contador
	elementos = [] #Lista auxiliar
	while i <= len(cadena): #Ciclo dependiente del tamaño de la cadena
		if  i == len(cadena) or cadena[i] == ',' or cadena[i] == '\n': #Si llega al final de la cadena, o si encuentra una coma o un salto de linea
			elementos.append(cadena[j:i]) #Guarda todo lo anterior en un item de la lista auxiliar
			i += 1 #Incrementamos el contador
			j = i #Igualamos el contador
		i+=1  #Incrementamos el contador
	return elementos #Retornamos la lista auxiliar

#Función que crea una nueva lista, usando como delimitador un salto de linea
def get_lista(inicial,cadena):
	i = inicial  #Igualamos el contador
	while cadena[i] != '\n': #Ciclo dependiente de encontrar un salto de linea
		i += 1 #Incrementamos el contador
	return cadena[inicial:i] #Retornamos la lista con el rango indicado

#Función main
if __name__ == "__main__":
	f = open('Thompson2.txt','r') #Abrimos el archivo del AF
	contenido = f.read() #Procedemos a leer el AF
	
	i = 0 #Contador del renglón
	estados = get_lista(i,contenido) #Creamos una lista con los estados del AF
	i += (len(estados) + 1) #Incrementamos el contador de renglónes
	simbolos = get_lista(i,contenido) #Creamos una lista con los simbolos del AF
	i += (len(simbolos) + 1) #Incrementamos el contador de renglónes
	inicial = get_lista(i,contenido) #Creamos una lista con el estado inicial del AF
	i += (len(inicial) + 1) #Incrementamos el contador de renglónes
	final = get_lista(i,contenido) #Creamos una lista con el estado final del AF
	i += (len(final) + 1) #Incrementamos el contador de renglónes
	transiciones = contenido[i:len(contenido)] #Creamos una lista con las transiciones del AF
	
	estados = convertir(get_elementos(estados)) #Separamos los items de la lista y los convertimos las cadenas en enteros
	simbolos = get_elementos(simbolos) #Separamos los items de la lista
	inicial = convertir(get_elementos(inicial)) #Separamos los items de la lista y los convertimos las cadenas en enteros
	final = convertir(get_elementos(final)) #Separamos los items de la lista y los convertimos las cadenas en enteros
	transiciones = tres(get_elementos(transiciones)) #Separamos los items de la lista y los convertimos las cadenas en tuplas
	estados.append(-1) #Agregamos un estado al final de la lista -1
	
	if len(inicial) > 1: #Comprobamos que solo exista un único estado inicial
		print("\nSolo puede haber un estado inicial...") #Mensaje de error
		exit() #Fin del programa
	
	nodos = [] #Lista de nodos
	i = 0 #Reinicio del contador
	for i in range(0,len(estados)): #Ciclo del número de estados
		primero = False #Bandera indicadora del estado inicial
		ultimo = False #Bandera indicadora del estado final
		if estados[i] in inicial: #Comprobamos si el estado actual es el inicial
			primero = True #Bandera verdadera
		if estados[i] in final: #Comprobamos si el estado actual es el final
			ultimo = True #Bandera verdadera
		nodos.append(Estado(estados[i],primero,ultimo)) #Creamos objeto nuevo dentro de lista nodos
	
	i = 0 #Reinicio del contador
	for i in range(0,len(transiciones)): #Ciclo del número de transiciones
		Aux = posicion(nodos,transiciones[i][0]) #Obtenemos la posicion de la transición en la lista de nodos
		if Aux != -1: #Si se logró encontrar la transición buscada
			Aux2 = posicion(nodos,transiciones[i][2]) #Obtenemos la posicion de la transición en la lista de nodos
			if Aux2 != -1: #Si se logró encontrar la transición buscada
				nodos[Aux].agregar_transicion(transiciones[i][1],Aux2) #Mediante el método del objeto, agregamos las transiciones validadas
	
	i = 0 #Reinicio del contador
	for i in range(0,len(nodos)): #Ciclo del número de nodos
		Aux = completar(simbolos,simbolos_transitivos(nodos[i],simbolos)) #Extraemos los simbolos de transición y los completamos
		j = 0 #Reinicio del contador
		for j in range(0,len(Aux)): #Ciclo del número de transiciones no validas
			nodos[i].agregar_transicion(Aux[j],estados.index(-1)) #Mediante el método del objeto, agregamos las transiciones no validas
	print("\n          __________Tabla de formalizada de relaciones__________") #Titulo de la tabla
	imprimir_tabla(nodos,simbolos) #Imprimimos tabla formalizada de relaciones
	
	Nuevos_estados = [] #Lista de nuevos estados
	estados_alcanzables = [str(estados[inicial[0]])] #Lista de estados alcanzables con el estado inicial
	estados_alcanzables += Thompson.Cerradura_E(transiciones,str(estados[inicial[0]])) #Agregamos los estados alcanzables aplicando la cerradura épsilon
	Nuevos_estados.append(Thompson.Estado_AFD('A',estados_alcanzables,0)) #Ya tenemos los nuevos estados alcanzables iniciales, y pertenecen al grupo A
	
	bandera = 1 #Bandera axiliar
	while bandera != 0: #Ciclo dependiente de la bandera
		bandera = 0 #Cambio de la bandera
		i = 0 #Reinicio del contador
		for i in range(0,len(Nuevos_estados)): #Ciclo del número de nuevos estados
			j = 0 #Reinicio del contador
			for j in range(0,len(simbolos)): #Ciclo del número de simbolos
				estados_alcanzables = Thompson.Ir_a(transiciones,simbolos[j],Nuevos_estados[i]) #Modificamos la lista aplicando la función Ir_a
				if Thompson.analisis(Nuevos_estados,estados_alcanzables): #Analizamos comparando los nuevos estados y los estados alcanzables, si son iguales
					letra = chr(ord(Nuevos_estados[len(Nuevos_estados) - 1].simbolo) + 1) #Obtenemos la letra del siguiente grupo de estados
					if Thompson.final(final,estados_alcanzables,estados):
						Nuevos_estados.append(Thompson.Estado_AFD(letra,estados_alcanzables,2)) #Ya tenemos los nuevos estados alcanzables finales
					else:	
						Nuevos_estados.append(Thompson.Estado_AFD(letra,estados_alcanzables,1)) #Ya tenemos los nuevos estados alcanzables normales
					bandera += 1 #Activamos la bandera para repetir el ciclo
	
	N_trancisiones = Thompson.crear_trancisiones(Nuevos_estados,transiciones,simbolos) #Calculamos el número de transiciones
	N_final = [] #Lista de nodos finales
	N_estados = [] #Lista de número de estados
	
	i = 0 #Reinicio del contador
	for i in range(0,len(Nuevos_estados)): #Ciclo del número de nuevos estados
		if Nuevos_estados[i].inicial: #Si el estado actual es inicial
			N_inicial = [i] #Se crea una lista del tamaño del contador
		if Nuevos_estados[i].final: #Si el estado actual es final
			N_final += [i] #Se incrementa la lista del tamaño del contador
		N_estados += [Nuevos_estados[i].simbolo]  #Se incrementa la lista del tamaño del simbolo
	Nuevos_estados.append(Thompson.Estado_AFD("-1",[],1)) #Creamos un nuevo objeto al final de la lista de nuevos estados
	N_estados.append("-1") #Agregamos un -1 al final de la lista
	
	i = 0 #Reinicio del contador
	for i in range(0,len(N_trancisiones)): #Ciclo del número de transiciones
		Aux = Thompson.posicion(Nuevos_estados,N_trancisiones[i][0]) #Obtenemos la posicion de la transición en la lista de nodos
		if Aux != -1: #Si se logró encontrar la transición buscada
			Aux2 = Thompson.posicion(Nuevos_estados,N_trancisiones[i][2]) #Obtenemos la posicion de la transición en la lista de nodos
			if Aux2 != -1: #Si se logró encontrar la transición buscada
				Nuevos_estados[Aux].agregar_transicion(N_trancisiones[i][1],Aux2) #Mediante el método del objeto, agregamos las transiciones validadas
	
	
	i = 0 #Reinicio del contador
	for i in range(0,len(Nuevos_estados)): #Ciclo del número de nuevos estados
		Aux = Thompson.completar(simbolos,Thompson.simbolos_transitivos(Nuevos_estados[i],simbolos)) #Extraemos los simbolos de transición y los completamos
		j = 0 #Reinicio del contador
		for j in range(0,len(Aux)): #Ciclo del número de transiciones no validas
			Nuevos_estados[i].agregar_transicion(Aux[j],N_estados.index("-1")) #Mediante el método del objeto, agregamos las transiciones no validas
	print("\n\n       __________Tabla de simplificada de transicciones__________\n") #Titulo de la tabla
	Thompson.imprimir_tabla_nueva(Nuevos_estados,simbolos) #Imprimimos la tabla simplificada de transacciones

