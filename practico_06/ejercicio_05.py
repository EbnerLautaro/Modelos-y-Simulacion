import random, math


def simulacion():
    values = [random.random(), random.random()]
    i = 1
    while values[i - 1] <= values[i]:

        values.append(random.random())
        i += 1

    return len(values)


def stats_sim(sim, n_sim):
    assert n_sim >= 1
    mu = sim()
    S_sq = 0
    n = 1

    while n < n_sim:

        mu_ant = mu
        mu = mu_ant + (sim() - mu_ant) / (n + 1)

        S_sq_ant = S_sq
        S_sq = (1 - (1 / n)) * S_sq_ant + (n + 1) * (mu - mu_ant) ** 2
        n += 1

    return mu, S_sq, n


def stats_sim_d_var(sim, threshold, min_sim):
    mu = sim()
    S_sq = 0
    n = 1

    while n <= min_sim or S_sq / n > threshold:

        mu_ant = mu
        mu = mu_ant + (sim() - mu_ant) / (n + 1)

        S_sq_ant = S_sq
        S_sq = (1 - (1 / n)) * S_sq_ant + (n + 1) * (mu - mu_ant) ** 2
        n += 1

    return mu, S_sq, n


def stats_sim_d_ic(sim, threshold, min_sim):
    mu = sim()
    S_sq = 0
    n = 1

    while n <= min_sim or ic > threshold:

        mu_ant = mu
        mu = mu_ant + (sim() - mu_ant) / (n + 1)

        S_sq_ant = S_sq
        S_sq = (1 - (1 / n)) * S_sq_ant + (n + 1) * (mu - mu_ant) ** 2
        n += 1

        ic = math.sqrt(S_sq / n)

    return mu, S_sq, n, ic


if __name__ == "__main__":

    d = 0.01
    print(f"valor real de e:        {math.e}")
    print(" ejercicio b ".center(100, "-"))

    mu, var, n = stats_sim(sim=simulacion, n_sim=10_000)

    print(f"estimacion              {mu}")
    print(f"var                     {var}")
    print(f"iter                    {n}")

    print(" ejercicio c ".center(100, "-"))
    mu, var, n = stats_sim_d_var(sim=simulacion, threshold=d, min_sim=10)
    print(f"estimacion              {mu}")
    print(f"var                     {var}")
    print(f"iter                    {n}")

    print(" ejercicio d ".center(100, "-"))
    d = 0.1 / (1.96 * 2)

    mu, var, n, ic = stats_sim_d_ic(sim=simulacion, threshold=0.01, min_sim=10)
    print(f"estimacion              {mu}")
    print(f"var                     {var}")
    print(f"iter                    {n}")
    print(f"ic                      ({mu-ic}, {mu+ic})")
