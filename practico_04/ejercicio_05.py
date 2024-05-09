import math
from auxiliares import GeneradorVariableDiscreta
import random
import time


def binomial_transformada_inversa(n: int, p: float) -> int:
    """
    generacion de una variable aleatoria con distribucion binomial, utilizando la transformada inversa
    """

    def prob(i: int) -> float:
        fact = math.factorial  # para que sea mas legible
        return (fact(n) / (fact(i) * fact(n - i))) * (p**i) * ((1 - p) ** (n - i))

    probabilities = {i: prob(i) for i in range(n)}

    gen = GeneradorVariableDiscreta()
    return gen.transformada_inversa(probs=probabilities)


def ensayos(n: int, p: float) -> int:
    exitos = 0
    for _ in range(n):
        u = random.random()
        exitos += int(u <= p)
    return exitos


if __name__ == "__main__":
    # Implemente dos métodos para generar una binomial Bin(n, p):
    #     I) Usando transformada inversa.
    #     II) Simulando n ensayos con probabilidad de éxito p y contando el número de éxitos.

    # Para ambos métodos:
    #     a) Compare la eficiencia de ambos algoritmos para n = 10 y p = 0,3, evaluando el tiempo necesario para
    #         realizar 10000 simulaciones.
    #     b) Estime el valor con mayor ocurrencia y la proporción de veces que se obtuvieron los valores 0 y 10
    #         respectivamente.
    #     c) Compare estos valores con las probabilidades teóricas de la binomial. Si están alejados, revise el código.

    # si creamos la funcion de densidad de probabilidad y luego llamamos a la funcion transformada inversa generica, obtenemos la siguiente funcion

    print("ejercicio a".center(100, "="))
    n_sim = 10_000

    def time_funcs(funcs: list, n_sim, n, p):
        for func in funcs:
            start = time.time()
            for _ in range(n_sim):
                func(n, p)
            time_elapsed = time.time() - start
            print(f"{func.__name__} \n\ttime: {time_elapsed}")

    time_funcs(funcs=[binomial_transformada_inversa, ensayos], n_sim=n_sim, n=10, p=0.3)

    print("ejercicio b".center(100, "="))
    n_sim = 10_000
    for func in [binomial_transformada_inversa, ensayos]:
        sumatoria = 0
        results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for _ in range(n_sim):
            elem = func(n=10, p=0.3)
            results[elem] += 1
            sumatoria += elem

        print(f"{func.__name__}")
        print(f"\tMedia: {sumatoria/n_sim}")
        print(f"\tProporcion: {[elem/n_sim for elem in results]}")

    print("ejercicio c".center(100, "="))

    p = 0.3

    def prob(i: int, n: int) -> float:
        fact = math.factorial  # para que sea mas legible
        return (fact(n) / (fact(i) * fact(n - i))) * (p**i) * ((1 - p) ** (n - i))

    print("Probabilidades teoricas:")
    probs = [prob(i, 10) % 0.1000 for i in range(10)]
    formatted = ", ".join(["{:.5f}".format(number) for number in probs])
    print(f"\t[{formatted}]")
