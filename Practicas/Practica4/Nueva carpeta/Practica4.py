

if __name__ == "__main__":
	print("-----Analisis Sintactico de Descenso Recursivo-----")
	Cadena = "a+a"
	Terminales = ('a', '+')
	NoTerminales = ('E', 'Z', 'T')
	Inicial = 'E'
	Posicion = 0

	#Producciones:
	#	E->TZ
    #   Z->+TZ | e | R  
    #   T->a
    #   R->-TZ | e

def A():
	#Elegir una produccion A, A -> X1X2...Xk, k=2
	for i in range (1, 2):
		if (true):
			#Llamar al procedimiento Xi();
		elif (true):
			#Xi es igual simbolo de entrada actual a
			#Avanzar la entrada hasta el sigueinte simbolo
		else:
			#Ha ocurrido un error
			