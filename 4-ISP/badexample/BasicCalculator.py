from Operations import Operations


class BasicCalculator(Operations):
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def sine(self, angle: float) -> float:
        raise NotImplementedError("Basic Calculator does not support trigonometric operations")

    def cosine(self, angle: float) -> float:
        raise NotImplementedError("Basic Calculator does not support trigonometric operations")
