from hw_4 import Addition
from hw_4 import Subtraction
from hw_4 import Multiply
from hw_4 import Division

class Calculator(Addition, Subtraction, Multiply, Division):
    def additions(*val1):
       print(Calculator.Additions(*val1))
       pass

    def subtract(val1, val2):
       print(Calculator.Substraction(val1, val2))
       pass

    def multy(val1, val2):
       print(Calculator.Multiplication(val1, val2))
       pass
    def division(val1, val2):
       print(Calculator.Division(val1, val2))
       pass


