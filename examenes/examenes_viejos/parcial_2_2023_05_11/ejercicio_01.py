import random


def variableX():
    u = random.random()
    v = random.random()

    if u < 0.3:
        return 0
    elif u < 0.75:
        if v < 0.2:
            return 1
        else:
            return 2
    else:
        if v < 0.8:
            return 2
        else:
            return 3


def transdormada_inversa():
    u = random.random()
    probs = [(0, 0.3), (1, 0.09), (2, 0.56), (3, 0.05)]

    i = 0
    acumulado = probs[i][1]
    while u >= acumulado:
        i += 1
        acumulado += probs[i][1]

    return probs[i][0]


if __name__ == "__main__":

    resultados = [0 for _ in range(4)]
    resultados_2 = [0 for _ in range(4)]

    n_sim = 10_000
    for _ in range(n_sim):
        resultados[variableX()] += 1
        resultados_2[transdormada_inversa()] += 1

    print([elem/n_sim for elem in resultados])
    print([elem/n_sim for elem in resultados_2])
