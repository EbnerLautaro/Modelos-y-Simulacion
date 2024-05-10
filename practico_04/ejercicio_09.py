import random
import math
import time


def transformada_inversa(p):
    i = 1
    p_i = p
    acumulada = p_i
    u = random.random()
    while u >= acumulada:
        i += 1
        p_i *= (1-p)
        acumulada += p_i
    return i


def ensayos(p):
    cont = 1
    u = random.random()
    while u >= p:
        cont += 1
        u = random.random()
    return cont


if __name__ == "__main__":
    # Implemente dos métodos para simular una variable geométrica Geom(p):
    #   a) Usando transformada inversa y aplicando la fórmula recursiva para P(X = i).
    #   b) Simulando ensayos con probabilidad de éxito p hasta obtener un éxito.
    #
    # Compare la eficiencia de estos algoritmos para p = 0,8 y para p = 0,2.
    # Para cada caso, realice 10000 simulaciones y calcular el promedio de los valores obtenidos.
    # Comparar estos valores con el valor esperado de la distribución correspondiente. Si están alejados, revisar el código.

    n_sim = 100_000
    for p in [0.8, 0.2]:
        print("".center(100, "="))
        for func in [transformada_inversa, ensayos]:
            print(f"- {func.__name__}({p})")
            start = time.time()
            prom = 0
            for _ in range(n_sim):
                prom += func(p=p)
            print(f"\tvalor esperado: {prom/n_sim}")
            print(f"\ttime: {time.time() - start}")
