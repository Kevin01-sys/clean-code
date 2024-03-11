from math import sin, cos
from i_basic_operations import IBasicOperations
from i_trigonometric_operations import ITrigonometricOperations


class AdvancedCalculator(IBasicOperations, ITrigonometricOperations):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def sine(self, angle):
        return sin(angle)

    def cosine(self, angle):
        return cos(angle)
