import random
import math
import numpy as np


def media_muestral(m):
    return sum(m)/len(m)


def estimador_d(muestra, F):
    m = muestra
    m.sort()
    n = len(muestra)
    d = 0
    for i in range(1, n+1):
        elem = m[i-1]
        d = max(d, (i/n)-F(elem), F(elem) - ((i-1)/n))
    return d


def acumulada_exponencial(x, lambd):
    return 1 - math.exp(-(x*lambd))


def sim_p_valor_uniformes(d, n_sample, n_sim):
    def acumulada_uniforme(x):
        assert 0 <= x <= 1
        return x

    p_valor = 0

    for _ in range(n_sim):

        uniformes = np.random.uniform(0, 1, size=n_sample)
        uniformes.sort()

        d_j = estimador_d(uniformes, acumulada_uniforme)

        if d_j >= d:
            p_valor += 1

    return p_valor/n_sim


def sim_p_valor_exponenciales(d, exp_param,  n_sample, n_sim):
    p_valor = 0

    for _ in range(n_sim):
        exponenciales = np.random.exponential(scale=exp_param, size=n_sample)
        exponenciales.sort()
        d_j = estimador_d(
            muestra=exponenciales,
            F=lambda x: acumulada_exponencial(
                x=x,
                lambd=1 / media_muestral(exponenciales)
            ),
        )

        if d_j >= d:
            p_valor += 1

    return p_valor/n_sim


if __name__ == "__main__":
    muestra = [1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3,
               10.7, 8.4, 4.9, 7.9, 12, 16.2, 6.8, 14.7]

    est_param = 1/media_muestral(muestra)

    # def F_exp(x):
    #     return acumulada_exponencial(x, est_param)

    # calculamos el estimador d
    est_d = estimador_d(muestra, lambda x: acumulada_exponencial(x, est_param))
    print(f"estimador d                         {est_d}")

    p_valor = sim_p_valor_uniformes(
        d=est_d,
        n_sample=len(muestra),
        n_sim=10_000
    )
    print(f"p-valor simulado con uniformes      {p_valor}")

    p_valor = sim_p_valor_exponenciales(
        exp_param=est_param,
        d=est_d,
        n_sample=len(muestra),
        n_sim=10_000
    )
    print(f"p-valor simulado con exponenciales  {p_valor}")
