import random

PROBS = [0.05, 0.1, 0.2, 0.3, 0.35]


def ejercicio1a():

    def p(x):
        return PROBS[x]

    def q(x):
        return 1/5

    def simular_y():
        return random.randint(0, 4)

    c = max(p(x)/q(x) for x in range(5))

    while True:
        y = simular_y()
        u = random.random()

        if u < (p(y)/(q(y)*c)):
            return y


def ejercicio1b(N: int):
    suma = 0
    for _ in range(N):
        suma += ejercicio1a()
    return suma/N


def ejercicio2a():

    probs = [elem for elem in enumerate(PROBS)]
    probs = sorted(probs, key=lambda elem: elem[1], reverse=True)

    u = random.random()
    i = 0
    acumulador = probs[i][1]
    while u >= acumulador:
        i += 1
        acumulador += probs[i][1]

    return probs[i][0]


def ejercicio2b(N):
    suma = 0
    for _ in range(N):
        suma += ejercicio2a()
    return suma/N


def ejercicio3():
    return sum([i*prob for i, prob in enumerate(PROBS)])


if __name__ == "__main__":
    # Sea X una variable aleatoria que toma los valores del 0 al 4 con probabilidades:
    #     p_{0}=0.05
    #     p_{1}=0.1
    #     p_{2}=0.2
    #     p_{3}=0.3
    #     p_{4}=0.35
    #
    # 1) Escribir una función ejercicio1a() en python que genere valores de la variable X usando el método de
    #     aceptación y rechazo, rechazando con una variable uniforme discreta, y escribir una función
    #     ejercicio1b(N) que estime su valor esperado con N simulaciones usando la función ejercicio1a().
    #     Imprimir el valor de ejercicio1b(10000).

    # 2) Escribir una función ejercicio2a() en python que genere valores de la variable X usando el método de la
    #     transformada inversa mejorada, y escribir una función ejercicio2b(N) que estime su valor esperado con N
    #     simulaciones usando la función ejercicio2a(). Imprimir el valor de ejercicio2b(10000).

    # 3) Escribir un código ejercicio3() que calcule e imprima el valor esperado exacto de la variable aleatoria X.
    n_sim = 10_000
    print(f"ejercicio1b: \t{ejercicio1b(n_sim)}")
    print(f"ejercicio2b: \t{ejercicio2b(n_sim)}")
    print(f"ejercicio3:  \t{ejercicio3()}")
