from math import gcd as mcd


class Generadores: 
    """
    Implementacion de los siguientes generadores
    - von neumann
    - congruencial_lineal 
    - congruencial_lineal_mixto
    
    Ademas un extra para verificar si un generador congruencial lineal es de parametro maximo
    - is_congruencial_periodo_maximo
    """

    def von_neumann(self, u: int) -> int:
        """
        Dada una semilla u, calculamos von_neuman de esa semilla
        """
        return (u**2 // 100) % 10_000

    def congruencial_lineal(self, a: int, y: int, c: int, m: int):
        """
        Dada una semilla, retorna ((a*y) + c) % M
        """
        return ((a*y) + c) % m

    def congruencial_lineal_multiplicativo(self, a: int, y: int, m: int):
        """
        Dada una semilla, retorna ((a*y)) % M
        """
        return self.congruencial_lineal(a, y, 0, m)

    def is_congruencial_periodo_maximo(self, a: int, c: int, m: int) -> bool:
        """
        Dados los parametros a, c, m retorna si un generador 
        congruencial lineal con estos parametros, seria de periodo maximo 
        """
        def descomponer_en_factores_primos(n: int):
            """ 
            Descompone un numero n en primos
            """
            primo = 2
            factores = []
            while primo * primo <= n:
                if (n % primo) != 0:
                    primo += 1
                else:
                    n /= primo
                    factores.append(primo)
            if n > 1:
                factores.append(n)
            return factores

        # c distinto de 0
        if c == 0:
            return False

        # El maximo comun divisor entre c y m es 1
        if mcd(c, m) != 1:
            return False

        # a ≡ 1 mod p, para todo factor primo p de M
        for p in descomponer_en_factores_primos(m):
            if (a % p) != 1:
                return False

        # si 4|m, entonces a ≡ 1 mod 4
        if (m % 4 == 0) and (a % 4 != 1):
            return False

        return True


if __name__ == "__main__":

    gen = Generadores()

    print("\n============ EJERCICIO a ============")

    for i in [3792, 1004, 2100, 1234]:
        secuencia = []
        x = i
        for _ in range(10):
            x = gen.von_neumann(x)
            secuencia.append(x)
        print(f"{x}: {secuencia}")

    print("\n============ EJERCICIO B ============")

    for i in [4, 50]:
        secuencia = []
        x = i
        for _ in range(10):
            x = gen.congruencial_lineal(x, 5, 4, 2**5)
            secuencia.append(x)
        print(f"{x}: {secuencia}")

    print("\n============ EJERCICIO C ============")

    for a, c, m in [(125, 3, 2**9), (123, 3, 2**9), (5, 0, 71), (7, 0, 71)]:
        print(f"{(a,c,m)}: {gen.is_congruencial_periodo_maximo(a,c,m)}")
