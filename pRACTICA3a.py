import random
import pygame
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
                costos[vecino] = nuevo_costo  # Se agrega esta línea
            elif nuevo_costo >= costos[vecino]:
                continue
            padres[vecino] = actual
            costos[vecino] = nuevo_costo

    return None


def dibujar_laberinto(canvas, laberinto, inicio, meta, ruta_optima):
    tam_celda = 50
    canvas.fill((255, 255, 255))
    for i in range(10):
        for j in range(10):
            celda_rect = pygame.Rect(j * tam_celda, i * tam_celda, tam_celda, tam_celda)
            if laberinto[i][j] == 0:
                pygame.draw.rect(canvas, (255, 255, 255), celda_rect)
            else:
                pygame.draw.rect(canvas, (0, 0, 0), celda_rect)
            if (i, j) == inicio:
                pygame.draw.circle(canvas, (255, 0, 0), (j * tam_celda + tam_celda//2, i * tam_celda + tam_celda//2), tam_celda//3)
            elif (i, j) == meta:
                pygame.draw.circle(canvas, (0, 255, 0), (j * tam_celda + tam_celda//2, i * tam_celda + tam_celda//2), tam_celda//3)
            elif ruta_optima and (i, j) in ruta_optima:
                pygame.draw.rect(canvas, (0, 0, 255), celda_rect)
def main():
    laberinto = generar_laberinto()
    inicio = generar_posicion_aleatoria()
    meta = generar_posicion_aleatoria()
    while inicio == meta or laberinto[inicio[0]][inicio[1]] == 1 or laberinto[meta[0]][meta[1]] == 1:
        inicio = generar_posicion_aleatoria()
        meta = generar_posicion_aleatoria()
    ruta_optima = resolver_laberinto(laberinto, inicio, meta)
    pygame.init()
    canvas = pygame.display.set_mode((500, 500))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        dibujar_laberinto(canvas, laberinto, inicio, meta, ruta_optima)
        pygame.display.update()

if __name__ == '__main__':
    main()
