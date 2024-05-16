import random
import math


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


if __name__ == "__main__":

    n_sim = 10_000
    arrivos = 0
    T = 9
    for _ in range(n_sim):
        arrivos += hot_dog(T)[0]
    print(f"esperanza: {arrivos/n_sim}")
