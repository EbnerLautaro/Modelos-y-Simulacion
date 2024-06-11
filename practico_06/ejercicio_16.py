import random
import math
import numpy as np
from scipy import stats


def estimador_d(muestra, F):
    m = muestra
    m.sort()
    n = len(m)
    d = 0
    for i in range(1, n+1):
        x = m[i-1]
        d = max(d, (i/n)-F(x), F(x)-((i-1)/n))
    return d


def acumulada_normal_no_estandar(x, loc, scale):
    return stats.norm.cdf(x, loc=loc, scale=scale)


def acumulada_uniforme(x):
    assert 0 <= x <= 1
    return x


def p_valor_uniforme(d, n_sample, n_sim):
    p_valor = 0
    for _ in range(n_sim):
        uniformes = np.random.uniform(0, 1, size=n_sample)
        uniformes.sort()

        dj = estimador_d(muestra=uniformes, F=acumulada_uniforme)

        if dj >= d:
            p_valor += 1

    return p_valor/n_sim


def media_varianza(muestra):
    n = len(muestra)

    mu = 0
    mu_sq = 0

    for x in muestra:
        mu += x
        mu_sq += pow(x, 2)

    med = mu/n
    var = mu_sq/n - pow(med, 2)

    return med, var


def simular_p_valor_utilizando_normales_no_estandares(mu, sigma, d, n_sample, n_sim):
    p_valor = 0
    for _ in range(n_sim):
        normales = np.random.normal(loc=mu, scale=sigma, size=n_sample)
        med, var = media_varianza(normales)
        dj = estimador_d(
            normales,
            lambda x: stats.norm.cdf(x, loc=med, scale=math.sqrt(var))
        )
        if dj >= d:
            p_valor += 1
    return p_valor / n_sim


if __name__ == "__main__":

    muestra = [91.9, 97.8, 111.4, 122.3, 105.4,
               95.0, 103.8, 99.6, 96.6, 119.3, 104.8, 101.7]

    med, var = media_varianza(muestra)
    print(med, var, math.sqrt(var))
    d_stat = estimador_d(
        muestra, lambda x: acumulada_normal_no_estandar(x, med, math.sqrt(var)))
    print(f"estimador d                 {d_stat}")

    p_valor = p_valor_uniforme(
        d=d_stat,
        n_sample=len(muestra),
        n_sim=10_000
    )
    print(f"p-valor con uniformes       {p_valor}")

    p_valor = simular_p_valor_utilizando_normales_no_estandares(
        mu=med,
        sigma=math.sqrt(var),
        d=d_stat,
        n_sample=len(muestra),
        n_sim=10_000
    )
    print(f"p-valor con normales        {p_valor}")
