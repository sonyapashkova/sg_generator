class LFSR:
    """ Генерирует псевдослучайную последовательность по алгоритму LFSR """


    def __init__(self, polynomial: str):
        self.__polynomial = polynomial
        self.state = self.__load_state(len(polynomial))


    def __load_state(self, n: int) -> list[int]:
        """ Считывает начальное состояние из файла и возвращает его """
        states = []
        with open("state.txt", "r", encoding="utf-8") as file_in:
            states = file_in.read().split()
        for state in states:
            if (len(state) == n):
                return [int(i) for i in state]
        

    def get_polynomial(self) -> list[int]:
        """ Возвращает полином """
        return self.__polynomial
    
    
    def get_state(self):
        """ Возвращает начальное состояние """
        return self.state
       

    def __calc_new_bit(self, new_state: list) -> int:
        """ Считает и возвращет бит для получения нового состояния """
        new_bit = 0
        polynomial = self.get_polynomial()
        for i in range(len(polynomial)):
            if polynomial[i] == 1:
                 new_bit ^= new_state[i]
        return new_bit
    
    
    def generate(self) -> list[int]:
        """ Генерирует и возвращает псевдослучайную последовательность """
        result, new_state = [], []
        result.append(self.state[-1])
        new_state = self.state[:-1]
        new_state.insert(0, self.__calc_new_bit(self.state))
        while new_state != self.state:
            result.append(new_state[-1])
            new_bit = self.__calc_new_bit(new_state)
            new_state = new_state[:-1]
            new_state.insert(0, new_bit)
        return result
    