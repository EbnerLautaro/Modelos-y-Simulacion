import random
import math


def exponencial(lamda):
    return -math.log(random.random())/lamda


def eventos_poisson(lamda, T):
    t = 0
    events = []

    while t < T:
        # generamos una exponencial de parametro lamda
        t += exponencial(lamda=lamda)
        if t <= T:
            events.append(t)

    return len(events), events


if __name__ == "__main__":
    # Escriba un programa que calcule el número de eventos y sus tiempos de arribo en las primeras
    # T unidades de tiempo de un proceso de Poisson homogéneo con parámetro λ
    pass
