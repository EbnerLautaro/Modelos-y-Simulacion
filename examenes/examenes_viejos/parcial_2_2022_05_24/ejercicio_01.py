import random
import math


def AliasX():
    U = random.random()
    V = random.random()
    if U < 0.4:
        if V < 0.8:
            return 0
        else:
            return 2
    elif U < 0.75:
        if V < 0.6:
            return 1
        else:
            return 3
    else:
        return 2


def urna(k: int, probs: list[tuple[int, float]]) -> int:
    A = []
    for (key, p) in probs:
        for _ in range(int(k*p)):
            A.append(key)

    return A[int(random.random()*k)]


if __name__ == "__main__":

    print(" ejercicio a ".center(100, "-"))
    n_sim = 10_000

    resultados = [0 for _ in range(4)]

    for _ in range(n_sim):
        sim = AliasX()
        resultados[sim] += 1

    print([(i, round(n/n_sim, 4)) for i, n in enumerate(resultados)])

    print(" ejercicio c ".center(100, "-"))
    print("esta en el codigo!")
    probs = [(0, 0.32), (1, 0.21), (2, 0.33), (3, 0.14)]

    print(f"valor generado: {urna(100, probs=probs)}")
