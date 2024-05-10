import time
import random
from typing import Callable, List, Tuple
import math


def transformada_inversa(probs: List[Tuple[any, int]]) -> any:

    probs = sorted(probs, key=lambda elem: elem[1], reverse=True)

    i = 0
    F = probs[0][1]
    u = random.random()
    while u >= F:
        i += 1
        F += probs[i][1]
    return probs[i][0]


def aceptacion_rechazo(px, py, sim_y, c) -> any:

    while True:

        y = sim_y()
        u = random.random()
        if u < (px(y) / (py(y) * c)):
            return y


if __name__ == "__main__":

    # Una variable aleatoria X tiene una función de probabilidad puntual pi = P(X = i) dada por
    # p0 = 0,15, p1 = 0,20, p2 = 0,10, p3 = 0,35, p4 = 0,20
    # I) Describir mediante un pseudocodigo un algoritmo que simule X utilizando el método de la transformada inversa y que minimice el número esperado de búsquedas.
    # II) Describir mediante un pseudocodigo un algoritmo que simule X utilizando el método de aceptación y rechazo con una variable soporte Y con distribución binomial B(4, 0.45).
    # III) Compare la eficiencia de los dos algoritmos realizando 10000 simulaciones

    probs = [(0, 0.15), (1, 0.2), (2, 0.10), (3, 0.35), (4, 0.2)]

    print("transformada inversa")
    start = time.time()
    for _ in range(10_000):
        transformada_inversa(probs=probs)
    print(f"\ttime: {time.time() - start}")

    def px(x: int) -> float:
        """
        Retorna la probabilidad de que la variable X tome cada valor
        """

        for elem in [(0, 0.15), (1, 0.2), (2, 0.10), (3, 0.35), (4, 0.2)]:
            if x == elem[0]:
                return elem[1]

        raise ValueError(f"{x} is not a posible value of X")

    def py(y: int) -> float:
        """
        la funcion computa P(X=i), donde X distribulye B(4, 0.45)
        """
        assert 0 <= y and y <= 4
        n = 4
        p = 0.45
        return math.comb(n, y) * (p**y) * ((1-p)**(n-y))

    def sim_y():
        """
        Vamos a simular la variable binomial Y con parametros n=4, p=0.45
        a travez del metodo de transformada inversa
        """
        n = 4
        p = 0.45

        acum = (1 - p) ** n
        f = acum
        n_exitos = 0
        x = random.random()
        while x >= f:
            acum *= p / (1 - p) * (n - n_exitos) / (n_exitos + 1)
            f += acum
            n_exitos += 1

        return n_exitos

    c = math.ceil(max(px(i)/py(i) for i in [elem[0] for elem in probs]))

    print("aceptacion_rechazo")
    start = time.time()
    for i in range(10_000):
        aceptacion_rechazo(px=px, py=py, c=c, sim_y=sim_y)
    print(f"\ttime {time.time()-start}")
