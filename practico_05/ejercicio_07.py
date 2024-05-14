import time
import math
import random


def transformada_inversa():
    u = random.random()
    return (math.e)**(u)


def aceptacion_rechazo(sim_y, py, px, c):

    while True:
        y = sim_y()
        u = random.random()
        if u < (px(y)/(py(y)*c)):
            return y


if __name__ == "__main__":

    def p_x(x):
        return 1/x if (1 <= x <= math.e) else 0

    def p_y(y):
        return 1/(math.e-1)

    def sim_y():
        return random.uniform(1, math.e)

    c = math.e

    n_sim = 10_000
    for func in [transformada_inversa, lambda: aceptacion_rechazo(sim_y=sim_y, px=p_x, py=p_y, c=c)]:
        suma = 0
        start = time.time()

        for _ in range(n_sim):
            suma += func()

        print(f"{func.__name__}")
        print(f"\tesperanza:  {suma/n_sim}")
        print(f"\ttime:       {time.time()-start}")
