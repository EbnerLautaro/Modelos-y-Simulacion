import random
import math
import numpy as np


def estadistico_d(F, m):
    muestra = m
    muestra.sort()

    d = 0
    n = len(muestra)
    for i in range(1, len(muestra)+1):

        x = muestra[i-1]
        d = max(d, ((i)/n)-F(x), F(x)-((i-1)/n))

    return d


def F_x(x):
    assert 0 <= x <= 1
    return x


def estimacion_p_valor(n, d, n_sim):

    p_valor = 0
    for _ in range(n_sim):
        uniformes = np.random.uniform(0, 1, n)
        uniformes.sort()
        d_j = estadistico_d(F_x, uniformes)
        if d_j > d:
            p_valor += 1

    return p_valor/n_sim


if __name__ == "__main__":
    muestras = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
    # muestras = [0.06, 0.12, 0.18, 0.27, 0.33, 0.36, 0.72, 0.74, 0.77, 0.83]
    print(f"muestras            {muestras}")
    d_calc = estadistico_d(F=F_x, m=muestras)
    print(f"estadistico d       {d_calc}")
    p_valor = estimacion_p_valor(n=len(muestras), d=d_calc, n_sim=10_000)
    print(f"estimacion p_valor  {p_valor}")
