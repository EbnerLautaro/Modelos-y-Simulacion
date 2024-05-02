import random


def jugar():
    puntaje = 0

    t1 = random.randint(1, 6)
    if t1 in [1, 6]:
        puntaje = t1 * 2
    else:
        t2 = random.randint(1, 6)
        t3 = random.randint(1, 6)
        puntaje = t2 + t3

    return puntaje > 6





if __name__ == "__main__":
    
    for n in [10**2, 10**3, 10**4, 10**5, 10**6]:
        wins = 0
        for _ in range(n):
            wins += 1 if jugar() else 0

        print(f"n: {n}, ratio: {wins/n}")


