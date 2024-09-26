# Programa en python para generar cuadrados magicos de 3x3

# Funcion para generar los cuadros

def CrearCuadro(n):

	# Funcion para crear arreglo inicializado con 0
	magicSquare = [[0 for x in range(n)]
				for y in range(n)]

	# Inicializar en la poscicion 1
	i = n // 2
	j = n - 1

	#Funcion para rellenar con valores el arreglo
	num = 1
	while num <= (n * n):
		if i == -1 and j == n: # 3ra condicional
			j = n - 2
			i = 0
		else:

			# Funcion que rellena el siguiente numero
			if j == n:
				j = 0

			# Funcion que rellena el siguiente numero
			if i < 0:
				i = n - 1

		if magicSquare[int(i)][int(j)]: # 2da condicional para rellenar
			j = j - 2
			i = i + 1
			continue
		else:
			magicSquare[int(i)][int(j)] = num
			num = num + 1

		j = j + 1
		i = i - 1 # 1ra condicional
	# Printing magic square
	print("\nCuadrado magico de n = 3 *", n)
	print("\nSuma de cada columna, fila y diagonales",
		n * (n * n + 1) // 2, "\n")

	for i in range(0, n):
		for j in range(0, n):
			print('%2d ' % (magicSquare[i][j]),
				end='')

			# Imprime la matriz de salida
			if j == n - 1:
				print()

n = 3
CrearCuadro(n)

