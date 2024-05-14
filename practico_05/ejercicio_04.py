from typing import List
import random
import math

if __name__ == "__main__":
    pass


def gen_exp(lam):  # Generador de exponencial.
    u = 1-random.random()
    return -math.log(u)/lam


def generator():
    y = gen_exp(1)
    u = random.random()
    return u**(1/y)


if __name__ == "__main__":
    generator()
