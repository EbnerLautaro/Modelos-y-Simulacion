import math
import numpy as np


def F_x(x, lambd):
    return 1 - math.exp(-(x*lambd))


def estadistico_d(F, m):
    muestra = m
    muestra.sort()

    d = 0
    n = len(muestra)
    for i in range(1, len(muestra)+1):

        x = muestra[i-1]
        d = max(d, ((i)/n)-F(x), F(x)-((i-1)/n))

    return d


def estimacion_p_valor(n, d, n_sim):

    def F_x(x):
        return x

    p_valor = 0
    for _ in range(n_sim):
        uniformes = np.random.uniform(0, 1, n)
        uniformes.sort()
        d_j = estadistico_d(F_x, uniformes)
        if d_j > d:
            p_valor += 1

    return p_valor/n_sim


if __name__ == "__main__":

    def f(x):
        return F_x(x=x, lambd=1/50)

    muestra = [86.0, 133.0, 75.0, 22.0, 11.0, 144.0,
               78.0, 122.0, 8.0, 146.0, 33.0, 41.0, 99.0]

    muestra.sort()

    d = estadistico_d(F=f, m=muestra)
    print(f"estadistico d       {d}")

    p_valor = estimacion_p_valor(n=len(muestra), d=d,  n_sim=10_000)
    print(f"simulacion p-valor  {p_valor}")
