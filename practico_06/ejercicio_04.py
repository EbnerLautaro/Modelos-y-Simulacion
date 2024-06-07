import random, math


def simulacion():
    suma = 0
    cont = 0
    while suma < 1:
        suma += random.random()
        cont += 1
    return cont


def var_simulacion(sim, n_sim):
    assert n_sim >= 1
    mu = sim()
    S_sq = 0
    n = 1

    while n <= n_sim:

        mu_ant = mu
        mu = mu_ant + (sim() - mu_ant) / (n + 1)

        S_sq_ant = S_sq
        S_sq = (1 - (1 / n)) * S_sq_ant + (n + 1) * (mu - mu_ant) ** 2
        n += 1

    return S_sq


def var_muestral_ic(sim, d_threshold, sim_min=100):
    mu = sim()
    S_sq = 0
    n = 1

    while n <= sim_min or ic > d_threshold:

        mu_ant = mu
        mu = mu_ant + (sim() - mu_ant) / (n + 1)

        S_sq_ant = S_sq
        S_sq = (1 - (1 / n)) * S_sq_ant + (n + 1) * (mu - mu_ant) ** 2
        n += 1

        ic = math.sqrt(S_sq / n)

    return mu, S_sq, n, ic


if __name__ == "__main__":

    print(" ejercicio a ".center(100, "-"))
    print(f"valor real     {math.e}")
    print(f"aproximacion   {sum(simulacion() for _ in range(10_000))/10_000}")

    print(" ejercicio b ".center(100, "-"))

    n = 1_000
    print("expresion derivada")
    print(f"\tVar(Ñ) n={n}   {(math.e * 3 - math.e**2)/n:f}")
    print("expresion simulada")
    print(f"\tVar(Ñ) n={n}   {var_simulacion(simulacion, n)}")

    print(" ejercicio c ".center(100, "-"))

    long = 0.025
    z_alpha_2 = 1.96
    d = long / 2 * z_alpha_2

    aprox, var, n, ic = var_muestral_ic(sim=simulacion, d_threshold=d, sim_min=1_000)

    F = ":.4f"

    print(f"media       {aprox}")
    print(f"intervalo   ({aprox-ic:F}, {aprox+ic:F})")
    print(f"var         {var}")
