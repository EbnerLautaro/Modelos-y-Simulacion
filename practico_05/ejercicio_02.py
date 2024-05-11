import math
import random


def inv_pareto(a):
    u = random.random()
    return (1-u) ** (1/(-a))


if __name__ == "__main__":

    n_sim = 100_000
    a = 2
    sumatoria = 0
    for _ in range(n_sim):
        sumatoria += inv_pareto(a=a)

    print(sumatoria/n_sim)
