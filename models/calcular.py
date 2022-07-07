from random import randint


class Calcular:
    def __init__(self: object, dificuldade: int,/) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3) # 1 = somar, 2 = diminuir, 3 = multiplicar
        self.__resultado: int = self._gerar_resultado

