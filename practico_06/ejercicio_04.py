import random, math


def simulacion():
    suma = 0
    cont = 0
    while suma < 1:
        suma += random.random()
        cont += 1
    return cont


if __name__ == "__main__":

    print(" ejercicio a ".center(100, "-"))
    print(f"valor real:     {math.e}")
    print(f"aproximacion:   {sum(simulacion() for _ in range(10_000))/10_000}")
