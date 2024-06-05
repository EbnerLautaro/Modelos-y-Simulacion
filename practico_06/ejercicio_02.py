import math
import random
from typing import Callable


def fun_1(x: float) -> float:
    return math.exp(x)/math.sqrt(2*x)


def monte_carlo(func, max_sim, n_min, d_threshold):

    values = []
    n_values = n_min
    while n_values <= max_sim:
        values_to_insert = [func(random.random())
                            for _ in range(n_values - len(values))]
        values.extend(values_to_insert)

        mean = sum(values)/len(values)
        mean_sq = sum(value ** 2 for value in values) / len(values)
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
    _, media, varianza = monte_carlo(
        func=fun_1, max_sim=10_000, n_min=100, d_threshold=0.01)
    print(f"\tMedia      {media}")
    print(f"\tVarianza   {varianza}")
