import math
from scipy.stats import chi2
import numpy as np


def media_muestral(m):
    return sum(m) / len(m)


def estimador_T(ocurrencias, N, p_list):

    T = 0
    for Ni, Pi in zip(ocurrencias, p_list):
        T += pow(Ni-(N*Pi), 2) / (N*Pi)

    return T


def p_binomial(x, n, p):
    return math.comb(n, x) * pow(p, x) * pow(1-p, n-x)


def sim_p_valor(t_sample, n_bin, p_bin, N_sample, n_sim):

    p_valor = 0
    n = 0
    while n <= n_sim:

        values = np.random.binomial(n=n_bin, p=p_bin, size=N_sample)
        ocurrencias = [0 for _ in range(n_bin+1)]
        for i in values:
            ocurrencias[i] += 1

        pi = sum(values)/len(values) / 8
        probs = [p_binomial(i, n_bin, pi) for i in range(n_bin+1)]
        Ti = estimador_T(ocurrencias, N_sample, probs)
        if Ti >= t_sample:
            p_valor += 1

        n += 1

    return p_valor / n_sim


if __name__ == "__main__":

    # Calcular una aproximación del p−valor de la prueba de que los siguientes datos corresponden
    # a una distribución binomial con parámetros (n = 8, p), donde p no se conoce

    muestra = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
    muestra.sort()
    print(muestra)
    n = 8

    # aproximamos el parametro p, como E(X)=np, tenemos que p=E(X)/n
    p_aprox = media_muestral(m=muestra)/n

    # luego, utilizamos este parametro para el test de Pearson

    def p_x(x):
        return p_binomial(x, 8, p_aprox)

    ocurrencias = [0 for _ in range(n+1)]

    for elem in muestra:
        ocurrencias[elem] += 1

    t = estimador_T(ocurrencias=ocurrencias, N=sum(
        ocurrencias), p_list=[p_x(i) for i in range(n+1)])

    df = len(ocurrencias) - 1 - 1

    p_valor = chi2.sf(x=t, df=df)

    p_valor_sim = sim_p_valor(
        t_sample=t, n_bin=8, p_bin=p_aprox, N_sample=len(muestra), n_sim=10_000)

    print(f"aproximacion p                      {p_aprox}")
    print(f"estimador T                         {t}")
    print(f"aproximacion p-valor con chi2       {p_valor:.5f}")
    print(f"simulacion p-valor                  {p_valor_sim}")
