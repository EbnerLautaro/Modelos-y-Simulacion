import random
import collections

class GeneradorVariableDiscreta:

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

