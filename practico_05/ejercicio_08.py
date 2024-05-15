import math
import random


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

    print("ejercicio a".center(100, "-"))
    n_sim = 10_000
    suma_ar = 0
    suma_ti = 0
    suma_su = 0

    c = 2
    for _ in range(n_sim):
        suma_ar += aceptacion_rechazo(sim_y=sim_y, px=p_x, py=p_y, c=c)
        suma_ti += transformada_inversa()
        suma_su += suma_uniformes()

    print(f"esperanza acetacion_rechazo:    {suma_ar/n_sim}")
    print(f"esperanza transformada_inversa: {suma_ti/n_sim}")
    print(f"esperanza suma uniformes:       {suma_su/n_sim}")
