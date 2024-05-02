import random
import math


def monte_carlo_0_inf(g, n_sim: int):
    """
    Aproximacion de la integral de la funcion g sobre el intervalo [0, inf].
    """
    def h(y):
        return (1/y**2) * g((1/y) - 1)

    integral = 0

    for _ in range(n_sim):
        u = random.random()
        integral += h(u)

    return integral / n_sim


if __name__ == "__main__":

    def funcion_f(x):
        return 1/(((x+1)**2) * math.log(x+2))


    for n in [1_000, 10_000, 100_000]:
        integral = monte_carlo_0_inf(funcion_f, n)
        print(f"n: {n} integral: {integral}")