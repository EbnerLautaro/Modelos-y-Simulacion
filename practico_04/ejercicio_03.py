import math
import random


def tirar_dados() -> int:
    return random.randint(1,6) + random.randint(1,6)

def juego() -> int:
    # hacemos esto porque pepe me dijo que no era optimo 🤓 
    resultados = {
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "12": 0
    }

    while 0 in resultados.values():
        resultados[str(tirar_dados())] += 1
    
    assert len(resultados.keys()) == 11
    
    return sum(resultados.values())


if __name__ == "__main__":

    print("============================ Ejercicio (b) ===========================")
    for n in [100, 1000, 10000, 100000]:
        media =  0
        media_cuadrada =  0
        N9, N15 = 0, 0
        for _ in range(n):
            N = juego()
            media += N/n
            media_cuadrada += (N**2)/n 
            N15 += int(N>=15)
            N9 += int(N<=9)

        desviacion = math.sqrt(media_cuadrada - (media**2))
        print(f"iteraciones: {n}")
        print(f"Media: {media:<12}")
        print(f"Desviacion: {desviacion:<12}")
        print(f"P(N>=15): {N15/n:<12} P(N<=9): {N9/n:<12}")
        print("======================================================================")
