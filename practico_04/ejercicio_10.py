import random


def transformada_inversa():
    i = 1
    t1 = (1/2)**2
    t2 = (1/2)/3
    acumulada = t1 + t2
    u = random.random()
    while u >= acumulada:
        i += 1
        t1 *= (1/2)
        t2 *= (2/3)
        acumulada += t1 + t2
    return i


if __name__ == "__main__":

    n_sim = 100_000
    sumatoria = 0
    for _ in range(n_sim):
        sumatoria += transformada_inversa()
    print(f"Esperanza: {sumatoria/n_sim}")
