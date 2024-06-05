import random
import math


def exponencial(lambd: float = 1.0) -> float:
    u = 1 - random.random()
    return -math.log(u)/lambd


def normal(mu: float = 0.0, sigma: float = 1.0) -> float:
    while True:
        Y1 = exponencial()
        Y2 = exponencial()
        if Y2 >= ((Y1 - 1) ** 2)/2:
            if random.random() <= 1/2:
                return Y1 * sigma + mu
            else:
                return Y2 * sigma + mu


def generar_normales(n_values: int = 100) -> list[float]:
    values = []
    while True:
        values_to_insert = [normal() for _ in range(n_values - len(values))]
        values.extend(values_to_insert)

        mean = sum(values)/len(values)
        mean_sq = sum(value ** 2 for value in values) / len(values)
        variance = mean_sq - (mean**2)
        deviance = math.sqrt(variance)

        if deviance/math.sqrt(len(values)) <= 0.1:
            break
        else:
            n_values += 1
    return values, mean, variance


if __name__ == "__main__":

    # Genere n valores de una variable aleatoria normal estándar de manera tal que se cumplan
    # las condiciones: n ≥ 100 y S/√n < 0,1, siendo S el estimador de la desviación estándar de los n datos
    # generados.

    contador: int = 0
    media: float = 0
    varianza: float = 0
    n_sim = 10_000

    for _ in range(n_sim):
        values, mean, variance = generar_normales()
        contador += len(values)
        media += mean
        varianza += variance
    contador /= n_sim
    media /= n_sim
    varianza /= n_sim

    print("a) ¿Cuál es el número de datos generados efectivamente?")
    print(f"contador\t{contador}")
    print("b) ¿Cuál es la media muestral de los datos generados?")
    print(f"media   \t{media}")
    print("c) ¿Cuál es la varianza muestral de los datos generados?")
    print(f"varianza\t{varianza}")
