import math
import random


def cociente(lamda, k):
    sumatoria = 0
    j_fact = 1
    for j in range(0, k+1):
        if j == 0:
            sumatoria += math.exp(-lamda)
            continue

        j_fact *= j
        sumatoria += math.exp(-lamda) * ((lamda**j) / j_fact)

    return sumatoria


def transformada_inversa(lamda, k):
    q = cociente(lamda=lamda, k=k)
    i = 0
    p_i = math.exp(-lamda)/q
    acumulador = p_i
    u = random.random()
    while u >= acumulador:
        i += 1
        p_i *= (lamda/i)
        acumulador += p_i
    return i


def aceptacion_rechazo():
    pass


if __name__ == "__main__":
    n_sim = 10_000
    k = 10
    resultados = [0 for _ in range(k)]
    for _ in range(n_sim):
        sim = transformada_inversa(k=k, lamda=0.7)
        resultados[sim] += 1
    print(resultados)
    print([elem/n_sim for elem in resultados])
