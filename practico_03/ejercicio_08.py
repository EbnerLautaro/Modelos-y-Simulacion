import random
import math


def simulacion(limit: float):

    producto = 1
    cont = 0
    while producto >= limit:
        producto *= random.random()
        cont += 1

    return cont


def promedio(n, limit):
    if n == 0:
        return None

    suma = 0
    for _ in range(n):
        suma += simulacion(limit)

    return suma/n


if __name__ == "__main__":
    


    for n in [100, 1_000, 10_000, 100_000, 1_000_000]:
        print(f"n: {n :<8}  E(X): {promedio(n, math.e **(-3)):<12}")
