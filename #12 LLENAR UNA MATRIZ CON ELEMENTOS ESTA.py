#12 LLENAR UNA MATRIZ CON ELEMENTOS ESTATICOS LONGITUD FILA = 4 Y COLUMNA = 5:
def llenar_matriz():
     matriz=[
          [1,2,3,4,5],
          [6,7,8,9,10],
          [11,12,13,14,15],
          [16,17,18,19,20]
     ]
     return matriz

#13 LLENAR UNA MATRIZ CON N CANTIDAD DE FILAS Y M CANTIDAD DE COLUMNAS:
def llenar_matriz(n,m):
     x=1
     matriz=[[1000]*m for _ in range(n)]
     for f in range(n):
          for c in range(m):
               matriz[f][c]=x
               x=x+1
     return matriz

cantidad_fila=3
cantidad_columna=5
matriz=llenar_matriz(cantidad_fila,cantidad_columna)
print(matriz)

#TAREA 01 LLENAR MATRIZ DE 4 FILAS Y 5 COLUMNAS CON NUMEROS PARES:
def llenar_matriz_pares():
     fila=4
     columna=5
     numero=2
     matriz=[[] for _ in range(fila)]
     for fila in matriz:
          for _ in range(columna):
               fila.append(numero)
               numero += 2
     return matriz
matriz=llenar_matriz_pares()
print(matriz)

#TAREA 02 LLENAR MATRIZ DE 4 FILAS Y 5 COLUMNAS [ [0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7] ]:
