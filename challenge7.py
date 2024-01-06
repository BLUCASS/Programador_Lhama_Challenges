'''A calculator receives two numbers to perform its calculation.

The first number is multiplied by 5 and divided by 8.
Then, the square root of the previous result is taken and raised to the cube.

The second number is squared and added to the initial value.
The previous result is multiplied by 2, divided by 5 and added to a constant of 5.7

Finally, the previous results are added together and the sum is multiplied by a constant of 4.2'''

# CONTROLLER
#############################################################################################################
class Calculator:

    def __init__(self) -> None:
        self.const1 = 5.7
        self.const2 = 4.2

    def first_number(self, n1) -> float:
        res1 = (n1 * 5) / 8
        tot1 = (res1 ** (0.5)) ** 3
        return tot1
    
    def second_number(self, n2) -> float:
        res2 = (n2 ** 2) + n2
        tot2 = ((res2 * 2) / 5) + self.const1
        return tot2

    def calculate(self, n1, n2) -> float:
        tot1 = self.first_number(n1)
        tot2 = self.second_number(n2)
        tot = (tot1 + tot2) * self.const2
        return tot


# VIEW
#############################################################################################################
calculator = Calculator()
res = calculator.calculate(1, 1)
print(res)