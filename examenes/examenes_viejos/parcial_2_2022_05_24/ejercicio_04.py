import random
import math


def tirada():
    return random.randint(0, 1)


def ensayos():
    ultima_tirada = tirada()
    qty = 1
    while True:
        actual = tirada()
        qty += 1
        if ultima_tirada != actual:
            return qty
        ultima_tirada = actual


def geometrica(p):
    i = 1
    p_i = p
    acumulada = p_i
    u = random.random()
    while u >= acumulada:
        p_i *= (1-p)
        acumulada += p_i
        i += 1
    return i


def px(x):
    if x < 2:
        return 0
    return ((2**(x-1))+2)/(3**x)


def py(y):
    return (1/3)*(2/3)**(y-1)


def aceptacion_rechazo(sim_y, py, px, c):
    iteraciones = 0
    while True:
        iteraciones += 1
        y = sim_y()
        u = random.random()
        if u < px(y)/(py(y)*c):
            return y, iteraciones


if __name__ == "__main__":

    # La variable aleatoria X representa el numero de tiradas independientes que deben realizarse hasta obtener ´
    # dos tiradas consecutivas distintas. Por ejemplo, X(cara, cara, cruz) = X(cruz, cruz, cara) = 3.

    n_sim = 10_000
    cont = 0
    for _ in range(n_sim):
        if ensayos() == 4:
            cont += 1
    print(f"P(X=4)= {cont/n_sim}")

    c = 2

    n_sim = 10_000
    iteraciones = 0
    suma = 0
    for _ in range(n_sim):
        sim, cont = aceptacion_rechazo(
            c=c, px=px, py=py, sim_y=lambda: geometrica(1/3))
        iteraciones += cont
        suma += sim

    print(f"esperanza:              {suma/n_sim}")
    print(f"esperanza iteraciones:  {iteraciones/n_sim}")
