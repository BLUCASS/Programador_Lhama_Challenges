# MODEL
#############################################################################################################

''' Now using the concept of Abstract Methods'''

from abc import ABC, abstractmethod

class Calculator(ABC):

    def __init__(self) -> None:
        self.const1 = 5.7
        self.const2 = 4.2

    def first_number(self, n1) -> float:
        res1 = (n1 * 5) / 8
        tot1 = (res1 ** (0.5)) ** 3
        return tot1
    
    @abstractmethod
    def second_number(self, n2) -> float:
        pass

    def calculate(self, n1, n2) -> float:
        tot1 = self.first_number(n1)
        tot2 = self.second_number(n2)
        tot = (tot1 + tot2) * self.const2
        return tot


# CONTROLLER
#############################################################################################################
class Calculator1(Calculator):

    def second_number(self, n2) -> float:
        res2 = (n2 ** 2) + n2
        tot2 = ((res2 * 2) / 5) + self.const1
        return tot2
    
class Calculator2(Calculator):

    def __init__(self) -> None:
        super().__init__()
        self.const3 = 1.2

    def second_number(self, n2) -> float:
        res = ((n2 ** 3) - n2) * 2
        res = res + self.const3
        return res
    

# VIEW
#############################################################################################################
calculator1 = Calculator1()
calculator2 = Calculator2()
print(calculator1.calculate(1, 1))
print(calculator2.calculate(1, 1))