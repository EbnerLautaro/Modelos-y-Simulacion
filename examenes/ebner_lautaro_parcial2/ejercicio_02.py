import random
import math


def ejercicio2():
    u = random.random()
    if u < 2/3:
        return ((3*u)/2)**(2 / 3)

    return ((u-(2/3))*3)+1


def test_ejercicio2(u):
    if u < 2/3:
        return ((3*u)/2)**(2 / 3)

    return ((u-(2/3))*3)+1


if __name__ == "__main__":
    # para probar el ejercicio 2a descomentar!
    # print(f"u=0.2 => x={test_ejercicio2(0.2)}")
    # print(f"u=0.5 => x={test_ejercicio2(0.5)}")
    # print(f"u=0.8 => x={test_ejercicio2(0.8)}")

    n_sim = 10_000
    cont = 0
    for _ in range(n_sim):
        sim = ejercicio2()
        if sim > 1:
            cont += 1

    print(f"simulacion de P(X>1): {cont/n_sim}")
