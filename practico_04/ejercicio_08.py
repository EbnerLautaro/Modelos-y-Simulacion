import math
import random

LAMDA = 0.7
K = 10


def cociente(lamda, k):
    sumatoria = 0
    j_fact = 1
    for j in range(0, k+1):
        if j == 0:
            sumatoria += math.exp(-lamda)
            continue

        j_fact *= j
        sumatoria += math.exp(-lamda) * ((lamda**j) / j_fact)

    return sumatoria


def transformada_inversa(lamda, k):
    q = cociente(lamda=lamda, k=k)
    i = 0
    p_i = math.exp(-lamda)/q
    acumulador = p_i
    u = random.random()
    while u >= acumulador:
        i += 1
        p_i *= (lamda/i)
        acumulador += p_i
    return i


def aceptacion_rechazo(px, py, sim_y, c):

    while True:
        y = sim_y()
        u = random.random()
        if u < (px(y)/(py(y)*c)):
            return y


if __name__ == "__main__":

    def p_x(x):
        aux = (math.exp(-LAMDA) * (LAMDA**x)) / math.factorial(x)
        return aux / cociente(k=10, lamda=LAMDA)

    def p_y(y):
        return (math.exp(-LAMDA) * (LAMDA**y)) / math.factorial(y)

    c = max(p_x(i)/p_y(i) for i in range(K))

    def poisson():
        u = random.random()
        i = 0
        p = math.exp(-LAMDA)
        acumulada = p
        while u >= acumulada:
            i += 1
            p *= LAMDA / i
            acumulada += p

        return i

    n_sim = 1_000
    cont_ti = 0
    cont_ar = 0
    for _ in range(n_sim):
        sim_ti = transformada_inversa(k=K, lamda=LAMDA)
        sim_ar = aceptacion_rechazo(px=p_x, py=p_y, sim_y=poisson, c=c)
        cont_ti += int(sim_ti > 2)
        cont_ar += int(sim_ar > 2)

    print("P(X>2):")
    print(f"\ttransformada_inversa: {cont_ti/n_sim} ")
    print(f"\taceptacion_rechazo:   {cont_ar/n_sim}")
