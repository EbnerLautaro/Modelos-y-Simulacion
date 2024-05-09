import time
from auxiliares import GeneradorVariableDiscreta

if __name__ == "__main__":

    gen = GeneradorVariableDiscreta()

    # Una variable aleatoria X tiene una función de probabilidad puntual pi = P(X = i) dada por
    # p0 = 0,15, p1 = 0,20, p2 = 0,10, p3 = 0,35, p4 = 0,20
    # I) Describir mediante un pseudocodigo un algoritmo que simule X utilizando el método de la transformada inversa y que minimice el número esperado de búsquedas.
    # II) Describir mediante un pseudocodigo un algoritmo que simule X utilizando el método de aceptación y rechazo con una variable soporte Y con distribución binomial B(4, 0.45).
    # III) Compare la eficiencia de los dos algoritmos realizando 10000 simulaciones

    probabilities = [(0, 0.15), (1, 0.2), (2, 0.10), (3, 0.35), (4, 0.2)]

    start = time.time()
    for _ in range(10_000):
        gen.transformada_inversa(probabilities=probabilities)
    print(f"transformada_inversa \n\ttime {time.time()-start}")
