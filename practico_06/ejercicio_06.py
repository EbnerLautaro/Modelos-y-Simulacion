import random, math


def area(n_sim):

    area = 0
    n = 0
    while n <= n_sim:
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)

        if pow(x, 2) + pow(y, 2) <= 1:
            area += 1

        n += 1
    return 4 * area / n_sim


def f():
    """
    No tengo idea que nombre ponerle a esta funcion
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    return pow(x, 2) + pow(y, 2) <= 1


def area_proporcion(sim, threshold, sim_min=100):

    mu = sim()
    n = 1
    S_sq = 0

    while n <= sim_min or math.sqrt(S_sq / n) > threshold:

        mu_ant = mu
        mu = mu_ant + (sim() - mu_ant) / (n + 1)

        S_sq = mu * (1 - mu)
        n += 1

    return mu, n


def area_d_ic(sim, threshold, sim_min=100):

    mu = sim()
    n = 1
    S_sq = 0

    while n <= sim_min or ic > threshold:

        mu_ant = mu

        mu = mu_ant + (sim() - mu_ant) / (n + 1)
        S_sq = mu * (1 - mu)
        n += 1

        ic = math.sqrt(S_sq / n)

    return mu, n, ic


if __name__ == "__main__":

    F = ".5f"
    print(f"valor real  {math.pi:F}")
    print(f"simulacion  {area(10_000):F}")

    print(" ejercicio a ".center(100, "-"))

    p, n = area_proporcion(f, 0.01)

    print(f"proporcion      {p}")
    print(f"simulations     {n}")

    print(" ejercicio b ".center(100, "-"))

    z_alpha_2 = 1.96
    long = 0.1
    d = long / (2 * z_alpha_2)

    mu, n, ic = area_d_ic(sim=f, threshold=d)
    # hacemos 4*mu porque mu es la proporcion de puntos que caen dentro del circulo
    mu *= 4
    print(f"estimacion      {mu}")
    print(f"iter            {n}")
    print(f"ic              ({mu-z_alpha_2*ic}, {mu+z_alpha_2*ic})      dif {1.96*ic}")
