import random
import math


def lamda_t_i(t):
    return 3 + (4/(t+1))


def lamda_t_ii(t):
    return (t-2)**2 - (5*t) + 17


def lamda_t_iii(t):
    if 2 <= t <= 3:
        return (t/2)-1
    if 3 <= t <= 6:
        return 1 - (t/6)
    return 0


def poisson_no_homogeneo_adelgazamiento(T, lamda, lamda_t):
    events = []
    t = -math.log(random.random()) / lamda
    while t <= T:
        v = random.random()
        if v < lamda_t(t)/lamda:
            events.append(t)
        t += -math.log(random.random()) / lamda
    return len(events), events


def exponential(lamda):
    u = random.random()
    return -math.log(u)/lamda


def poisson_no_homogeneo_adelgazamiento_mejorado(T, lamda_t, intervals):
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


if __name__ == "__main__":

    suma_i = 0
    suma_ii = 0
    suma_iii = 0
    suma_i_m = 0
    suma_ii_m = 0
    suma_iii_m = 0

    interval_i = [(7, 1), (5, 2), (13/3, 3)]
    interval_ii = [(21, 2), (7, 4), (1, 5)]
    interval_iii = [(1/2, 3), (1/2, 4), (2/6, 6)]

    n_sim = 10_000

    for _ in range(n_sim):

        suma_i += poisson_no_homogeneo_adelgazamiento(3, 7, lamda_t_i)[0]
        suma_ii += poisson_no_homogeneo_adelgazamiento(5, 21, lamda_t_ii)[0]
        suma_iii += poisson_no_homogeneo_adelgazamiento(6, 1/2, lamda_t_iii)[0]
        suma_i_m += poisson_no_homogeneo_adelgazamiento_mejorado(
            T=3, lamda_t=lamda_t_i, intervals=interval_i)[0]
        suma_ii_m += poisson_no_homogeneo_adelgazamiento_mejorado(
            T=5, lamda_t=lamda_t_ii, intervals=interval_ii)[0]
        suma_iii_m += poisson_no_homogeneo_adelgazamiento_mejorado(
            T=6, lamda_t=lamda_t_iii, intervals=interval_iii)[0]

    print("i)")
    print(f"\tcomun:    {suma_i/n_sim}")
    print(f"\tmejorado: {suma_i_m/n_sim}")
    print("ii)")
    print(f"\tcomun:    {suma_ii/n_sim}")
    print(f"\tmejorado: {suma_ii_m/n_sim}")
    print("iii)")
    print(f"\tcomun:    {suma_iii/n_sim}")
    print(f"\tmejorado: {suma_iii_m/n_sim}")
