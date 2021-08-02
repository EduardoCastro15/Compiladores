#Clase con los metodos de cada Estado 
class Estado:
	#Declaración del constructor
	def __init__(self,numero,inicial,final):
		self.numero = numero
		self.inicial = inicial
		self.final = final
		self.transiciones = []

	#Declaración de metodo para agregar Transición
	def agregar_transicion(self,simbolo,siguiente):
		temp = [simbolo,siguiente]
		self.transiciones.append(temp)

	#Declaración de metodo para agregar Transición siguiente
	def siguiente(self,simbolo,nodos):
		i = 0
		estado = []
		for i in range(0,len(self.transiciones)):
			if self.transiciones[i][0] == simbolo:
				estado = estado + [str(nodos[self.transiciones[i][1]].numero)]
		return estado

#Función para imprimir la tabla formalizada de relaciones
def imprimir_tabla(nodos,simbolos):
	linea = "       |       |" #Borde
	i = 0 #Reinicio del contador
	for i in range(0,len(simbolos)): #Ciclo del número de simbolos
		linea += ("	"+simbolos[i]+"	|") #Almacenamos el encabezado de la tabla
	linea +=("	ε	|") #Concatenamos la columna final épsilon
	separacion = "" #Variable auxiliar
	i = 0 #Reinicio del contador
	
	print(separacion) #Imprimimos separación
	print(linea) #Imprimimos encabezado de la tabla
	print(separacion) #Imprimimos separación

	j = 0 #Reinicio del contador
	for j in range(0,len(nodos)): #Ciclo del número de nodos
		linea = "       | " #Borde
		if nodos[j].numero != -1: #Si no hemos llegado al final de la lista de nodos
			if nodos[j].inicial == True: #Si estamos en el nodo inicial
				linea += "->" #Concatenamos una flecha
			else: #Else
				linea += "  " #Concatenamos un espacio
			if nodos[j].final == True: #Si estamos en el nodo final
				linea += "*" #Concatenamos un asterísco
			else: #Else
				linea += " " #Concatenamos un espacio
		else: #Else
			linea += "  " #Concatenamos un espacio

		linea +=str(nodos[j].numero)+"  |" #Borde
		i = 0 #Reinicio del contador

		for i in range(0,len(simbolos)): #Ciclo del número de símbolos
			linea += ("	"+",".join(nodos[j].siguiente(simbolos[i],nodos))+"	|") #Concatenamos los símbolos de transición + borde

		linea += ("	"+",".join(nodos[j].siguiente('E',nodos))+"	|") #Concatenamos los símbolos de transición + borde
		print(linea) #Imprimimos renglón de la tabla
		print(separacion) #Imprimimos separación

#Función que completa los simbolos que faltan para hacer las trancisiones
def completar(simbolos,actuales):
	aux = [] #Variable auxiliar
	i = 0 #Reinicio del contador
	for i in range(0,len(simbolos)): #Ciclo del número de símbolos
		if (simbolos[i] in actuales) == False: #Si el item de la lista de símbolos no está en la lista actuales
			aux.append(simbolos[i]) #Agregamos al final de la lista el símbolo
	return aux #Retornamos la lista auxiliar

#Función que completa los simbolos trasitivos
def simbolos_transitivos(nodo,simbolos):
	aux = [] #Variable auxiliar
	i = 0 #Reinicio del contador
	for i in range(0,len(simbolos)): #Ciclo del número de símbolos
		j = 0 #Reinicio del contador
		for j in range(0,len(nodo.transiciones)): #Ciclo del número de transiciones del nodo
			if simbolos[i] in nodo.transiciones[j]: #Si el item de la lista de símbolos está en la transiciones del nodo
				aux.append(simbolos[i]) #Agregamos al final de la lista el símbolo
	return aux #Retornamos la lista auxiliar

#Función que devuelve la posicion de un elemento en un arreglo de nodos
def posicion(nodos,elemento):
	i = 0 #Reinicio del contador
	posicion = -1 #Variable auxiliar
	for i in range(0,len(nodos)): #Ciclo del número de nodos
		if nodos[i].numero == int(elemento): #Si el numero del nodo es igual al elemento buscado
			posicion = i #Guardamos la posición del numero en la lista
	return posicion #Retornamos la variable auxiliar