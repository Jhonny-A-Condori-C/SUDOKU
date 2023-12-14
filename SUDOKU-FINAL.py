import os
import random

cantidad_filas = 0 #cantidad de filas del tablero de sudoku
cantidad_columnas = 0 #cantidad de columnas del tablero de sudoku
opcion_insertar = 1 # opcion 1 insertar numero en el tablero sudoku
opcion_resolver_sudoku = 2
opcion_salir = 3 # opcion 3 salir del menu
minimo_valor = 1 # numero minimo que se puede insertar en el tablero sudoku
maximo_valor = 0 # numero maximo que se puede insertar en el tablero sudoku


'''	
meetodo que explica las reglas del juego dependiendo del nivel
'''
def reglas_sudoku ():
	if nivel == 1 :
		print ("usted eligio el nivel facil")
		print ("las reglas de este juego consisten en: ")
		print ("insertar un numero entre el 1 y el 6")
		print ("el numero ingresado no se debe repetir ni en fila ni en columnas ni en el cuadrante")
	elif nivel == 2 :
		print ("usted eligio el nivel medio ")
		print ("las reglas de este juego consisten en: ")
		print ("insertar un numero entre el 1 y el 6")
		print ("el numero ingresado no se debe repetir ni en fila ni en columnas ni en el cuadrante")	
	elif nivel == 3:
		print ("usted eligio el nivel dificil ")
		print ("las reglas de este juego consisten en: ")
		print ("insertar un numero entre el 1 y el 9")
		print ("el numero ingresado no se debe repetir ni en fila ni en columnas ni en el cuadrante")


''''
creamos una matriz para ambos niveles
'''

facil_1 = [
    [1, 0, 3, 0],
	[0, 0, 2, 0],
	[3, 0, 1, 0],
	[0, 1, 0, 3]
]

facil_2 = [
    [1, 0, 0, 4],
	[3, 0, 1, 0],
	[0, 3, 2, 0],
	[0, 1, 0, 0]
]

facil_3 = [
    [2, 1, 0, 3],
    [0, 4, 0, 0],
    [0, 3, 0, 2],
    [1, 0, 0, 4]
]

medio_1 = [
    [1, 0, 0, 0, 4, 0],
    [0, 0, 0, 5, 0, 0],
    [0, 5, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 3, 0],
    [0, 0, 3, 0, 0, 0]
]

medio_2 = [
    [0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

medio_3 = [
    [0, 0, 0, 0, 0, 0],
    [0, 3, 0, 4, 0, 0],
    [5, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 2, 0],
    [4, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]


dificil_1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

dificil_2 = [
    [0, 9, 0, 0, 4, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 6, 0, 1, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 7],
    [4, 0, 0, 0, 5, 0, 8, 0, 0],
    [0, 0, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 0, 3, 0],
    [0, 0, 0, 8, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 0, 9]
]


dificil_3 = [
    [0, 0, 5, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 7, 0, 0, 1, 0, 5, 0, 0],
    [4, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 1, 0, 5, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 9, 7, 0, 0, 0, 0, 0]
    ]




'''
metodo que verifica si el valor ya se encuentra en la fila indicada del tablero, en caso de existir retorna true, caso contrario retorna false
'''
def validar_fila(f, valor, tablero):
	for c in range(cantidad_columnas):
		if tablero[f][c] == valor:
			return False
	return True 

'''
metodo que verifica si el valor ya se encuentra en la columna indicada del tablero, en caso de existir retorna true, caso contrario retorna false
'''
def validar_columna(c, valor, tablero):
	for f in range(cantidad_filas):
		if tablero[f][c] == valor:
			return False
	return True
'''
metodo que verifica si el valor ya se encuentra en el cuadrante indicado por su fila (f) y columna(c) del tablero , en caso de existir retorna true, caso contrario retorna false
'''
def validar_cuadrante_2x2(f, c, valor, tablero):
    inicio_fila = (f//2)*2
    inicio_columna = (c//2)*2
    for i in range(inicio_fila, inicio_fila + 2):
        for j in range(inicio_columna, inicio_columna + 2):
            if tablero[i][j] == valor:
                return False
    return True

def validar_cuadrante_2x3(f, c, valor, tablero):
    inicio_fila = (f // 2) * 2
    inicio_columna = (c // 3) * 3
    for i in range(inicio_fila, inicio_fila + 2):
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == valor:
                return False
    return True

def validar_cuadrante_3x3(f, c, valor, tablero):
    inicio_fila = (f // 3) * 3
    inicio_columna = (c // 3) * 3
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == valor:
                return False
    return True
'''
metodo que verifica si la fila(f) y columna(c) se encuentran dentro del rango permitido del ta lero sudoku, en caso de estar dentro del rango retorna true, caso contrario retorna false
'''
def validar_posicion(f, c):
	return True
'''
metodo que verifica si el valor se encuentra del rango permitido de numeros que acpeta el tablero sudoku, estar, en caso de estar demtro del rango retorna true, caso contrario retorna false
'''
def validar_valor(valor):
	return valor >= minimo_valor and valor <= maximo_valor
'''
metodo que verifica que se cumplam todas las condiciones para insertar un valor en el tablero sudoku en la fila (f) y columna(c) indicada, en caso de cumplirla retorna true, caso contrario retorna false
'''
def validar(f, c, valor, tablero):
    if nivel == 1:
        return (validar_posicion(f, c)
                and validar_valor(valor)
                and validar_fila(f, valor, tablero)
                and validar_columna(c, valor, tablero)
                and validar_cuadrante_2x2(f, c, valor, tablero))
    elif nivel == 2:
        return (validar_posicion(f, c)
                and validar_valor(valor)
                and validar_fila(f, valor, tablero)
                and validar_columna(c, valor, tablero)
                and validar_cuadrante_2x3(f, c, valor, tablero))
    elif nivel == 3:
        return (validar_posicion(f, c)
                and validar_valor(valor)
                and validar_fila(f, valor, tablero)
                and validar_columna(c, valor, tablero)
                and validar_cuadrante_3x3(f, c, valor, tablero))

	            
'''
metodo que inserta un valor en el tablero sudoku en la fila (f) y columna(c) indicada, una vez insertada retorna el tablero modificado
'''
def insertar_valor(f, c, valor, tablero):
	tablero[f][c] = valor
	return tablero

'''
metodo que no deja cambiar los valores ya predefinidos en la tabla del sudoku
'''
def insertar_valor(f, c, valor, tablero):
    if tablero[f][c] != 0:
        print("No puedes cambiar un valor predefinido en el tablero")
    else:
        tablero[f][c] = valor
    return tablero


'''
metodo que imprime el tablero de sudoku
'''
def mostrar_tablero(tablero):
	for m in tablero:
		print(m)
'''
metodo que imprime el nivel del juego
'''
def selccion_niveles ():
	print ("seleccione el nivel en el que desea jugar")
	print ("1) Nivel facil ")
	print ("2) Nivel medio")
	print ("3) Nivel dificil")
	
'''
metodo que te muestra el sudoku ya resuelto dependiendo del nivel 
'''
def sudoku_resuelto ():
	if nivel == 1:
		if genera_tab_facil == 1:
			tab_resuelto = [
				[1, 2, 3, 4],
				[4, 3, 2, 1],
				[3, 4, 1, 2],
				[2, 1, 4, 3]
            ]
			for m in tab_resuelto:
				print (m)
		elif genera_tab_facil == 2:
			tab_resuelto = [
				[1, 2, 3, 4],
				[3, 4, 1, 2],
				[4, 3, 2, 1],
				[2, 1, 4, 3]
            ]	
			for m in tab_resuelto:
				print(m)
		else:
			tab_resuelto = [
				[2, 1, 4, 3],
                [3, 4, 2, 1],
                [4, 3, 1, 2],
                [1, 2, 3, 4]
            ] 	
			for m in tab_resuelto:
				print (m)
	elif nivel ==2:
		if genera_tab_medio == 1:
			tab_resuelto = 	[
				[1, 6, 3, 2, 4, 5],
                [6, 4, 2, 5, 1, 3],
                [2, 5, 4, 3, 3, 6],
                [3, 1, 5, 4, 6, 2],     
                [5, 2, 1, 2, 3, 4],
                [4, 3, 6, 1, 5, 1]
			]
			for m in tab_resuelto:
				print (m)
		if genera_tab_medio == 2:
			tab_resuelto = [
				[1, 4, 3, 5, 6, 2],
                [2, 3, 5, 4, 1, 6],
                [5, 2, 4, 6, 3, 1],
                [4, 6, 1, 3, 2, 5],
                [6, 1, 2, 3, 5, 4],
                [3, 5, 6, 2, 4, 1]
			]
			for m in tab_resuelto:
				print(m)
		else:
			tab_resuelto = [ 

			]
			for m in tab_resuelto:
				print(m)
	else:
		if genera_tab_dificil == 1:
			tab_resuelto = [
				[5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]
				]
			for m in tab_resuelto:
				print(m)
		elif genera_tab_dificil ==2:	
			tab_resuelto = [
				[1, 9, 8, 7, 4, 6, 3, 5, 2],
                [2, 6, 7, 3, 5, 8, 4, 1, 9],
                [3, 4, 5, 6, 9, 1, 2, 7, 8],
                [6, 7, 4, 1, 2, 3, 5, 9, 7],
                [4, 1, 2, 9, 8, 5, 8, 2, 6],
                [8, 5, 9, 4, 6, 7, 1, 9, 3],
                [9, 2, 6, 5, 7, 4, 6, 3, 5],
                [5, 3, 1, 8, 3, 9, 7, 4, 4],
                [7, 8, 3, 2, 1, 6, 9, 8, 1]
			]
			for m in tab_resuelto:
				print(m)	
		else:
			tab_resuelto = [
				[3, 4, 5, 6, 2, 8, 7, 1, 9],
                [8, 6, 1, 9, 7, 3, 4, 2, 5],
                [9, 7, 2, 4, 1, 5, 8, 6, 3],
                [4, 9, 3, 2, 8, 7, 6, 5, 1],
                [6, 1, 7, 5, 4, 9, 3, 8, 2],
                [5, 2, 8, 3, 6, 1, 9, 4, 7],
                [1, 8, 6, 8, 3, 4, 5, 7, 9],
                [7, 3, 4, 1, 9, 6, 2, 5, 8],
                [2, 5, 9, 7, 5, 2, 1, 3, 4]
			]
			for m in tab_resuelto:
				print(m)
'''
metodo que imprime el menu del juego 
'''	
def menu( ):
	print("-------------------😎Menu😎------------------")
	print("Debe seleccionar una opcion escribiendo el numero")
	print("1) Insertar valor")
	print("2) ver sudoku resuelto")
	print("3) Salir")
'''
metodo que ingresa un mensaje al ganador 
'''

if __name__ == "__main__":
	resp = 0
	nivel = 0
	
	while nivel == 0 or nivel > 3:
		selccion_niveles ()
		nivel = int (input("escriba el numero de la opcion : "))

	if nivel == 1:
		genera_tab_facil = random.randint(1,3)
		if genera_tab_facil == 1:
			facil = facil_1
		elif genera_tab_facil ==2:
			facil = facil_2
		else :
			facil = facil_3
			
		tablero = facil
		cantidad_columnas = 4
		cantidad_filas = 4
		maximo_valor = 4		
	elif nivel == 2:
		genera_tab_medio = random.randint(1,3)
		if genera_tab_medio ==1:
			medio = medio_1
		elif genera_tab_medio == 2:
			medio = medio_2
		else:
			medio = medio_3
		tablero = medio	
		cantidad_columnas = 6
		cantidad_filas = 6
		maximo_valor = 6
	elif nivel == 3 :
		genera_tab_dificil = random.randint(1,3)
		if genera_tab_dificil ==1:
			dificil = dificil_1
		elif genera_tab_dificil == 2:
			dificil = dificil_2
		elif genera_tab_dificil == 3:
			dificil = dificil_3
		tablero = dificil	
		cantidad_columnas = 9
		cantidad_filas = 9
		maximo_valor = 9
		
	def nivel_superado(tablero):
		for fila in tablero:
			for valor in fila:
				if valor == 0:
					return False
		return True
	

	while (resp != opcion_salir ):
		if nivel_superado(tablero):
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Nivel Superado, ¡¡Has completado el SUDOKU!!")
			break
		os.system('cls' if os.name == 'nt' else 'clear')
		print("                  ✨ SUDOKU ✨              ")
		reglas_sudoku()
		mostrar_tablero(tablero)
		menu( )	
		resp = (input("Escriba el numero de la opcion :"))
		if resp.isdigit():
			resp = int(resp)
			if resp == opcion_salir:
				break
			elif resp == opcion_resolver_sudoku:
				os.system('cls' if os.name == 'nt' else 'clear')
				print("                  ✨ Sudoku Resuelto ✨              ")
				sudoku_resuelto()
				break
			else:
				os.system('cls' if os.name == 'nt' else 'clear')
				print("                  ✨ SUDOKU ✨              ")
				reglas_sudoku()
				mostrar_tablero(tablero)
				menu()
				v = input("Introduzca el valor a introducir en el tablero:")
				if v.isdigit():
					v = int(v)
				else:
					print("Por favor, ingrese solo números.")
					continue  # Vuelve a hacer la pregunta si la entrada es invalida
				f = input("Introduzca la fila del tablero: ")
				if f.isdigit():
					f = int(f) - 1
				else:
					print("Por favor, ingrese solo números.")
					continue  # Vuelve a hacer la pregunta si la entrada es invalida
				c = input("Introduzca la columna del tablero: ")
				if c.isdigit():
					c = int(c) - 1
				else:
					print("Por favor, ingrese solo números.")
					continue  # Vuelve a hacer la pregunta si la entrada es invalida
				es_valido = validar(f, c, v, tablero)
				if es_valido:
					tablero = insertar_valor(f, c, v, tablero)
				else:
					print("Error al introducir el número, intente nuevamente.")
					continue  # Vuelve a hacer la pregunta si la entrada es invalida
					

		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Error")
			input("Presione Enter para continuar")
	else:
		print ("error")
		input ("presione enter para cotinuar")