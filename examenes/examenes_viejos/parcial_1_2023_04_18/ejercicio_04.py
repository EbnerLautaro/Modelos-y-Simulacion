import random

def simulacion_b():
    u = random.random()
    v = random.random()
    # si gana en la primera
    if u > 0.5 and v < 0.5:
        return True
    
    elif u < 0.5 and v > 0.5:
        return False
    
    u = random.random()
    v = random.random()
    # si gana en la primera
    if u > 0.5 and v < 0.5:
        return True
    
    return False


if __name__ == "__main__":

    cont = 0
    for _ in range(1_000_000):
        cont += 1 if simulacion_b() else 0

    print(f"cont: {cont}")
    print(f"probablidad: {cont/1_000_000}")
    print(f"3/8: {3/8}")
