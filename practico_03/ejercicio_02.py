import random





# para generar una variable aleatoria entere 0 y 1, lo que hacemos es llamar a random.random


def jugar() -> bool:

    """
    Se propone el siguiente juego en el cual todas las variables aleatorias que se generan son
    independientes e idénticamente distribuidas U(0,1): Se simula la variable aleatoria U. Si U <1/2, 
    se suman dos nuevos números aleatorios W1 +W2. Pero si U >= 1/2, se suman tres números aleatorios. 
    El resultado de la suma, en cualquiera de los casos, es una variable aleatoria X. 
    Se gana en el juego si X ≥ 1.
    """

    w0 = random.random()
    w1 = random.random()
    w2 = random.random()
    w3 = random.random()

    if w0 < 0.5:
        x = w1 + w2
    else: 
        x = w1 + w2 + w3

    return x >= 1




if __name__ == "__main__":


    # Ejercicio a: 
    # ¿Cuál es la probabilidad de ganar?.
    # resuelto en notas

    # Ejercicio b:
    # Implementar un algoritmo en computadora que estime la probabilidad de ganar, esto es, la fracción
    # de veces que se gana en n realizaciones del juego

    for n in [100, 1000, 10000, 100000, 1000000]:
        wins = 0
        for i in range(n):
            wins = wins+1 if jugar() else wins 
        print(f"n={n:<12} wins={wins:<12} ratio={wins/n}")
    