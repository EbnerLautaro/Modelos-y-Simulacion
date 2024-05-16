import math
import random

# ========================= ejercicio 1 ===================================


def algo_x(p: list[float]):

    def sim_y():
        return random.randint(0, 3)

    def py(y):
        return 1/4

    def px(x):
        return p[x]

    c = (0.35) / (1/4)

    while True:
        y = sim_y()
        u = random.random()
        if u < px(y)/(c*py(y)):
            return y

# ========================= ejercicio 2 ===================================


def ejercicio2():
    u = random.random()
    if u < 2/3:
        return ((3*u)/2)**(2 / 3)

    return ((u-(2/3))*3)+1


def test_ejercicio2(u):
    if u < 2/3:
        return ((3*u)/2)**(2 / 3)

    return ((u-(2/3))*3)+1


# ========================= ejercicio 3 ===================================

def exponential(lamda):
    u = 1 - random.random()
    return -math.log(u)/lamda


def hot_dog(T):

    def lamda_t(t):
        if 0 <= t < 3:
            return 5 + 5*t
        elif 3 <= t <= 5:
            return 20
        elif 5 < t <= 9:
            return 30-2*t

    intervals = [(10, 1), (15, 2), (20, 6), (18, 8),
                 (12, 9)]  # (lamda, limite_derecho)

    j = 0
    events = []
    t = exponential(lamda=intervals[j][0])
    while t <= T:
        lamda = intervals[j][0]
        b = intervals[j][1]

        if t <= b:
            v = random.random()
            if v < lamda_t(t)/lamda:
                events.append(t)
            t += exponential(lamda)

        else:  # t > b
            t = b + ((t-b) * lamda) / intervals[j+1][0]
            j += 1
    return len(events), events


# ========================= ejercicio 4 ===================================

def f(x, y):
    return (x**2) + (y - (abs(x)**(3/2))) ** 2


def area(n_sim: int):
    cont = 0
    for _ in range(n_sim):
        x = random.uniform(-1.5, 1.5)
        y = random.uniform(-1.5, 1.5)
        if f(x, y) <= 1:
            cont += 1

    return 9 * cont / n_sim


if __name__ == "__main__":
    # ========================= ejercicio 1 ===================================
    print("ejercicio 1".center(100, "-"))

    print("para verificar ejercicio1 descomentar!")
    # resultados = [0 for _ in range(4)]
    # n_sim = 10_000
    # p = [0.13, 0.22, 0.35, 0.3]
    # for _ in range(n_sim):
    #     resultados[algo_x(p)] += 1
    # print([elem/n_sim for elem in resultados])

    # ========================= ejercicio 2 ===================================
    print("ejercicio 2".center(100, "-"))

    # para probar el ejercicio 2a descomentar!
    # print(f"u=0.2 => x={test_ejercicio2(0.2)}")
    # print(f"u=0.5 => x={test_ejercicio2(0.5)}")
    # print(f"u=0.8 => x={test_ejercicio2(0.8)}")

    n_sim = 10_000
    cont = 0
    for _ in range(n_sim):
        sim = ejercicio2()
        if sim > 1:
            cont += 1

    print(f"simulacion de P(X>1): {cont/n_sim}")

    # ========================= ejercicio 3 ===================================
    print("ejercicio 3".center(100, "-"))
    n_sim = 10_000
    arrivos = 0
    T = 9
    for _ in range(n_sim):
        arrivos += hot_dog(T=T)[0]
    print(f"esperanza: {arrivos/n_sim}")

    # ========================= ejercicio 4 ===================================
    print("ejercicio 4".center(100, "-"))
    n_sim = 100000
    print(f"area encerrada por la curva: {area(n_sim=n_sim)}")

    print("\n")
