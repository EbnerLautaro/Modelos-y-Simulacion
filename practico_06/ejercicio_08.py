from scipy.stats import chi2
import numpy as np


def simulacion_p_valor_gen(N, probs, T, n_sim):
    n = 0
    cont = 0
    while n <= n_sim:

        # calcular N_i
        N_list = []
        sum_probs = 0
        for prob in probs:
            N_i = np.random.binomial(
                n=N - sum(N_list),
                p=prob / (1-sum_probs),
            )
            N_list.append(N_i)
            sum_probs += prob

        # Calcular T
        t = 0
        for i in range(len(probs)):
            value = pow(N_list[i]-(N*probs[i]), 2) / (N*probs[i])
            t += value

        if t > T:
            cont += 1
        n += 1

    return cont/n_sim


if __name__ == "__main__":

    x = 2.1796
    df = 5
    print(f"estimacion de p-valor segun Pearson     {chi2.sf(x, df)}")

    estimate = simulacion_p_valor_gen(
        N=1000, probs=[1/6 for _ in range(6)], T=x, n_sim=10_000
    )

    print(f"simulacion de p-valor                   {estimate}")
