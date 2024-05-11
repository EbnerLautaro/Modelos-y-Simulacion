import random
import math


def inversa_a():

    u = random.random()

    if u <= 1/4:
        return 2*(1+math.sqrt(u))
    else:
        return -6*(-1+math.sqrt((1-u)/3))


def inversa_b():
    u = random.random()

    if u <= 3/5:
        return (1/3)*(math.sqrt(3) * math.sqrt((35*u)+27) - 9)

    else:
        return (((35*u)-19)**(1/3)) / ((2)**(1/3))


def inversa_c():
    u = random.random()

    if u <= 1/16:
        return math.log(16*u)/4

    else:
        return ((u*16)-1)/4


if __name__ == "__main__":
    n_sim = 10_000
    sum_a = 0
    sum_b = 0
    sum_c = 0

    for _ in range(n_sim):
        sum_a += inversa_a()
        sum_b += inversa_b()
        sum_c += inversa_c()

    print(f"Esperanza ejercicio a: {sum_a/n_sim}")
    print(f"Esperanza ejercicio b: {sum_b/n_sim}")
    print(f"Esperanza ejercicio c: {sum_c/n_sim}")
