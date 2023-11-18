from lfsr_generator import LFSR


class SG:
    """ Генерирует псевдослучайную последовательность по алгоритму SG """


    def __init__(self, G1: LFSR, G2: LFSR):
        self.G1 = G1
        self.G2 = G2

    
    def generate(self):
        """ Генерирует псевдослучайную последовательность с помощью псевдослучайного прореживания """
        result = []
        elementary_sequence = self.G1.generate()
        selective_sequence = self.G2.generate()
        for i in range(len(selective_sequence)):
            if selective_sequence[i] == 1:
                if (i < len(elementary_sequence)):
                    result.append(elementary_sequence[i])
                else:
                    break
        return result
    

    def calc_period(self) -> int:
        """ Вычисляет и возвращает период """
        elementary_polynomial = self.G1.get_polynomial()
        selective_polynomial = self.G2.get_polynomial()
        return (2 ** (len(elementary_polynomial)) - 1) * (2 ** (len(selective_polynomial) - 1))
    

    def check_pirson(self, sequence: list[int]) -> str:
        """ Проверяет выполнение критерия Пирсона """
        K = 2
        P = 1 / K
        S_true = 3.8415
        S_star = len(sequence) * ((((sequence.count(0) / len(sequence) - P) ** 2) / P)
                                   + (((sequence.count(1) / len(sequence) - P) ** 2) / P))
        if S_star > S_true:
            return f"False, {S_star:.4f} (S*) > {S_true:.4f} (Sкр)"
        else:
            return f"True, {S_star:.4f} (S*) <= {S_true:.4f} (Sкр)"