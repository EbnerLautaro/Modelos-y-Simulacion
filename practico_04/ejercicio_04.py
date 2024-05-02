import random
import collections

class GeneradorVariableDiscreta:
    """
    Generador de variables discretas a travezde distintos metodos
    """

    @staticmethod
    def transformada_inversa(probs: dict[any, float]) -> int:
        """
        Generador de variables aleatorias discretas a travez del metodo 
        de la transformada inversa.

        Parametros: 
            - probs: es una diccionario donde cada par key, value indica:
                - key: valor de la variable discreta
                - probabilidad del valor de la variable discreta 
        """
        assert sum(probs.values()) == 1.0, "La suma de las probabilidades debe ser 1.0"

        sorted_probs = sorted(probs.items(), key=lambda elem: elem[1])
        sorted_probs = collections.OrderedDict(sorted_probs)

        _sum = 0
        x = random.random()
        for key in sorted_probs.keys():
            _sum += sorted_probs.get(key)
            sorted_probs.update({key: _sum})

            if x <= _sum:
                return key
        # te juro que nunca no retorna :)
        raise ValueError

    @staticmethod
    def urna(probs: dict[any, float], k:int) -> any:
        
        array: list[any] = []
        for key, value in probs.items():
            for _ in range(int(value*k)):
                array.append(key)

        return array[int(random.random()*k)]

    def urna_smart(self, probs: dict[any, float]) -> any:
        k = 0
        for _, value in probs.items():
            k = max(k, len(str(value).split(".")[1]))
        k = 10**k

        return self.urna(probs=probs, k=k)

    def aceptacion_rachazo(self, probs: dict[any, float]) -> any:
        
        while True:

            pos_y = random.randint(1, len(probs.keys()))
            y = list(probs.keys())[pos_y-1]
            p_y = probs.get(y)
            u = random.random()
            if u < p_y:
                return y


def test_functions(probs: dict[any, float], funcs: list, n_sim:int=10**6):
    
    for f in funcs:
        probs_count = {key: 0 for key in probs.keys()}

        for _ in range(n_sim):
            var = f(probs)
            probs_count.update({var: (probs_count.get(var)+1)})

        probs_count = {key: (value/n_sim) for key, value in probs_count.items()}

        print(f"function: {f.__name__}")
        print(f"actual   : {probs}")
        print(f"simulated: {probs_count}")
        print("=========================================================")


if __name__ == "__main__":
    pass











