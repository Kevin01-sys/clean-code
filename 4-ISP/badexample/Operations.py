from abc import ABC, abstractmethod


class Operations(ABC):
    @abstractmethod
    def add(self, a: float, b: float) -> float:
        pass

    @abstractmethod
    def subtract(self, a: float, b: float) -> float:
        pass

    @abstractmethod
    def multiply(self, a: float, b: float) -> float:
        pass

    @abstractmethod
    def divide(self, a: float, b: float) -> float:
        pass

    @abstractmethod
    def sine(self, angle: float) -> float:
        pass

    @abstractmethod
    def cosine(self, angle: float) -> float:
        pass
