import random
import math


class MonteCarlo:
    """
    Contiene todas las funciones necesarias para calcular distintos tipos de
    aproximaciones de integrales por metodo de montecarlo.
    """

    def monte_carlo(self, g, n_sim: int):
        """
        Aproximacion de la integral de la funcion g sobre el intervalo [0, 1].
        """
        integral = 0

        for _ in range(n_sim):
            u = random.random()
            integral += g(u)

        return integral / n_sim

    def monte_carlo_a_b(self, g, a: int, b: int, n_sim: int):
        """
        Aproximacion de la integral de la funcion g sobre el intervalo [a, b].
        """
        assert a < b

        integral = 0

        for _ in range(n_sim):
            u = random.random()
            integral += g(a + (b-a) * u)

        return integral / n_sim

    def monte_carlo_0_inf(self, g, n_sim: int):
        """
        Aproximacion de la integral de la funcion g sobre el intervalo [0, inf].
        """

        def h(y):
            return (1/y**2) * g((1/y) - 1)

        integral = 0

        for _ in range(n_sim):
            u = random.random()
            integral += h(u)

        return integral / n_sim

    def monte_carlo_n_vars(self, g, n_vars: int, n_sim: int):
        """
        Aproximacion de la integral de la funcion g (de n variables) sobre el intervalo [0, 1].
        """
        integral = 0

        for _ in range(n_sim):
            params = [random.random() for _ in range(n_vars) ]
            integral += g(*params)

        return integral / n_sim


    def monte_carlo_n_vars_a_b(self, g, a: list, b: list, n_vars, n_sim):
        """
        Aproximacion de la integral de la funcion g (de n variables) sobre los intervalos dados por a_i, b_i.
        Aclaracion:
            si la funcion es g(x, y) entonces los parametros a y b 
            tiene que ser a=[x_a, y_a], b=[x_b, y_b] en ese orden.
        """
        
        
        integral = 0

        for _ in range(n_sim):
            r_vars = [a[i] + (b[i]-a[i]) * random.random() for i in range(n_vars)]
            integral += g(*r_vars)

        multiplicador = 1
        for i in range(n_vars):
            multiplicador *= (a[i]-b[i])


        return integral * multiplicador/ n_sim

    def monte_carlo_n_vars_0_inf(self, g, n_vars, n_sim):
        """
        Aproximacion de la integral de la funcion g (de n variables) sobre el intervalo [0, inf].
        """
        integral = 0

        for _ in range(n_sim):

            r_vars = [random.random() for _ in range(n_vars)]
            params = [1/u - 1 for u in r_vars]

            denominador = 1
            for var in r_vars:
                denominador *= var**2

            integral += g(*params)/denominador

        return integral / n_sim


if __name__ == "__main__":


    def func_a(x):
        return (1-x**2)**(3/2)

    def func_b(x):
        return (x)/((x**2)-1)

    def func_c(x):
        return x*(1 + (x**2))**(-2)

    def func_d(x):
        # la integral es de -inf a inf, luego de transformarla, como es simetrica, 
        # queda la integral de 0 a inf de esta funcion
        return 2* (math.e ** -(x**2))

    def func_e(x, y):
        return math.e ** ((x+y) ** 2)

    def func_f(x, y):
        return math.e ** -(x+y)


    mc = MonteCarlo()


    # print("\n============ a ============")
    # for n in [100, 1_000, 10_000, 100_000, 1_000_000]:
    #     aprox = mc.monte_carlo(func_a, n)
    #     print(f"n: {n:<10} aproximacion: {aprox:<12}")
    # print("Resultado exacto: 0.5890486225")

    # print("\n============ b ============")
    # for n in [100, 1_000, 10_000, 100_000, 1_000_000]:
    #     aprox = mc.monte_carlo_a_b(g=func_b,a=2, b=3, n_sim=n)
    #     print(f"n: {n:<10} aproximacion: {aprox:<10}")
    # print("Resultado exacto: 0.49041")


    # print("\n============ c ============")
    # for n in [100, 1_000, 10_000, 100_000, 1_000_000]:
    #     aprox = mc.monte_carlo_0_inf(g=func_c, n_sim=n)
    #     print(f"n: {n:<10} aproximacion: {aprox:<10}")
    # print("Resultado exacto: 0.5")

    # print("\n============ d ============")
    # for n in [100, 1_000, 10_000, 100_000, 1_000_000]:
    #     aprox = mc.monte_carlo_0_inf(g=func_d, n_sim=n)
    #     print(f"n: {n:<10} aproximacion: {aprox:<10}")
    # print("Resultado exacto: 1.77245385090")

    # print("\n============ e ============")
    # for n in [100, 1_000, 10_000, 100_000, 1_000_000]:
    #     aprox = mc.monte_carlo_n_vars(g=func_e, n_vars=2, n_sim=n)
    #     print(f"n: {n:<10} aproximacion: {aprox:<10}")





    def f_random(x,y):
        return (math.e) ** ((x+y)**(2/5))





    print(mc.monte_carlo_n_vars_a_b(g=f_random, a=[1,8.9], b=[2,9], n_vars=2, n_sim=1_000_000))