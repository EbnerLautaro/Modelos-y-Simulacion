import random


def juego():

    u = random.random()
    v = random.random()
    if max(u, v) > 0.6:
        return True
    return False


if __name__ == "__main__":
    
    wins = 0
    n = 10_000
    for _ in range(n):
        wins += int(juego())

    print(f"wins {wins}")
    print(f"wins/played {wins/n}")