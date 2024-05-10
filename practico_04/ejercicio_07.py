import time
import random
import math


def poisson(lamda):
    u = random.random()
    i = 0
    p = math.exp(-lamda)

    acumulada = p

    while u >= acumulada:
        i += 1
        p *= lamda / i
        acumulada += p

    return i


def poisson_optimized(lamda):
    p = math.exp(-lamda)
    acumulada = p
    for j in range(1, int(lamda)+1):
        p *= lamda/j
        acumulada += p

    u = random.random()
    if u >= acumulada:
        j = int(lamda)+1
        while u >= acumulada:
            p *= lamda/j
            acumulada += p
            j += 1
        return j-1

    j = int(lamda)
    while u < acumulada:
        acumulada -= p
        p *= j/lamda
        j -= 1
    return j+1


if __name__ == "__main__":
    print("ejercicio 07".center(100, " "))
    param = 10
    n_sim = 1_000
    for func in [poisson, poisson_optimized]:
        cont = 0
        start = time.time()
        for _ in range(n_sim):
            sim = func(param)
            cont += int(sim > 2)
        print(f"{func.__name__}")
        print(f"\tP(X > 2)={cont/n_sim}")
        print(f"\ttime {time.time() - start}")
