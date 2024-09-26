import random
import math

def generar_laberinto():
    laberinto = [[0 for _ in range(10)] for _ in range(10)]
    obstaculos = random.sample(range(100), 20)
    for obs in obstaculos:
        i, j = divmod(obs, 10)
        laberinto[i][j] = 1
    return laberinto

def generar_posicion_aleatoria():
    return (random.randint(0, 9), random.randint(0, 9))

def distancia_euclidiana(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def resolver_laberinto(laberinto, inicio, meta):
    por_evaluar = [(inicio, 0)]
    visitados = []
    padres = {inicio: None}
    costos = {inicio: 0}
    
    while por_evaluar:
        actual, costo_actual = sorted(por_evaluar, key=lambda x: x[1] + distancia_euclidiana(x[0], meta))[0]
        if actual == meta:
            ruta_optima = [meta]
            while padres[ruta_optima[0]]:
                ruta_optima.insert(0, padres[ruta_optima[0]])
            return ruta_optima
        
        por_evaluar.remove((actual, costo_actual))
        visitados.append(actual)
        
        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            vecino = (actual[0] + i, actual[1] + j)
            nuevo_costo = costos[actual] + laberinto[vecino[0]][vecino[1]]
            if vecino in visitados:
                continue
            if laberinto[vecino[0]][vecino[1]] == 1:
                continue
            if vecino not in [n[0] for n in por_evaluar]:
                por_evaluar.append((vecino, nuevo_costo))
            elif nuevo_costo >= costos[vecino]:
                continue
            padres[vecino] = actual
            costos[vecino] = nuevo_costo
    
    return None

def visualizar_laberinto(laberinto, inicio, meta, ruta_optima):
    for i in range(10):
        for j in range(10):
            if laberinto[i][j] == 0:
                print(".", end="")
            else:
                print("#", end="")
            if (i, j) == inicio:
                print("I", end="")
            elif (i, j) == meta:
                print("M", end="")
            elif (i, j) in ruta_optima:
                print("*", end="")
            else:
                print(".", end="")
        print("")

# Generamos un laberinto aleatorio
laberinto = generar_laberinto()

# Generamos posiciones aleatorias para el inicio y la meta
inicio = generar_posicion_aleatoria()
meta = generar_posicion_aleatoria()

# Resolvemos el laberinto
ruta_optima = resolver_laberinto(laberinto, inicio, meta)

# Visualizamos el laberinto y la ruta óptima
visualizar_laberinto(laberinto,inicio,meta,ruta_optima)