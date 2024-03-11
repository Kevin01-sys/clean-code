from Mammal import Mammal
from CannotWalkException import CannotWalkException


class Dolphin(Mammal):
    def walk(self):
        raise CannotWalkException("I am a dolphin, I cannot walk!")