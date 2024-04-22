import random
from scipy.stats import expon

def simulacion_a():
    cont = 0
    for _ in range(1_000):

        u = random.random()

        # caja 1
        if u < 40/100:
            espera = float(expon.rvs(loc=0, scale=3, size=1)[0])

        # caja 2
        elif u < 72/100:
            espera = float(expon.rvs(loc=0, scale=4, size=1)[0])

        # caja 3
        else:
            espera = float(expon.rvs(loc=0, scale=5, size=1)[0])

        cont += 1 if espera < 4.0 else 0
    return cont

def simulacion_b():

    ocurrencias = [0, 0, 0]
    for _ in range(1_000):

        u = random.random()

        # caja 1
        if u < 40/100:
            espera = float(expon.rvs(loc=0, scale=3, size=1)[0])
            if espera > 4:
                ocurrencias[0] += 1
        # caja 2
        elif u < 72/100:
            espera = float(expon.rvs(loc=0, scale=4, size=1)[0])
            if espera > 4:
                ocurrencias[1] += 1

        # caja 3
        else:
            espera = float(expon.rvs(loc=0, scale=5, size=1)[0])
            if espera > 4:
                ocurrencias[2] += 1

    return ocurrencias, sum(ocurrencias)



if __name__ == "__main__":


    print("========== Simulacion Ejercico A ==========\n")


    ocurrencias = simulacion_a()
    print("Cantidad de veces que los clientes esperaron menos de 4 min:", ocurrencias)
    print("Ratio:", ocurrencias/1_000)


    print("\n========== Simulacion Ejercico B ==========\n")
    


    ocurrencias, suma = simulacion_b()



    print("una ocurrencia es cuando se da que el cliente espero mas de 4 minusos en una caja")
    for i in range(3):
        print(f"Caja {i+1 :<12} ocurrencias {ocurrencias[i] :<12} ratio {ocurrencias[i]/suma :<12}")
