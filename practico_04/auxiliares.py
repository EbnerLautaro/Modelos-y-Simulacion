import random


def test_functions(probs: dict[any, float], funcs: list, n_sim: int = 10**6):

    for func in funcs:
        probs_count = {key: 0 for key in probs.keys()}

        for _ in range(n_sim):
            var = func(probs)
            probs_count.update({var: (probs_count.get(var) + 1)})

        probs_count = {key: (value / n_sim)
                       for key, value in probs_count.items()}

        print(f"function: {func.__name__}")
        print(f"actual   : {probs}")
        print(f"simulated: {probs_count}")
        print("=========================================================")


class GeneradorVariableDiscreta:

    @staticmethod
    def transformada_inversa(probabilities: list[tuple[any, int]], optimize: bool = True):
        """
        Generador de variables aleatorias discretas a travez del metodo
        de la transformada inversa.

        Params    
            - probabilities: cada elemento tiene la forma: (valor, probabilidad)
            - optimize: 

        Considerar:
            - no se verifica que la sumatoria de las probabilidades sea 1
        """
        if optimize:
            probabilities = sorted(probabilities, key=lambda elem: elem[1])

        i = 0
        u = random.random()
        acumulador = probabilities[0][1]
        while u >= acumulador:
            i += 1
            acumulador += probabilities[i][1]
        return probabilities[i][0]

    @staticmethod
    def urna(probs: dict[any, float], k: int) -> any:
        """
        Generador de variables aleatorias discretas a travez del metodo
        de la urna.
        Se debe proporcionar un parametro k tal que para todo valor de probs, (valor*k) sea entero
        """
        array: list[any] = []
        for key, value in probs.items():
            for _ in range(int(value * k)):
                array.append(key)

        return array[int(random.random() * k)]

    def urna_smart(self, probs: dict[any, float]) -> any:
        """
        Generador de variables aleatorias discretas a travez del metodo
        de la urna.
        Se determina el valor de k (tamaño de array de forma automatica,
        no de la forma mas eficiente)
        """
        k = 0
        for _, value in probs.items():
            k = max(k, len(str(value).split(".")[1]))
        k = 10**k

        return self.urna(probs=probs, k=k)

    def aceptacion_rachazo(self, probs: dict[any, float]) -> any:
        """
        Generador de variables aleatorias discretas a travez del metodo de aceptacion
        y rechazo, la variable auxiliar se genera a travez de random.randint()
        """
        while True:

            pos_y = random.randint(1, len(probs.keys()))
            y = list(probs.keys())[pos_y - 1]
            p_y = probs.get(y)
            u = random.random()
            if u < p_y:
                return y

    @staticmethod
    def aceptacion_rechazo_2(
        probabilities: list[tuple[any, int]],
        y_probabilities: list[tuple[any, int]],
        var_aux
    ):
        """
        Parametros:
            - probabilities: pares (valor, p(valor)) de la variable a generar
            - y_probabilities: pares (valor, p(valor)) de la variale auxiliar
            - var_aux: funcion que genera una variable con valores y probabilidades dadas por y_probabilities
        """
        filtered_probs_y = []
        flattened_p = [elem[0] for elem in probabilities]
        for elem in y_probabilities:
            if elem[0] in flattened_p:
                filtered_probs_y.append(elem)

        max_p = max(probabilities, key=lambda elem: elem[1])
        max_py = min(filtered_probs_y, key=lambda elem: elem[1])
        c = int(max_p / max_py)
        assert c > 1

        while True:
            y = var_aux()
            u = random.random()
            if u < (probabilities[y][1] / (c * y_probabilities[y][1])):
                return y

    @staticmethod
    def distribucion_binomial(n: int, p: float) -> int:
        """
        Si consideramos un experimento que consiste en n ensayos independientes, cada uno con probabilidad
        p de exito, entonces el numero de exitos tiene una distribucion binomial de parametros n y p
        """
        acum = (1 - p) ** n
        f = acum
        n_exitos = 0
        x = random.random()
        while x >= f:
            acum *= p / (1 - p) * (n - n_exitos) / (n_exitos + 1)
            f += acum
            n_exitos += 1

        return n_exitos
