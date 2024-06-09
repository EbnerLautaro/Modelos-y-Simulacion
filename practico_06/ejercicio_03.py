import math
import random
from typing import Callable

F = ":.4f"


def fun_i(x: float) -> float:
    return math.sin(x) / x


def fun_ii(x: float) -> float:
    return 3 / (3 + x**4)


def func_a_b(x, func, a, b):
    assert 0 <= x <= 1
    return func(a + ((b - a) * x)) * (b - a)


def func_0_inf(x, func):
    assert 0 <= x <= 1
    return (1 / (x**2)) * func((1 / x) - 1)


def monte_carlo(func, n_sim):

    media = func(random.random())
    S_sq = 0
    n = 1

    while n <= n_sim:
        sim = func(random.random())

        media_ant = media
        media = media_ant + (sim - media_ant) / (n + 1)

        S_sq_ant = S_sq
        S_sq = (1 - (1 / n)) * S_sq_ant + (n + 1) * (media - media_ant) ** 2

        n += 1

    ic = math.sqrt(S_sq / n)

    return media, math.sqrt(S_sq), ic


def monte_carlo_d(func, d_threshold, min_sim):

    media = func(random.random())
    S_sq = 0
    n = 1
    ic = math.sqrt(S_sq / n)

    while n <= min_sim or ic > d_threshold:

        sim = func(random.random())

        media_ant = media
        media = media_ant + (sim - media_ant) / (n + 1)

        S_sq_ant = S_sq
        S_sq = (1 - (1 / n)) * S_sq_ant + (n + 1) * (media - media_ant) ** 2
        n += 1
        ic = math.sqrt(S_sq / n)

        if n == 100:
            print(media, math.sqrt(S_sq / n))
            break

    return media, math.sqrt(S_sq), ic, n


if __name__ == "__main__":
    d = 0.001 / (2 * 1.96)
    d = d * 2
    print(d)
    print(" ejercicio i ".center(100, "="))

    def f(x): return func_a_b(x=x, func=fun_i, a=math.pi, b=2 * math.pi)

    for n in [1000, 5_000, 7_000]:
        print(f"n_sim\t{n}")
        mu, var, ic = monte_carlo(
            func=f,
            n_sim=1000,
        )
        print(f"\tmedia {mu:F}")
        print(f"\tvar   {var:F}")
        print(f"\tic    [{mu - 1.96*ic:F}, {mu + 1.96*ic:F}]\tdif: {ic:F}")

    mu, var, ic, n = monte_carlo_d(
        func=f,
        d_threshold=d,
        min_sim=100,
    )
    print(f"n_sim\t{n}")
    print(f"\tmedia {mu:F}")
    print(f"\tvar   {var:F}")
    print(f"\tic    [{mu - 1.96*ic:F}, {mu + 1.96*ic:F}]\tdif: {ic:F}")

    print(" ejercicio ii ".center(100, "="))

    def f(x): return func_0_inf(x=x, func=fun_ii)

    for n in [1000, 5_000, 7_000]:
        print(f"n_sim\t{n}")
        mu, var, ic = monte_carlo(
            func=f,
            n_sim=1000,
        )
        print(f"\tmedia {mu:F}")
        print(f"\tvar   {var:F}")
        print(f"\tic    [{mu - 1.96*ic:F}, {mu + 1.96*ic:F}]\tdif: {ic:F}")

    mu, var, ic, n = monte_carlo_d(
        func=f,
        d_threshold=d,
        min_sim=100,
    )
    print(f"n_sim\t{n}")
    print(f"\tmedia {mu:F}")
    print(f"\tvar   {var:F}")
    print(f"\tic    [{mu - 1.96*ic:F}, {mu + 1.96*ic:F}]\tdif: {ic:F}")
