

import random


def aceptacion_rechazo(sim_y, px, py, c):
    while True:
        y = sim_y()
        u = random.random()
        if u < (px(y) / (py(y) * c)):
            return y


if __name__ == "__main__":

    def sim_y():
        p = 6/10
        i = 1
        p_i = p
        acumulada = p_i
        u = random.random()
        while u >= acumulada:
            i += 1
            p_i *= (1-p)
            acumulada += p_i
        return i

    def py(y):
        return (6/10) * ((4/10) ** (y-1))

    def px(x):
        assert 1 <= x <= 20
        denominador = 0
        for i in range(1, 21):
            denominador += (6/10) * ((4/10) ** (i-1))

        numerador = (6/10) * ((4/10) ** (x-1))
        return numerador/denominador

    c = max(px(x)/py(x) for x in range(1, 20))

    print([round(px(i), 4) for i in range(1, 21)])
