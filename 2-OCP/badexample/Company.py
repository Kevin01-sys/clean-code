from Programmer import Programmer
from ProgrammerMemoryPersistence import ProgrammerMemoryPersistence


class Company:
    def __init__(self):
        self.persistence = ProgrammerMemoryPersistence()

    def get_programmers(self) -> []:
        return self.persistence.find_all()

    def add_programmer(self, full_name, salary) -> None:
        self.persistence.save(Programmer(full_name, salary))
