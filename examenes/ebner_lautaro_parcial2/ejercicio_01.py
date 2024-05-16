import random
import math


def algo_x(p: list[float]):

    def sim_y():
        return random.randint(0, 3)

    def py(y):
        return 1/4

    def px(x):
        return p[x]

    c = (0.35) / (1/4)

    while True:
        y = sim_y()
        u = random.random()
        if u < px(y)/(c*py(y)):
            return y


if __name__ == "__main__":

    pass

    # para verificar descomentar!

    # resultados = [0 for _ in range(4)]
    # n_sim = 10_000
    # p = [0.13, 0.22, 0.35, 0.3]
    # for _ in range(n_sim):
    #     resultados[algo_x(p)] += 1
    # print([elem/n_sim for elem in resultados])
