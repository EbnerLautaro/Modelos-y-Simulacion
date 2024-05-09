import math
from .auxiliares import GeneradorVariableDiscreta

def binomial_transformada_inversa(n: int, p: float) -> int:
    """
    generacion de una variable aleatoria con distribucion binomial, utilizando la transformada inversa
    """

    def prob(i: int) -> float:
        fact = math.factorial # para que sea mas legible
        return (fact(n)/(fact(i)*fact(n-i)))*(p**i)*((1-p)**(n-i))

    probabilities = {i: prob(i) for i in range(n)}  

    gen = GeneradorVariableDiscreta()
    return gen.transformada_inversa(probs=probabilities)

def 



if __name__ == "__main__":
    # Implemente dos métodos para generar una binomial Bin(n, p):
    #     I) Usando transformada inversa.
    #     II) Simulando n ensayos con probabilidad de éxito p y contando el número de éxitos.

    # Para ambos métodos:
    #     a) Compare la eficiencia de ambos algoritmos para n = 10 y p = 0,3, evaluando el tiempo necesario para
    #         realizar 10000 simulaciones.
    #     b) Estime el valor con mayor ocurrencia y la proporción de veces que se obtuvieron los valores 0 y 10
    #         respectivamente.
    #     c) Compare estos valores con las probabilidades teóricas de la binomial. Si están alejados, revise el código.

    # si creamos la funcion de densidad de probabilidad y luego llamamos a la funcion transformada inversa generica, obtenemos la siguiente funcion
    print(binomial_transformada_inversa(10, 0.3))

