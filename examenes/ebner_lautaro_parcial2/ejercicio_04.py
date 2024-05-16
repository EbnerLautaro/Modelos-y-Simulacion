import random


def f(x, y):
    return (x**2) + (y - (abs(x)**(3/2))) ** 2


def area(n_sim: int):
    cont = 0
    for _ in range(n_sim):
        x = random.uniform(-1.5, 1.5)
        y = random.uniform(-1.5, 1.5)
        if f(x, y) <= 1:
            cont += 1

    return 9 * cont / n_sim


if __name__ == "__main__":

    n_sim = 100000
    print(area(n_sim))
