import time

from auxiliares import GeneradorVariableDiscreta

if __name__ == "__main__":
    # Implemente tres métodos para generar una variable X que toma los valores del 1 al 10, con
    # probabilidades p1 = 0,11, p2 = 0,14, p3 = 0,09, p4 = 0,08, p5 = 0,12, p6 = 0,10, p7 = 0,09, p8 =
    # 0,07, p9 = 0,11, p10 = 0,09 usando:
    # a) Método de rechazo con una uniforme discreta.
    # b) Transformada inversa.
    # c) Método de la urna: utilizar un arreglo A de tamaño 100 donde cada valor i está en exactamente pi ∗ 100
    # posiciones. El método debe devolver A[k] con probabilidad 0,01. ¿Por qué funciona?
    # Compare la eficiencia de los tres algoritmos realizando 10000 simulaciones.

    probabilities = {
        "x1": 0.11,
        "x2": 0.14,
        "x3": 0.09,
        "x4": 0.08,
        "x5": 0.12,
        "x6": 0.10,
        "x7": 0.09,
        "x8": 0.07,
        "x9": 0.11,
        "x10": 0.09,
    }

    def time_simulation(probabilities, function, n_sim) -> float:
        start = time.time()
        for _ in range(n_sim):
            function(probabilities)
        end = time.time()
        return end - start

    gen = GeneradorVariableDiscreta()

    for function in [gen.aceptacion_rachazo, gen.transformada_inversa, gen.urna_smart]:
        print (f"{function.__name__}")
        print (f"\ttime: {time_simulation(probabilities=probabilities, function=function, n_sim=10000)}")


