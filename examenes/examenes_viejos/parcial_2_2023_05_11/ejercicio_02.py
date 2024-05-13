import random


def inversa():
    u = random.random()

    if u < 1/2:
        return 4*u

    return 1/(1-u)


if __name__ == "__main__":

    n_sim = 10_000
    cont = 0
    suma = 0
    for _ in range(n_sim):
        x = inversa()
        cont += x <= 3
        suma += x

    print(f"esperanza: {suma/n_sim}")
    print(f"P(X<=3): {cont/n_sim}")
