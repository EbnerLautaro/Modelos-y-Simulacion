import math
import numpy
from ejercicio_05 import MonteCarlo

def aproximacion_pi(n_sim: int):
    """
    Calcula una aproximacion de pi por metodo de monte carlo
    """

    def func(x, y):
        if (x**2 + y**2) < 1:
            return 1
        return 0

    int_a = [-1, -1]
    int_b = [1, 1]

    mc = MonteCarlo()
    return mc.monte_carlo_n_vars_a_b(g=func, a=int_a, b=int_b, n_vars=2, n_sim=n_sim)




if __name__ == "__main__":

    for n in [1_000, 10_000, 100_000, 1_000_000]:
        aproximacion = aproximacion_pi(n_sim=n)
        print(f"n: {n:<8} aproximacion {aproximacion:<12}")

    print(f"valor de math.pi:  {math.pi}")
    print(f"valor de numpy.pi: {numpy.pi}")
