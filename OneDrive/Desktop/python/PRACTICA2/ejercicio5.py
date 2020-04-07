

#Defino la lista de nummeros
lista = []
ordenada = []

#Comienza el proceso del juego
#Pido que elija un numero
numero = int(input('ELIGA UN NUMERO:\n 1: INGRESAR NUMERO\n 2: ORDENAR NUMERO\n 3: CALCULAR MAXIMO\n 4: CALCULAR MINIMO\n 5: CALCULAR PROMEDIO\n 0: PARA TERMINAR\n'))


#inicializo variables 
cantidad = 0;


def ingresar_numero (lista,cantidad):
	num = int(input('INGRESE UN NUMERO:\n'))
	lista.append(num)
	cantidad = cantidad + 1
	return cantidad
	
def ordenar_numero(lista):
	lista.sort()

def calcular_max(lista):
	print ("\nEL NUMERO MAXIMO ES: \n" , max (lista))
	
def calcular_min(lista):
	print ("\nEL NUMERO MINIMO ES: \n" , min (lista))
	
def calcular_promedio(lista):
	suma = sum(lista)
	num = int (len(lista))
	print ("\nEL PROMEDIO ES: \n" , suma / num)

def termina (lista):
	if len(lista) == 0:
		print ('LA LISTA ESTA VACIA')
				
#comienza la interacción con el jugador

while numero != 0:

	if numero == 1:
		cantidad = ingresar_numero(lista,cantidad)
	else:
		if numero == 2:
			ordenar_numero(lista)
		else:
			if numero == 3:
				calcular_max(lista)
			else:
				if numero == 4:
					calcular_min(lista)
				else:
					if numero == 5:
						calcular_promedio(lista)					
	numero = int(input('\nELIGA UN NUMERO:\n 1: INGRESAR NUMERO\n 2: ORDENAR NUMERO\n 3: CALCULAR MAXIMO\n 4: CALCULAR MINIMO\n 5: CALCULAR PROMEDIO\n 0: PARA TERMINAR\n'))
termina(lista)
				

