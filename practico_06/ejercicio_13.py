import random
import math
from scipy.stats import chi2
import numpy as np


def estadistico_d(muestra, F):
    m = muestra
    muestra.sort()
    d = 0
    n = len(m)
    for i in range(1, n+1):
        elem = m[i-1]
        d = max(d, (i/n)-F(elem), F(elem)-((i-1)/n))
    return d


def acumulada_exponencial(x):
    return 1 - math.exp(-x)


def p_valor_smirnov(d, N_sample,  n_sim):

    def F_x(x):
        assert 0 <= x <= 1
        return x

    p_valor = 0
    for _ in range(n_sim):

        uniformes = np.random.uniform(0, 1, N_sample)
        uniformes.sort()
        d_j = estadistico_d(uniformes, F_x)

        if d_j >= d:
            p_valor += 1

    return p_valor/n_sim


def p_valor_smirnov_exp(d, N_sample,  n_sim):

    def F_x(x):
        assert 0 <= x <= 1
        return x

    p_valor = 0
    for _ in range(n_sim):

        uniformes = np.random.exponential(1, N_sample)
        uniformes.sort()
        d_j = estadistico_d(uniformes, lambda x: 1-math.exp(-x))

        if d_j >= d:
            p_valor += 1

    return p_valor/n_sim


if __name__ == "__main__":
    # Generar los valores correspondientes a 30 variables aleatorias exponenciales
    # independientes, cada una con media 1. Luego, en base al estadístico de prueba
    # de Kolmogorov-Smirnov, aproxime el p−valor de la prueba de que los datos realmente
    # provienen de una distribución exponencial con media 1.

    # generamos la muestra
    N_sample = 100
    muestra = np.random.exponential(1, size=N_sample)

    # calculamos el estadistico d
    d_stat = estadistico_d(muestra, acumulada_exponencial)
    print(f"estadistico d           {d_stat}")

    # estimamos el p-valor
    p_valor = p_valor_smirnov(d=d_stat, N_sample=N_sample, n_sim=10_000)

    print(f"estiamcion p-valor      {p_valor}")
    p_valor = p_valor_smirnov_exp(d=d_stat, N_sample=N_sample, n_sim=10_000)

    print(f"estiamcion p-valor exp  {p_valor}")
