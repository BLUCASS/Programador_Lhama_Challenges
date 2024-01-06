'''Implement 2 calculators. Both performing similar calculations;
however, the second calculator differs from the first in the calculation of the second number:
The second number is raised to the power of three.
After that, the obtained result is subtracted from the initial value of the second number and
then multiplied by two. 
Finally, the result is added to another constant of proportionality with a value of 1.2.

It is worth noting that the calculations of the first calculator remain the same.

Using the concept of Class Inheritance.'''

# CONTROLLER
#############################################################################################################
from challenge8_2 import Calculator

class SecondCalculator(Calculator):

    def __init__(self) -> None:
        super().__init__()
        self.const3 = 1.2

    def third_function(self, n1):
        res = super().second_number(n1)
        res = (res - n1) * 2
        tot = res + self.const3
        return tot


# VIEW
#############################################################################################################
calculator = SecondCalculator()
print(calculator.calculate(1, 1))
print(calculator.third_function(1))