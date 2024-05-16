import random
import math


def generator():
    U = random.random()
    if U < 0.22:
        return 1
    elif U < 0.55:
        return 2
    elif U < 0.72:
        return 3
    elif U < 0.9999:
        return 4
    else:
        return 5


if __name__ == "__main__":
    n_sim = 1_000_000
    cont = 0
    for _ in range(n_sim):
        cont += generator()

    print(cont/n_sim)
