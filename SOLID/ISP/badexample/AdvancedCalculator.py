from math import sin, cos
from Operations import Operations


class AdvancedCalculator(Operations):
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        return a / b

    def sine(self, angle: float) -> float:
        return sin(angle)

    def cosine(self, angle: float) -> float:
        return cos(angle)
