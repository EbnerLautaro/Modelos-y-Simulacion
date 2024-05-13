import random
import math
from typing import List, Callable


def exponencial(lamda):
    u = random.random()
    return ((-1) * math.log(1-u)) / lamda


def composition(p: List[float], var_list: List[Callable]):

    assert sum(p) == 1

    p_acum = 0
    p_list = []
    for i, pi in enumerate(p):
        p_acum += pi
        p_list.append(p_acum)

    u = random.random()
    i = 0
    while u >= p_list[i]:
        i += 1

    return var_list[i]()


if __name__ == "__main__":

    params = [1/3, 1/5, 1/7]
    proportions = [0.5, 0.3, 0.2]

    funcs = [
        lambda: exponencial(1/3),
        lambda: exponencial(1/5),
        lambda: exponencial(1/7),
    ]

    n_sim = 10_000

    suma = 0
    for _ in range(n_sim):
        suma += composition(proportions, funcs)

    print(f"esperanza: {suma/n_sim}")
