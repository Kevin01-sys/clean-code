from abc import ABC, abstractmethod


class ITrigonometricOperations(ABC):
    @abstractmethod
    def sine(self, angle):
        pass

    @abstractmethod
    def cosine(self, angle):
        pass
