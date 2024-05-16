import random
import math


def transformada_inversa():
    u = random.random()
    if u <= 1/3:
        return math.log(3*u)
    else:
        return (-1/2)*math.log((6-6*u)/4)


if __name__ == "__main__":
    n_sim = 10_000
    suma = 0
    cont = 0
    for _ in range(n_sim):
        sim = transformada_inversa()
        suma += sim
        if sim <= 1:
            cont += 1

    print(f"esperanza:  \t{suma/n_sim}")
    print(f"P(X<=1):    \t{cont/n_sim}")
