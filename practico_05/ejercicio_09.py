import math
import random


def exponencial(lamda):
    u = random.random()
    return -math.log(u)/lamda


def normal_rechazo(mu: float = 0.0, sigma: float = 1.0):
    while True:
        y1 = exponencial(1)
        y2 = exponencial(1)
        if y2 >= ((y1-1)**2) / 2:
            u = random.random()
            if u <= 1/2:
                return y1 * sigma + mu
            return -y1 * sigma + mu


def metodo_polar(mu: float = 0.0, sigma: float = 1.0):

    def f(n):
        return (n * sigma) + mu

    r_cuadrado = -2 * math.log(1-random.random())
    theta = 2 * math.pi * random.random()
    x = math.sqrt(r_cuadrado) * math.cos(theta)
    y = math.sqrt(r_cuadrado) * math.sin(theta)
    return f(x), f(y)


def metodo_razon_uniformes(mu: float = 0.0, sigma: float = 1.0):

    while True:
        u1 = random.random()
        u2 = random.random()

        z = (4*(2*math.e)**(-1/2)) * ((u2-(0.5)) / u1)

        if z**2 < -(4 * math.log(u1)):
            return z


if __name__ == "__main__":

    n_sim = 10_000
    for func in [normal_rechazo, lambda: metodo_polar()[1], metodo_razon_uniformes]:
        suma = 0
        suma_quadrado = 0
        for _ in range(n_sim):
            sim = func()
            suma += sim
            suma_quadrado += sim**2

        esperanza = suma/n_sim
        desviacion = math.sqrt((suma_quadrado/n_sim) - ((suma/n_sim)**2))
        print(f"{func.__name__ if func.__name__ != '<lambda>' else 'metodo_polar'}")
        print(f"\tesperanza: {round(esperanza, 4)}")
        print(f"\tdesviacion: {round(desviacion, 4)}")
