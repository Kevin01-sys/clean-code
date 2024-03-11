from Programmer import Programmer


class ProgrammerMemoryPersistence:
    def __init__(self):
        self.programmers = []

    def find_all(self) -> []:
        return self.programmers

    def save(self, programmer: Programmer) -> None:
        self.programmers.append(programmer)
