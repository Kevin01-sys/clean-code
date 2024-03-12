from abc import ABC, abstractmethod
from typing import List
from SOLID.DIP.refactored import Employee


class IEmployeePersistence(ABC):

    @abstractmethod
    def find_all(self) -> List[Employee]:
        pass

    @abstractmethod
    def save(self, employee: Employee) -> None:
        pass
