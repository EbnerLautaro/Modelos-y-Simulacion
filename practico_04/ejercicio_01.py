import numpy as np

if __name__ == "__main__":

    # c) Escriba un programa de simulación para estimar la esperanza y la varianza del número total de éxitos,
    # y de los eventos del inciso (a) con r=10, y compare los resultados obtenidos con 100, 1000, 10000
    # y 100000 iteraciones.

    # ejercicio c) con el inciso (a)(i)
    card_count = 10
    r = 1
    cards = np.arange(card_count)

    for n in [100, 1_000, 10_000, 100_000]:
        mean = 0
        mean_x_squared = 0
        for _ in range(n):
            cards_shuffle = np.random.permutation(cards)
            successes = sum(cards[:r] == cards_shuffle[:r]) == r
            
            mean += successes
            mean_x_squared += (successes**2)    

        variance = (mean**2) - mean_x_squared
        print(f" ============== (n = {n}) ============== ")
        print(f"esperanza: {mean/n:<12} \tvarianza: {variance/n:<12}")
