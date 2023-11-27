muro = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

class Laberinto:

    def construir_laberinto(muro):
        filas = 5
        columnas = 5
        laberinto = [[' ' for _ in range(columnas)] for _ in range(filas)]

        laberinto[filas-1][columnas-1] = "S" 
        laberinto[filas-5][columnas-5] = "E"

        for coordenada in muro:
            fila, columna = coordenada
            laberinto[fila][columna] = 'X'

        return laberinto


    laberinto = construir_laberinto(muro)

    for fila in laberinto:
        print('  '.join(fila))



