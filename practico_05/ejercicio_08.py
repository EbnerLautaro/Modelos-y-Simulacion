import math
import random
import time


def suma_uniformes():
    return random.random() + random.random()


def p_x(x):
    if 0 <= x < 1:
        return x

    if 1 <= x < 2:
        return 2-x

    return 0


def sim_y():
    return random.uniform(0, 2)


def p_y(y):
    return 1/(2-0)


def aceptacion_rechazo(sim_y, py, px, c):
    while True:
        y = sim_y()
        u = random.random()
        if u < px(y) / (py(y)*c):
            return y


def transformada_inversa():
    u = random.random()
    if u <= 1/2:
        return math.sqrt(2*u)

    return 2 - (math.sqrt(2)*math.sqrt(1-u))


if __name__ == "__main__":

    print("ejercicio b".center(100, "-"))

    n_sim = 10_000

    for func in [lambda: aceptacion_rechazo(sim_y=sim_y, px=p_x, py=p_y, c=2), transformada_inversa, suma_uniformes]:
        suma = 0
        start = time.time()
        for _ in range(n_sim):
            suma += func()
        print(f"{func.__name__}:")
        print(f"\t esperanza:   {suma/n_sim}:")
        print(f"\t time:        {time.time() - start}:")

    print("¿Para qué valor x0 se cumple que P(X > x0) = 0.125?")
    print(f"\t x0 =         {2 - (math.sqrt(2)*math.sqrt(1-0.875))}")
