import random
import math


def funcion_F(x, n, p, F):
    sumatoria = 0

    for i in range(1, n+1):
        sumatoria += p[i] * F[i](x)


if __name__ == "__main__":
    pass
