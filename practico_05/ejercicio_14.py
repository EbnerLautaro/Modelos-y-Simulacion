import math
import random


def proceso_poisson(lamda, T):

    t = 0
    events = []
    while t < T:
        u = random.random()
        t += -math.log(u)/lamda
        if t <= T:
            events.append(t)
    return len(events), events


def cap_autobus():
    return random.randint(20, 40)


if __name__ == "__main__":

    # Los autobuses que llevan los aficionados a un encuentro deportivo llegan a destino de acuerdo
    # con un proceso de Poisson a razón de cinco por hora. La capacidad de los autobuses es una variable
    # aleatoria que toma valores en el conjunto: {20,21,...,40} con igual probabilidad. A su vez, las capacidades
    # de dos autobuses distintos son variables independientes. Escriba un algoritmo para simular la llegada de
    # aficionados al encuentro en el instante t = 1hora.

    # cant_autobuses, t = proceso_poisson(lamda=5, T=1)

    # cant_aficionados = 0
    # for i in range(cant_autobuses):
    #     cant_aficionados += cap_autobus()
    # print(f"Autobuses:     {cant_autobuses}")
    # print(f"Aficionados:   {cant_aficionados}")

    n_sim = 10_000
    suma = 0
    for _ in range(n_sim):
        cantidad, llegadas = proceso_poisson(5, 1)
        suma += sum(cap_autobus() for _ in range(cantidad))

    print(f"esperanza: \t{suma/n_sim}")
