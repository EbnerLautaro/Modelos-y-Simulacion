import random
import math


def simulacion():
    suma = 0
    cont = 0
    while suma <= 1:
        suma += random.random()
        cont += 1

    return cont


def promedio(n):
    suma = 0
    for _ in range(n):
        suma += simulacion()

    return suma/n


if __name__ == "__main__":
    


    for n in [100, 1_000, 10_000, 100_000, 1_000_000]:
        print(f"n: {n :<8}  E(X): {promedio(n):<12}")


    print(f"valor de e: {math.e}")