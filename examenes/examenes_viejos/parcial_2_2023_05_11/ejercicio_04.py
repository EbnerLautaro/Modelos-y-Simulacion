import math
import random


def exponencial(lamda):
    u = random.random()
    return -math.log(u)/lamda


def binomial(n, p):
    c = p/(1-p)
    i = 0
    p_i = (1-p)**n
    acumulada = p_i
    u = random.random()
    while u >= acumulada:
        p_i *= c*(n-i)/(i+1)
        acumulada += p_i
        i += 1

    return i


def simulacion():
    reclamos = binomial(n=1_000, p=0.05)
    monto_acumulado = 0
    for _ in range(reclamos):
        monto_acumulado += exponencial(1/800)
    return monto_acumulado


if __name__ == "__main__":
    # Una compania de seguros tiene 1000 clientes, cada uno de los cuales puede presentar un reclamo
    # en forma independiente en el proximo mes con probabilidad p= 0.05. Se asume que los montos de los reclamos
    # son variables aleatorias independientes con distribucion exponencial con media $800

    # a) Disenar una simulacion de los reclamos de clientes a lo largo del proximo mes. Describir las variables
    # aleatorias utilizadas en la simulacion

    # b) Implementar la simulacion descripta en a) y utilizarla para estimar la probabilidad de que la suma de esos
    # reclamos exceda los $50000 con 10000 simulaciones

    n_sim = 10_000
    cont = 0
    for _ in range(n_sim):
        monto = simulacion()
        if monto > 50_000:
            cont += 1

    print(cont/n_sim)
