import math
import random
from typing import Callable


def fun_i(x: float) -> float:
    return math.exp(x) / math.sqrt(2 * x)


def monte_carlo_0_1(func: Callable, max_sim: int, n_min: int, d_threshold: float):

    values = []
    n_values = n_min
    while n_values <= max_sim:
        values_to_insert = [
            func(random.random()) for _ in range(n_values - len(values))
        ]
        values.extend(values_to_insert)

        mean = sum(values) / len(values)
        mean_sq = sum(value**2 for value in values) / len(values)
        variance = mean_sq - (mean**2)
        deviance = math.sqrt(variance)

        if deviance <= d_threshold:
            break
        else:
            n_values += 1
    return values, mean, variance


def fun_ii(x):

    def f1(y):
        return (-y) ** 2 * math.exp(-((-x) ** 2))

    def f2(w):
        return w**2 * math.exp(-((w) ** 2))

    return (f1(x) + f2(x))


def monte_carlo_0_inf(func: Callable, max_sim: int, n_min: int, d_threshold: float):

    def h(u):
        return (1 / (u**2)) * func((1 / u) - 1)

    values = []
    n_values = n_min
    while n_values <= max_sim:

        values_to_insert = [h(random.random())
                            for _ in range(n_values - len(values))]
        values.extend(values_to_insert)

        mean = sum(values) / len(values)
        mean_sq = sum(value**2 for value in values) / len(values)
        variance = mean_sq - (mean**2)
        deviance = math.sqrt(variance)

        if deviance <= d_threshold:
            break
        else:
            n_values += 1
    return values, mean, variance


if __name__ == "__main__":
    # Genere al menos 100 valores y deténgase cuando la desviación estándar muestral S del estimador sea
    # menor que 0,01.

    print("ejercicion i".center(100, "="))
    _, media, varianza = monte_carlo_0_1(
        func=fun_i, max_sim=10_000, n_min=100, d_threshold=0.01
    )
    print(f"\tMedia      {media}")
    print(f"\tVarianza   {varianza}")

    print("ejercicion ii".center(100, "="))
    _, media, varianza = monte_carlo_0_inf(
        func=fun_ii, max_sim=10_000, n_min=100, d_threshold=0.01
    )
    print(f"\tMedia      {media}")
    print(f"\tVarianza   {varianza}")
